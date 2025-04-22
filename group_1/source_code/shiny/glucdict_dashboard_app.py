from shiny import App, ui, render, run_app
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
synthetic_nhanes = pd.read_csv("../../Datasets/synthetic_nhanes.csv")
results_df = pd.read_csv("../results_df.csv")

# Filter to glucdict-derived columns only (excluding 'index')
glucdict_prefixes = [ 'glucose', 'resting_hr', 'mean_hr', 'avg_daily_steps', 'hr_zone', 'avg_weekly', 'avg_daily', 'accelerometer', 'gyroscope', 'magnetic_field', 'gravity']
numeric_cols = [
    col for col in synthetic_nhanes.select_dtypes(include='number').columns
    if any(col.startswith(prefix) for prefix in glucdict_prefixes)
]

# UI
app_ui = ui.page_fluid(
    ui.h2("Health Data Dashboard"),
    ui.navset_tab(
        ui.nav_panel("Feature Comparison",
            ui.input_select("feature", "Select a feature:", choices=numeric_cols),
            ui.output_plot("feature_plot", height="800px")
        ),
        ui.nav_panel("Model Performance",
            ui.output_plot("model_plot", height="800px")
        ),
        ui.nav_panel("Training Time",
            ui.output_plot("training_plot", height="800px")
        )
    )
)

# Server
def server(input, output, session):
    @output
    @render.plot
    def feature_plot():
        plt.figure(figsize=(8, 12))
        sns.boxplot(data=synthetic_nhanes, x='diabetes_status', y=input.feature())
        plt.title(f"{input.feature()} by Diabetes Status")
        plt.tight_layout()
        return plt.gcf()

    @output
    @render.plot
    def model_plot():
        plt.figure(figsize=(10, 5))
        melted = results_df.melt(id_vars='Model', var_name='Metric', value_name='Score')
        filtered = melted[melted["Metric"] != "Training Time (Mean)"]
        sns.barplot(data=filtered, x='Metric', y='Score', hue='Model')
        plt.title("Model Performance Comparison")
        plt.tight_layout()
        return plt.gcf()

    @output
    @render.plot
    def training_plot():
        plt.figure(figsize=(8, 5))
        sns.barplot(data=results_df, x='Model', y='Training Time (Mean)')
        plt.title("Model Training Time (Mean)")
        plt.tight_layout()
        return plt.gcf()

# App
app = App(app_ui, server)
run_app(app)

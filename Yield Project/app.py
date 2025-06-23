import ann_dashboard as ann_db
import bond_dashboard as bond_db
import yield_dashboard as yield_db

import pandas as pd
import numpy as np


from shiny import App, render, ui

# Define the UI
app_ui = ui.page_fluid(
    ui.input_slider("num", "Choose a number:", min=1, max=100, value=50),
    ui.output_text_verbatim("result")
)

# Define the server logic
def server(input, output, session):
    @output
    @render.text
    def result():
        return f"You selected: {input.num()}"

# Create the app
app = App(app_ui, server)
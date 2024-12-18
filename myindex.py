from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# import from folders
from app import *
from components import sidebar, dashboards
from globals import *

# Carregar dados da planilha e armazená-los
df_ordens = pd.read_excel("ordem_de_compra.xlsx")
df_ordens_aux = df_ordens.to_dict()

# Layout
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-ordens', data=df_ordens_aux),
    
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

import dash_bootstrap_components as dbc
from dash import dcc
from dash import html



def create_layout():
    return dbc.Container([
        dbc.NavbarSimple(
            brand="Состояние воздуха 🌪️",
            brand_href="#",
            color="primary",
            dark=True,
            className="mb-4 flex justify-content-between",
        ),
        dbc.Row([
            dbc.Col(dbc.Card(id='weather-output', body=True), width=6, xs=12, md=6),
            dbc.Col([
                dbc.Input(id='city-input', value='London', type='text', placeholder="Введите город", debounce=True),
            ], width=6, xs=12, md=6),
            ], className="mb-3"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='co-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='no2-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='o3-graph'), width=4, xs=12, md=4),
        
        ], className="mb-3"),


        dbc.Row([
            dbc.Col(dcc.Graph(id='so2-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='pm2_5-graph'), width=4, xs=12, md=4),
            dbc.Col(dcc.Graph(id='pm_10-graph'), width=4, xs=12, md=4),
        ], className="mb-3"),

        
    ], fluid=True)


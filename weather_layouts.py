import dash_bootstrap_components as dbc
from dash import dcc
from dash import html




def create_layout():
    return dbc.Container(
        fluid=True,
        style={
            'backgroundColor': '#121212',
            'color': 'white',
            'padding': '20px',
            'minHeight': '100vh'
        },
        children=[
            dbc.NavbarSimple(
                brand="Почасовой прогноз загрязнения воздуха 🌪️",
                brand_href="#",
                color="dark",
                dark=True,
                sticky="top",
                className="mb-4 shadow",
            ),
            
            
            html.Div([
                dbc.Row([
                    dbc.Col(
                        dbc.InputGroup([
                            dbc.InputGroupText("Город"),
                            dbc.Input(
                                id='city-input',
                                value='Санкт-Петербург',
                                placeholder="Введите город...",
                                debounce=True,
                                style={'backgroundColor': '#2a2a2a', 'color': 'white', 'border': '1px solid #444'}
                            ),
                        ]),
                        width=12, lg=6, className="mb-3"
                    ),
                    
                    
                    dbc.Col(
                        dbc.Card(
                            id='weather-output',
                            style={
                                'backgroundColor': '#1e1e1e',
                                'border': '1px solid #444',
                                'borderRadius': '15px'
                            }
                        ),
                        width=12, lg=6, className="mb-3"
                    ),
                ], className="mb-4"),
                
                
                dbc.Row([
                    dbc.Col(dcc.Graph(id='co-graph'), width=4, className="mb-3"), 
                    dbc.Col(dcc.Graph(id='no2-graph'), width=4, className="mb-3"),
                    dbc.Col(dcc.Graph(id='o3-graph'), width=4, className="mb-3"),
                ], className="mb-4"),
                
               
                dbc.Row([
                    dbc.Col(dcc.Graph(id='so2-graph'), width=4, className="mb-3"),
                    dbc.Col(dcc.Graph(id='pm2_5-graph'), width=4, className="mb-3"),
                    dbc.Col(dcc.Graph(id='pm_10-graph'), width=4, className="mb-3"),
                ], className="mb-4"),
                
                
            ])
        ]
    )
from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go
import dash_bootstrap_components as dbc



def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm2_5-graph', 'figure'),
        Output('pm_10-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
        
        
        weather_card = dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H4(f"{data['city_name']}", className="card-title mb-3 text-center", style={"color": "white"}),
                    html.Img(
                        src=f"https:{data['icon']}", 
                        style={"height": "64px", "display": "block", "margin": "0 auto"},
                        className="mb-3"
                    ),
                    html.H2(f"{data['temp']}°C", className="card-title text-center mb-4", style={"color": "white"}),
                    
                    dbc.Row([
                        dbc.Col(create_pollution_item(data, 'co_now', 'Угарный газ', 'мг/м³', '#FF5733')),
                        dbc.Col(create_pollution_item(data, 'no2_now', 'Диоксид азота', 'мкг/м³', '#33A1FF')),
                        dbc.Col(create_pollution_item(data, 'o3_now', 'Озон', 'мкг/м³', '#33FF57')),
                    ], className="mb-3"),
                    
                    dbc.Row([
                        dbc.Col(create_pollution_item(data, 'so2_now', 'Диоксид серы', 'мкг/м³', '#FF33A1')),
                        dbc.Col(create_pollution_item(data, 'pm2_5_now', 'Мелкие частицы', 'мкг/м³', '#8E33FF')),
                        dbc.Col(create_pollution_item(data, 'pm10_now', 'Крупные частицы', 'мкг/м³', '#33FFF5')),
                    ]),
                    
                    html.P(data['condition'], className="card-text text-center mt-3", style={"color": "white"}),
                ])
            ]),
            className="mb-4 shadow",
            style={
                "borderRadius": "15px",
                "backgroundColor": "#1e1e1e",
                "border": "1px solid #444"
            }
        )
        
       
        co_fig = create_pollution_figure(data, 'co', 'Концентрация угарного газа(CO)', 'мг/м³', '#FF5733', 5)
        no2_fig = create_pollution_figure(data, 'no2', 'Концентрация диоксида азота (NO₂)', 'мкг/м³', '#33A1FF', 40)
        o3_fig = create_pollution_figure(data, 'o3', 'Концентрация озона (O₃)', 'мкг/м³', '#33FF57', 30)
        so2_fig = create_pollution_figure(data, 'so2', 'Концентрация диоксида серы (SO₂)', 'мкг/м³', '#FF33A1', 5)
        pm2_5_fig = create_pollution_figure(data, 'pm2_5', 'Концентрация мелких частиц (PM2.5)', 'мкг/м³', '#8E33FF', 25)
        pm10_fig = create_pollution_figure(data, 'pm10', 'Концентрация крупных частиц (PM10)', 'мкг/м³', '#33FFF5', 50)
        
        return weather_card, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig

def create_pollution_item(data, key, name, unit, color):
    value = data.get(key, 0)
    return html.Div([
        html.Small(f"{name} ({unit})", className="text-muted d-block text-center"),
        html.H5(f"{value}", 
               className="mb-0 text-center",
               style={"color": color, "fontWeight": "bold"})
    ], className="p-2")

def create_pollution_figure(data, pollutant, title, unit, color, threshold=None):
    fig = go.Figure(
        data=[go.Scatter(
            x=data['hours'],
            y=data[pollutant],
            mode='lines+markers',
            name=title,
            line=dict(width=3, color=color),
            marker=dict(size=8, color=color),
            hovertemplate='<b>%{x}</b><br>%{y:.2f} '+unit+'<extra></extra>'
        )],
        layout=go.Layout(
            title=dict(text=title, x=0.5, xanchor='center'),
            xaxis_title='Время',
            yaxis_title=f'Концентрация ({unit})',
            template='plotly_dark',
            hovermode="x unified",
            margin=dict(l=50, r=50, t=80, b=50),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Arial, sans-serif")
        )
    )
    
      
    
    fig.update_traces(
        line_shape='spline',
        marker_line_width=0.5,
        marker_line_color='white'
    )
    
    return fig
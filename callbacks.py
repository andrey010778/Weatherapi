from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go


def register_callbacks(app):
    @app.callback(
        Output('weather-output', 'children'),
        Output('temp-graph', 'figure'),
        Output('ap-graph', 'figure'),
        Output('wind-dir-graph', 'figure'),
        Input('city-input', 'value')
    )
    def update_dashboard(city):
        data = load_data(city)
    
        weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text")
        ])

        temp_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['temps'], mode='lines+markers', name='Температура')],
           layout=go.Layout(title='Температура по часам', xaxis_title='Время', yaxis_title='Температура (°C)', template='plotly_dark') 
        )

        ap_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['ap'], mode='lines+markers', name='Атмосферное давление')],
           layout=go.Layout(title='Атмосферное давление по часам', xaxis_title='Время', yaxis_title='pa', template='plotly_dark') 
        )

        wind_dir_fig = go.Figure(
            data=go.Scatterpolar(
                r=data['wind'],
                theta=data['wind_dirs'],
                mode='lines+markers',
                name='Ветер'
            )
        )

        wind_dir_fig.update_layout(
            title='Направление и скорость ветра',
            template='plotly_dark',
            polar=dict(
                angularaxis=dict(
                    direction="clockwise",
                    tickmode="array",
                    rotation=90,
                    tickvals=[0, 45, 90, 135, 180, 225, 270, 315],
                    ticktext=["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
                ),
            
            radialaxis=dict(
                title="Скорость ветра (км/ч)"
                )
            )
        )
        

        return weather_info, temp_fig, ap_fig, wind_dir_fig
from dash import Input, Output, html, dcc
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
    
        weather_info = html.Div([
            html.H4(f"{data['city_name']}", className="card-title"),
            html.Img(src=f"https:{data['icon']}", style={"height": "64px"}),
            html.H5(f"{data['temp']}°C", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация CO: {data ['co_now']}(мг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация NO₂: {data ['no2_now']}(мкг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация O₃: {data ['o3_now']}(мкг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация SO₂: {data ['so2_now']}(мкг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация PM2.5: {data ['pm2_5_now']}(мкг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"Концентрация PM10: {data ['pm10_now']}(мкг/м³) ", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text"),
            
        ])

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='CO')],
           layout=go.Layout(title='Концентрация угарного газа (CO)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='NO2')],
           layout=go.Layout(title='Концентрация диоксида азота (NO₂)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='O3')],
           layout=go.Layout(title='Концентрация озона (O₃)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='SO2')],
           layout=go.Layout(title='Концентрация диоксида серы (SO₂)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='PM2_5')],
           layout=go.Layout(title='Концентрация мелких частиц (PM2.5)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='PM10')],
           layout=go.Layout(title='Концентрация крупных частиц (PM10)', xaxis_title='Время', yaxis_title='(мг/м³)', template='plotly_dark') 
        )

        
        return weather_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig 



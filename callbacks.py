from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go

 
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
            html.H5(f"CO: {data ['co_now']} ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"NO2: {data ['no2_now']} ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"O3: {data ['o3_now']} ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"SO2: {data ['so2_now']} ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"PM2_5: {data ['pm2_5_now']} ", className="card-subtitle mb-2 text-muted"),
            html.H5(f"PM10: {data ['pm10_now']} ", className="card-subtitle mb-2 text-muted"),
            html.P(data['condition'], className="card-text"),
            
        ])

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='CO')],
           layout=go.Layout(title='CO по часам', xaxis_title='Время', yaxis_title='CO', template='plotly_dark') 
        )

        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='NO2')],
           layout=go.Layout(title='NO2 по часам', xaxis_title='Время', yaxis_title='NO2', template='plotly_dark') 
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='O3')],
           layout=go.Layout(title='O3 по часам', xaxis_title='Время', yaxis_title='O3', template='plotly_dark') 
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='SO2')],
           layout=go.Layout(title='SO2 по часам', xaxis_title='Время', yaxis_title='SO2', template='plotly_dark') 
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='PM2_5')],
           layout=go.Layout(title='PM2_5 по часам', xaxis_title='Время', yaxis_title='PM2_5', template='plotly_dark') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='PM10')],
           layout=go.Layout(title='PM10 по часам', xaxis_title='Время', yaxis_title='PM10', template='plotly_dark') 
        )

        
        return weather_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig 
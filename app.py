from dash import Dash
from weather_layouts import create_layout
from callbacks import register_callbacks
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.LUX])
app.title = "Состояние воздуха"
server = app.server #  добавляем для деплоя

app.layout = create_layout()

register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True) # При продакшене используем False вместо True
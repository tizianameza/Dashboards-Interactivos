# Autor: Tiziana Meza
# Fecha: Feb-2024
# Descripción:Dashboards interactivos utilizando herramientas como Plotly y Dash visualizaciones dinámicas de datos relevantes para un negocio o sector específico, facilitando la comprensión y toma de decisiones.
# Versión de Python: 3.6

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Cargar datos de ventas
data = pd.read_csv("datos_ventas.csv")

# Crear aplicación Dash
app = dash.Dash(__name__)

# Definir el layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard Interactivo de Ventas"),

    dcc.Dropdown(
        id='dropdown-producto',
        options=[{'label': prod, 'value': prod} for prod in data['Producto'].unique()],
        value=data['Producto'].unique()[0]
    ),

    dcc.Graph(id='graph-ventas')
])

# Callback para actualizar el gráfico según el producto seleccionado
@app.callback(
    dash.dependencies.Output('graph-ventas', 'figure'),
    [dash.dependencies.Input('dropdown-producto', 'value')]
)
def update_graph(selected_product):
    filtered_data = data[data['Producto'] == selected_product]
    fig = px.line(filtered_data, x='Mes', y='Ventas', title=f'Ventas de {selected_product} por Mes')
    return fig

# Ejecutar la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)

import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from .plots import create_plot

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('My Interactive Plots Dashboard'),
    dcc.Input(
        id='data-source-input', 
        type='text', 
        value='data/iris.csv', 
        placeholder='Enter data source path'
    ),
    dcc.Dropdown(
        id='plot-type-dropdown',
        options=[
            {'label': 'Scatter Plot', 'value': 'scatter'},
            {'label': 'Line Plot', 'value': 'line'},
            {'label': 'Histogram', 'value': 'histogram'},
            {'label': 'Box Plot', 'value': 'box'},
            {'label': '3D Scatter Plot', 'value': '3d_scatter'},
            {'label': 'Geographical Map', 'value': 'geo_map'}
        ],
        value='scatter',
        clearable=False
    ),
    dcc.Graph(id='interactive-plot'),
])

@app.callback(
    Output('interactive-plot', 'figure'),
    [Input('plot-type-dropdown', 'value'),
     Input('data-source-input', 'value')]
)
def update_graph(plot_type, data_source):
    fig = create_plot(data_source, plot_type)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

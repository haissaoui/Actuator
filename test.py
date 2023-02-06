


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Bananas", "Cherries", "Dates"],
    "Count": [30, 40, 20, 10]
})

app.layout = html.Div([
    dcc.Graph(
        figure=px.bar(df, x="Fruit", y="Count")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)


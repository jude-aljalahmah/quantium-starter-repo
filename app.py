import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# load data
df = pd.read_csv("output.csv")

# convert date column
df["date"] = pd.to_datetime(df["date"])

# sort by date
df = df.sort_values("date")

# group by date (sum sales per day)
df = df.groupby("date")["sales"].sum().reset_index()

# create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# create app
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Soul Foods Sales Visualiser"),  # header

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# run server
if __name__ == "__main__":
    app.run(debug=True)
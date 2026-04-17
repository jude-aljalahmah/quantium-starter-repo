import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# load data
df = pd.read_csv("output.csv")

# convert and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# make sure region is consistent (optional safety)
df["region"] = df["region"].str.lower()

app = Dash(__name__)

# layout
app.layout = html.Div(style={
    "fontFamily": "Arial",
    "padding": "20px",
    "backgroundColor": "#f5f5f5"
}, children=[

    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center", "color": "#333"}
    ),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        )
    ]),

    dcc.Graph(id="sales-chart")
])


# callback for filtering
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    grouped = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        grouped,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales ({selected_region.title()})"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)

app = Dash(__name__)
server = app.server
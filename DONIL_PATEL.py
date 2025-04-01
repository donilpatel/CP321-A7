import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

#list of dictionaries
world_cup_data = [
    {"Year": 2018, "Winner": "France", "Runner-Up": "Croatia"},
    {"Year": 2014, "Winner": "Germany", "Runner-Up": "Argentina"},
    {"Year": 2010, "Winner": "Spain", "Runner-Up": "Netherlands"},
    {"Year": 2006, "Winner": "Italy", "Runner-Up": "France"},
    {"Year": 2002, "Winner": "Brazil", "Runner-Up": "Germany"},
    {"Year": 1998, "Winner": "France", "Runner-Up": "Brazil"},
    {"Year": 1994, "Winner": "Brazil", "Runner-Up": "Italy"},
    {"Year": 1990, "Winner": "Germany", "Runner-Up": "Argentina"},
    {"Year": 1986, "Winner": "Argentina", "Runner-Up": "Germany"},
    {"Year": 1982, "Winner": "Italy", "Runner-Up": "Germany"},
    {"Year": 1978, "Winner": "Argentina", "Runner-Up": "Netherlands"},
    {"Year": 1974, "Winner": "Germany", "Runner-Up": "Netherlands"},
    {"Year": 1970, "Winner": "Brazil", "Runner-Up": "Italy"},
    {"Year": 1966, "Winner": "England", "Runner-Up": "Germany"},
    {"Year": 1962, "Winner": "Brazil", "Runner-Up": "Czechoslovakia"},
    {"Year": 1958, "Winner": "Brazil", "Runner-Up": "Sweden"},
    {"Year": 1954, "Winner": "Germany", "Runner-Up": "Hungary"},
    {"Year": 1950, "Winner": "Uruguay", "Runner-Up": "Brazil"},
    {"Year": 1938, "Winner": "Italy", "Runner-Up": "Hungary"},
    {"Year": 1934, "Winner": "Italy", "Runner-Up": "Czechoslovakia"},
    {"Year": 1930, "Winner": "Uruguay", "Runner-Up": "Argentina"}
]

for row in world_cup_data:
    if row["Winner"] in ["West Germany"]:
        row["Winner"] = "Germany"
    if row["Runner-Up"] in ["West Germany"]:
        row["Runner-Up"] = "Germany"

df = pd.DataFrame(world_cup_data)

win_counts = df["Winner"].value_counts().reset_index()
win_counts.columns = ["Country", "Wins"]

country_iso_map = {
    "Brazil": "BRA",
    "Germany": "DEU",
    "Italy": "ITA",
    "Argentina": "ARG",
    "France": "FRA",
    "Uruguay": "URY",
    "England": "GBR",
    "Spain": "ESP",
    "Netherlands": "NLD",
    "Croatia": "HRV",
    "Sweden": "SWE",
    "Hungary": "HUN",
    "Czechoslovakia": "CZE"
}
win_counts["ISO_Code"] = win_counts["Country"].map(country_iso_map)

app = Dash(__name__)
server = app.server

app.title = "FIFA World Cup Dashboard"


# layout of the dashboard

app.layout = html.Div([
    html.H1("FIFA World Cup Winners Dashboard", style={"textAlign": "center"}),

    dcc.Graph(id="choropleth-map"),

    html.Label("Select a Country:", style={"marginTop": "20px"}),
    dcc.Dropdown(
        options=[{"label": country, "value": country} for country in sorted(win_counts["Country"])],
        id="country-dropdown",
        placeholder="Select a country"
    ),
    html.Div(id="country-output", style={"marginTop": "10px", "fontWeight": "bold"}),

    html.Label("Select a Year:", style={"marginTop": "20px"}),
    dcc.Dropdown(
        options=[{"label": year, "value": year} for year in sorted(df["Year"], reverse=True)],
        id="year-dropdown",
        placeholder="Select a year"
    ),
    html.Div(id="year-output", style={"marginTop": "10px", "fontWeight": "bold"})
])

@app.callback(
    Output("choropleth-map", "figure"),
    Input("country-dropdown", "value")
)
def update_map(selected_country):
    fig = px.choropleth(
        win_counts,
        locations="ISO_Code",
        color="Wins",
        hover_name="Country",
        color_continuous_scale="Oranges",
        title="World Cup Wins by Country"
    )
    fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
    return fig

@app.callback(
    Output("country-output", "children"),
    Input("country-dropdown", "value")
)
def display_country_wins(country):
    if not country:
        return ""
    wins = win_counts.loc[win_counts["Country"] == country, "Wins"].values[0]
    return f"{country} has won the FIFA World Cup {wins} time(s)."

@app.callback(
    Output("year-output", "children"),
    Input("year-dropdown", "value")
)
def display_year_results(year):
    if not year:
        return ""
    row = df[df["Year"] == year].iloc[0]
    return f"In {year}, the Winner was {row['Winner']} and the Runner-Up was {row['Runner-Up']}."

if __name__ == "__main__":
    app.run(debug=True)

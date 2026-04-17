import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app():
    return import_app("app")


def test_header(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert "Soul Foods Sales Visualiser" in header.text


def test_graph_exists(dash_duo, app):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_exists(dash_duo, app):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
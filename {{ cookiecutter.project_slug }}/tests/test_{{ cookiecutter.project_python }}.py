import pytest
import responses
from click.testing import CliRunner

from cli import cli
from {{ cookiecutter.project_python }}.{{ cookiecutter.project_python }} import (
    {{ cookiecutter.project_python }},
)


@pytest.fixture(scope="function")
def cli_runner():
    return CliRunner()


@pytest.mark.usefixtures("cli_runner")
def test_cli_with_no_parameter(cli_runner):
    actual = cli_runner.invoke(cli, [])
    assert actual.exit_code == 2
    assert "Usage: cli [OPTIONS]" in actual.output
    assert "Error: Missing option '--url'." in actual.output


@pytest.mark.usefixtures("cli_runner")
def test_cli_with_all_parameters(cli_runner, caplog):
    actual = cli_runner.invoke(cli, ["--url=https://example.com"])
    assert "Response: " in caplog.text
    assert actual.exit_code == 0


@responses.activate
def test_request_call():
    responses.get(
        "https://example.com",
        status=200,
    )
    actual = {{ cookiecutter.project_python }}("https://example.com")

    assert actual.request.method == "GET"
    assert actual.status_code == 200

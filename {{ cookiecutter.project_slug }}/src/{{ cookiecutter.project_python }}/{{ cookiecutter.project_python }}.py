import requests
from loguru import logger


def {{ cookiecutter.project_python }}(
    url,
):
    """
    Calls a given URL and prints the response status code
    """
    r = requests.get(url)
    logger.info(f"Response: {r.status_code}")
    return r

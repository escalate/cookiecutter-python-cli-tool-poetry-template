import os

REMOVE_PATHS = [
    '{% if cookiecutter.project_license != "MIT" %}LICENSE{% endif %}'
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

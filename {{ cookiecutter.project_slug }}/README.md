# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Local usage

Usage is possible via an interactive Docker container in VSCode.

1. Build and launch the DevContainer in VSCode.

2. Initiate the Python Virtual Environment via `poetry env activate` in the terminal.

3. Run `./src/cli.py --help`

```
Usage: cli.py [OPTIONS]

  {{ cookiecutter.project_name }}

Options:
  --url TEXT  URL, e.g. https://example.com  [required]
  --help      Show this message and exit.
```

## License

{{ cookiecutter.project_license }}

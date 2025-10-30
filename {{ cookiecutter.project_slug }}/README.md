[![Test](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml)

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## 📚 Usage

1. Build the Docker image.

```
$ make build-docker-image
```

2. Run Docker container from built image to print help.

```
$ make run-docker-image

Usage: cli.py [OPTIONS]

  {{ cookiecutter.project_name }}

Options:
  --url TEXT  URL, e.g. https://example.com  [required]
  --help      Show this message and exit.
```

## 🤝 Contributing

We welcome contributions of all kinds 🎉.

Please read our [Contributing](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/blob/master/CONTRIBUTING.md) guide to learn how to get started, submit changes, and follow our contribution standards.

## 🌐 Code of Conduct

This project follows a [Code of Conduct](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/blob/master/CODE_OF_CONDUCT.md) to ensure a welcoming and respectful community.

By participating, you agree to uphold this standard.

## 🐛 Issues

Found a bug or want to request a feature?

Open an issue here: [GitHub Issues](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/issues)

## 🧪 Development

Development is possible via an interactive Docker container in [VSCode](https://code.visualstudio.com/).

1. Build and launch the [DevContainer](https://code.visualstudio.com/docs/devcontainers/containers) in VSCode.

2. Initiate the Python Virtual Environment via `poetry env activate` in the terminal.

3. Run test suite via `pytest` in the terminal.

## 📜 License

This project is licensed under the **{{ cookiecutter.project_license }} License**.

See the [LICENSE](https://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.project_slug }}/blob/master/LICENSE) file for details.

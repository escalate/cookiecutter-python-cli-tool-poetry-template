SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c

.PHONY: test
test: clean
	cookiecutter . \
	--output-dir=test/ \
	--replay \
	--replay-file cookiecutter-python-cli-tool-poetry-template.json \
	--keep-project-on-failure \
	--verbose

.PHONY: clean
clean:
	rm --recursive --force test/

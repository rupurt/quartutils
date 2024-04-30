all: setup test

setup: deps.install

deps.install: deps.install.pyproject
deps.install.pyproject: deps.install.pyproject/global deps.install.pyproject/test
deps.install.pyproject/global:
	./scripts/deps/install_pyproject
deps.install.pyproject/test:
	./scripts/deps/install_pyproject test
deps.install.requirements: deps.install.requirements/global deps.install.requirements/test
deps.install.requirements/global:
	./scripts/deps/install_requirements
deps.install.requirements/test:
	./scripts/deps/install_requirements test
deps.compile: deps.compile/global deps.compile/test
deps.compile/global:
	./scripts/deps/compile
deps.compile/test:
	./scripts/deps/compile test
deps.clean:
	./scripts/deps/clean
deps.purge:
	./scripts/deps/purge

format/run:
	./scripts/format/run
format/check:
	./scripts/format/check

test: test/lint test/typecheck test/run test/coverage
test/lint:
	./scripts/test/lint
test/typecheck:
	./scripts/test/typecheck
test/run:
	./scripts/test/run
test/watch:
	./scripts/test/watch
test/nocapture:
	./scripts/test/nocapture
test/coverage:
	./scripts/test/coverage

pypi: pypi/build pypi/publish
pypi/build:
	./scripts/pypi/build
pypi/publish:
	./scripts/pypi/publish



.PHONY: help setup firmware flash software app pipeline test lint format clean

help: 
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

setup: 
	python -m venv .venv
	. .venv/bin/activate && pip install -e "software[dev]" && pre-commit install

firmware: 
	$(MAKE) -C firmware build

flash: 
	$(MAKE) -C firmware flash

software: 
	. .venv/bin/activate && pip install -e "software[dev]"

app:
	$(MAKE) -C app dev

pipeline: 
	$(MAKE) -C datapipeline run

test: 
	$(MAKE) -C firmware test
	. .venv/bin/activate && pytest software datapipeline app/backend

lint: 
	. .venv/bin/activate && ruff check software datapipeline app

format: 
	. .venv/bin/activate && ruff format software datapipeline app

clean: 
	$(MAKE) -C firmware clean
	find . -type d -name __pycache__ -prune -exec rm -rf {} +

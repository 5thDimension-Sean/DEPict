.PHONY: build flash monitor test clean

build:   ## Compile firmware
	pio run

flash:   ## Build and upload to board
	pio run -t upload

monitor: ## Open serial monitor
	pio device monitor

test:    ## Run native unit tests
	pio test -e native

clean:
	pio run -t clean
	rm -rf .pio

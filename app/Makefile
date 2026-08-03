.PHONY: dev backend frontend install

install: ## Install backend + frontend deps
	pip install -r backend/requirements.txt
	cd frontend && npm install

backend: ## Run the FastAPI backend
	uvicorn app.backend.main:app --reload --port 8000

frontend: ## Run the Vite dev server
	cd frontend && npm run dev

dev: ## Run backend and frontend together
	$(MAKE) -j2 backend frontend

"""FastAPI application factory + entry point.

Run:  uvicorn app.backend.main:app --reload
"""

from __future__ import annotations


def create_app():
    try:
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
    except ImportError:  # pragma: no cover
        raise SystemExit("Install backend deps: pip install fastapi uvicorn")

    from .api import assays, health

    app = FastAPI(title="DEPict", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # frontend dev server
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(health.router)
    app.include_router(assays.router)
    return app


app = create_app()

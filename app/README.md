# DEPict Companion App

A local web app to drive the sensor, watch live results, browse past runs, and label
data.

```
app/
  backend/    # FastAPI service: talks to the device, stores runs, serves the API
    api/      # HTTP routes
    services/ # device control, run storage
    models/   # request/response schemas (reuse depict.common where possible)
  frontend/   # Vite + web UI (dashboard, live assay, run history)
  tests/      # backend tests
```

## Dev

```bash
make dev        # runs backend (uvicorn) + frontend (vite) together
make backend    # backend only  → http://localhost:8000
make frontend   # frontend only → http://localhost:5173
```

The frontend talks to the backend REST API; the backend uses
`depict.acquisition.Device` to reach the hardware, so install the host package first
(`pip install -e software`).

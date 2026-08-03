# Contributing to DEPict

Thanks for helping build an affordable microplastic sensor! DEPict spans firmware,
hardware, ML, and application code — contributions of any size are welcome.

## Ground rules

- Be respectful. See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- Open an issue before large changes so we can align on approach.
- Keep PRs focused; one logical change per PR.
- Never commit real sample data, credentials, or large binaries. Use `data/` (git-ignored)
  and link datasets in `docs/`.

## Development setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e "software[dev]"
pre-commit install         # runs ruff + formatting on commit
```

For firmware you'll need [PlatformIO](https://platformio.org/); for hardware,
[KiCad 8+](https://www.kicad.org/).

## Conventions

- **Python**: `ruff` for lint + format, type hints encouraged, `pytest` for tests.
- **C/C++ firmware**: `clang-format` (LLVM style), keep ISR/real-time paths allocation-free.
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat:`, `fix:`, `docs:`, `hw:`, `fw:`, …).
- **Branches**: `feature/…`, `fix/…`, `hw/…`.

## Testing

```bash
make test        # runs firmware unit tests + python tests + pipeline tests
```

## Areas that need help

- EIS driver calibration and phase correction.
- DEP electrode geometry simulation (`hardware/simulation/`).
- Labeled datasets for training (`data/` + `datapipeline/`).
- Enclosure design for field deployment.

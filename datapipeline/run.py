from __future__ import annotations

import argparse

from .ingest import ingest
from .preprocess import preprocess
from .features import extract_features
from .fusion import fuse
from .export import export_datasets


def run(config_path: str) -> None:
   
    records = ingest(config_path)
    cleaned = preprocess(records)
    feats = extract_features(cleaned)
    matrix = fuse(feats)
    export_datasets(matrix, config_path)
    print("[scaffold] pipeline stages invoked (stubs).")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="config/pipeline.yaml")
    args = parser.parse_args(argv)
    run(args.config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""`depict-train` — train the fusion model from a prepared dataset."""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="depict-train", description=__doc__)
    parser.add_argument(
        "--dataset", default="software/datasets/train.parquet", help="prepared dataset"
    )
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument(
        "--out", default="software/models/fusion.pt", help="output checkpoint"
    )
    args = parser.parse_args(argv)

    # TODO: load dataset -> DataLoader, build_model(), train loop with early stopping,
    #       save checkpoint + metrics to args.out.
    print(f"[scaffold] would train {args.epochs} epochs on {args.dataset} → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

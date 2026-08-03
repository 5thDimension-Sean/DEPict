"""`depict-infer` — evaluate a trained model and/or export it for the firmware.

Two jobs:
  * evaluate: run the model on a held-out set and print metrics.
  * export:   quantize + emit a C array (model_data.cc) into firmware/src/fusion/.
"""

from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="depict-infer", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    ev = sub.add_parser("evaluate", help="compute metrics on a test set")
    ev.add_argument("--model", default="software/models/fusion.pt")
    ev.add_argument("--dataset", default="software/datasets/test.parquet")

    ex = sub.add_parser("export", help="quantize + export model to firmware")
    ex.add_argument("--model", default="software/models/fusion.pt")
    ex.add_argument(
        "--out", default="firmware/src/fusion/model_data.cc", help="C array output"
    )

    args = parser.parse_args(argv)

    if args.cmd == "evaluate":
        # TODO: load model, run on dataset, print accuracy / confusion matrix.
        print(f"[scaffold] would evaluate {args.model} on {args.dataset}")
    elif args.cmd == "export":
        # TODO: int8-quantize, convert to TFLite-Micro flatbuffer, emit C array.
        print(f"[scaffold] would export {args.model} → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

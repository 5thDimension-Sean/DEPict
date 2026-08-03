from __future__ import annotations

import argparse


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="depict-acquire", description=__doc__)
    parser.add_argument("--port", required=True, help="serial port, e.g. /dev/ttyUSB0")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--count", type=int, default=1, help="number of assays")
    parser.add_argument("--label", default=None, help="ground-truth polymer, if known")
    parser.add_argument(
        "--out", default="data/raw/session.jsonl", help="output JSONL path"
    )
    args = parser.parse_args(argv)

    # TODO: with Device(args.port, args.baud) as dev: loop run_assay(), tag label,
    #       append each AssayRecord.model_dump_json() to args.out.
    print(f"[scaffold] would capture {args.count} assay(s) from {args.port} → {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

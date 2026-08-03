from __future__ import annotations

import json

CMD_ASSAY = "a"  
CMD_PING = "p"
CMD_CALIBRATE = "c"


def encode_command(cmd: str) -> bytes:
    return (cmd + "\n").encode("ascii")


def decode_line(line: bytes) -> dict:

    try:
        return json.loads(line.decode("utf-8").strip())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:  # noqa: B904
        raise ValueError(f"bad device line: {line!r}") from exc

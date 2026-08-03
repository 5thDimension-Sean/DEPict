from __future__ import annotations

from ..common import protocol
from ..common.schemas import AssayRecord


class Device:

    def __init__(self, port: str, baud: int = 115200) -> None:
        self.port = port
        self.baud = baud
        self._serial = None  # placeholder for serial.Serial

    def open(self) -> None:

        raise NotImplementedError("open() not implemented in scaffold")

    def close(self) -> None:
        if self._serial is not None:
            # TODO: self._serial.close()
            self._serial = None

    def run_assay(self) -> AssayRecord:

        raise NotImplementedError("run_assay() not implemented in scaffold")

    def __enter__(self) -> "Device":
        self.open()
        return self

    def __exit__(self, *exc) -> None:
        self.close()

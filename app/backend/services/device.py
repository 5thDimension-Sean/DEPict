"""Bridge to the hardware via the depict host package."""

from __future__ import annotations


def run_assay(port: str) -> dict:
    """Run one assay and return it as a dict.

    Skeleton: real impl uses depict.acquisition.Device(port).run_assay().
    """
    # from depict.acquisition.device import Device
    # with Device(port) as dev:
    #     return dev.run_assay().model_dump()
    raise NotImplementedError("device bridge not implemented in scaffold")

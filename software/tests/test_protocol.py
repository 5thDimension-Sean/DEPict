

import pytest

from depict.common import protocol


def test_encode_command_appends_newline():
    assert protocol.encode_command(protocol.CMD_ASSAY) == b"a\n"


def test_decode_line_parses_json():
    assert protocol.decode_line(b'{"top": 1, "confidence": 0.9}\n') == {
        "top": 1,
        "confidence": 0.9,
    }


def test_decode_line_rejects_garbage():
    with pytest.raises(ValueError):
        protocol.decode_line(b"not json")

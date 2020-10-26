from multibase import ENCODINGS

from multibase_dataclass import supported_encodings


available_encodings = {enc.encoding for enc in ENCODINGS}

def test_if_any_new_encs_were_added():
    new_encs = available_encodings - supported_encodings
    assert len(new_encs) == 0


def test_if_any_encs_were_dropped():
    dropped_encs = supported_encodings - available_encodings
    assert len(dropped_encs) == 0

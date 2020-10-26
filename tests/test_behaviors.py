import pytest

from multibase_dataclass import Multibase


TEXT: str = "This is foo. Bar!"


def get_fresh_instance():
    return Multibase.encode(encoding="base58btc", data=TEXT)


def test_multibase_to_bytes():
    mb = get_fresh_instance()
    assert isinstance(mb.decode(), bytes)


def test_text_decoding_correctly():
    mb = get_fresh_instance()
    assert mb.decode() == bytes(TEXT, "utf-8")


def test_raise_on_none_data():
    with pytest.raises(ValueError):
        mb = Multibase()

from dataclasses import dataclass, field
from typing import Optional, Union

from multibase import decode, encode as encode_to_bytes, get_codec

from .types import Encoding


@dataclass(repr=True, eq=True, frozen=True)
class Multibase:
    data: Union[bytes, str]
    encoding: Optional[Encoding] = field(
        default=None, hash=False, compare=False
    )

    def __post_init__(self):
        if self.encoding is None:
            try:
                self.encoding = get_codec(self.data)
                pass
            except ValueError:
                msg = "Could not determine encoding for provided data.\n"
                if len(self.data) > 0:
                    msg += f"First byte was: {self.data[0]}"
                raise ValueError(msg)
        try:
            codec = get_codec(self.data).encoding
            if codec != self.encoding:
                msg = f"Data provided has been encoded with {codec!r},"
                msg += f"instead of {self.encoding!r}"
                raise ValueError(msg)
        except ValueError:
            raise

    def decode(self) -> bytes:
        return decode(self.data)

    def reencode(self, encoding: Encoding) -> "Multibase":
        return Multibase.encode(encoding=encoding, data=self.data)

    @classmethod
    def encode(cls, data: bytes, encoding: Encoding = None) -> "Multibase":
        """
        Instatiate a Multibase dataclass and return it.
        """
        encoded_data: bytes = encode_to_bytes(encoding=encoding, data=data)
        return cls(encoding=encoding, data=encoded_data)


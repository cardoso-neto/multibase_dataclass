# multibase_dataclass

A encoding/decoding helper for all the most used encodings.

The `Multibase` class is:
- hashable (you can use it as keys of a Dict)
- immutable (a new object is created everytime you call `.reencode(some_encoding)`)
- representable (it has a cute little `__repr__()`)
- serializable (JSON, coming soon)

Multibase instances also have an `encoding` attribute, which makes it easy to tell what you're dealing with, instead of just juggling bytes-type vars around.

And [here](src/multibase_dataclass/__init__.py) is a full list of the currently supported encodings.

## Install

`pip install git+https://github.com/cardoso-neto/multibase_dataclass.git@master`

## Usage

```python
from multibase_dataclass import Multibase


foo = "We'll win!"
bar = Multibase.encode(encoding="base58btc", data=foo)
print(bar)
# Multibase(encoding='base58btc', data=b'z5unJHbqF5pyTSY')
print(bar.decode())
# b"We'll win!"
print(bar.reencode("base64"))
# Multibase(encoding='base64', data=b'mejV1bkpIYnFGNXB5VFNZ')
print(bar.reencode("base16"))
# Multibase(encoding='base16', data=b'f7a35756e4a48627146357079545359')
```

## Acknowledgements

This is technically a python [dataclass](https://docs.python.org/3/library/dataclasses.html) wrapper for [multiformats/py-multibase](https://github.com/multiformats/py-multibase) which is the official python implementation of the [multiformats/multibase](https://github.com/multiformats/multibase) protocol.


## Contributing

`git clone git@github.com:cardoso-neto/multibase_dataclass.git`

`pip install -e ./multibase_dataclass/`

Work on it and run tests with `pytest -v` after running `pip install -r requirements-test.txt`.
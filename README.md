# multibase_dataclass

A python dataclass wrapper for [multiformats/py-multibase](https://github.com/multiformats/py-multibase) which is the official python implementation of the [multiformats/multibase](https://github.com/multiformats/multibase) protocol.

This makes it easier to tell what you're dealing with, instead of just juggling bytes-type vars around.

[Here](src/multibase_dataclass/__init__.py)'s a full list of the current supported encodings.

## Install

`git clone git@github.com:cardoso-neto/multibase_dataclass.git`

`pip install -e ./multibase_dataclass/`

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
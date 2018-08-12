# Encoding Tools

[![pipeline status](https://gitlab.kozlek.net/open-source/encoding_tools/badges/dev/pipeline.svg)](https://gitlab.seelk.io/seelk/mr-satan/commits/dev)
[![coverage report](https://gitlab.kozlek.net/open-source/encoding_tools/badges/dev/coverage.svg)](https://gitlab.seelk.io/seelk/mr-satan/commits/dev)
[![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%2C%203.7-blue.svg)](https://docs.python.org/3/whatsnew/3.7.html)


This module aims to provide a wrapper to deal with encoding in Python.

## Features
### Encode str to bytes

```python
from encoding_tools import TheSoCalledGreatEncoder

encoder = TheSoCalledGreatEncoder()
encoder.load_str('hellò')
encoder.encode('latin-1')

encoded_string = encoder.encoded_data
```

Yes, this is a much complicated than a simple `'hellò'.encode('latin-1')`, but it deals with encoding errors.
By default, it will fallback to ASCII if an error is encountered.

```python
from encoding_tools import TheSoCalledGreatEncoder

encoder = TheSoCalledGreatEncoder()
encoder.load_str('cœur')  # œ is not supported by latin-1
encoder.encode('latin-1')

encoded_string = encoder.encoded_data  # equals to b'coeur' 
```

If you want to force ASCII conversion, you can do it by specifying `force_ascii=True` when
calling `.encode()`.

### Decode bytes to str

```python
from encoding_tools import TheSoCalledGreatEncoder, GuessEncodingFailedException

encoder = TheSoCalledGreatEncoder()
encoder.load_bytes(b'hell\xf2')
try:
    encoder.decode()
except GuessEncodingFailedException as e:
    # Deal with it
    raise ValueError('Wrong input...') from e

decoded_string = encoder.decoded_data  # equals to 'hellò'
encoding = encoder.encoding  # equals to 'ISO-8859-1'
```

The decoder will guess encoding for you using the great Chardet library. You can as well provide the encoding
if you know when you load the data: `.load_bytes(b'hell\xf2', encoding='latin-1')`

To change data encoding, proceed this way:
```python
from encoding_tools import TheSoCalledGreatEncoder, GuessEncodingFailedException

encoder = TheSoCalledGreatEncoder()
encoder.load_bytes(b'hell\xf2')  # latin-1
try:
    encoder.decode()
except GuessEncodingFailedException as e:
    # Deal with it
    raise ValueError('Wrong input...') from e
    
encoder.encode('utf-8')

encoded_string = encoder.encoded_data  # equals to b'hell\xc3\xb2'
encoding = encoder.encoding  # equals to 'utf-8'
```

## Roadmap
* Deals with decoding errors
* Support more encoding (test suite)

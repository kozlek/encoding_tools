import chardet
from unidecode import unidecode

from .constants import SUPPORTED_ENCODING
from .exceptions import GuessEncodingFailedException


class TheSoCalledGreatEncoder(object):
    """Because when you deal with encoding,
    great is never a good qualifier."""

    def __init__(self):
        self._decoded_data = None
        self._encoded_data = None
        self._encoding = None
        self._has_fallback_to_ascii = None

    @property
    def decoded_data(self):
        if self._decoded_data is None:
            raise AssertionError('You must call `.decode()` before accessing `.decoded_data`.')
        return self._decoded_data

    @property
    def encoded_data(self):
        if self._encoded_data is None:
            raise AssertionError('You must call `.encode()` before accessing `.encoded_data`.')
        return self._encoded_data

    @property
    def encoding(self):
        if self._encoding is None:
            raise AssertionError('You must call `.decode()` before accessing `.encoding`.')
        return self._encoding

    @property
    def has_fallback_to_ascii(self):
        if self._has_fallback_to_ascii is None:
            raise AssertionError('You must call `.encode()` before accessing `.has_fallback_to_ascii`.')
        return self._has_fallback_to_ascii

    @staticmethod
    def _validate_encoding(encoding):
        if encoding not in SUPPORTED_ENCODING:
            raise ValueError("{} is not a supported encoding.".format(encoding))
        return encoding

    @staticmethod
    def _guess_encoding(data):
        """Use python chardet lib to guess encoding."""
        detection = chardet.detect(data)
        encoding = detection.get('encoding')

        if not encoding:
            raise GuessEncodingFailedException
        return encoding

    def load_str(self, data):
        """Load the data from Python 3 Unicode str.
        Parameters
        ----------
        data: str
        """
        self._decoded_data = data
        self._encoding = 'utf-8'

    def load_bytes(self, data, encoding=None):
        """Load the data from bytes.
        Parameters
        ----------
        data: bytes
        encoding: str
        """
        self._encoded_data = data

        if encoding:
            self._encoding = self._validate_encoding(encoding)

    def encode(self, encoding, force_ascii=False, fallback_to_ascii=True):
        """Encode loaded data to encoding. If you enable force_ascii,
        characters will be converted to their ascii equivalent.

        Parameters
        ----------
        encoding: str
        force_ascii: bool
        fallback_to_ascii: bool
        """
        if self._decoded_data is None:
            raise AssertionError('You must call `.load_str()` before calling `.encode`.')
        data = self._decoded_data

        self._has_fallback_to_ascii = False

        if force_ascii:
            data = unidecode(data)
            self._has_fallback_to_ascii = True

        try:
            self._encoded_data = data.encode(encoding)
            self._encoding = encoding
        except UnicodeEncodeError:
            if fallback_to_ascii:
                self._encoded_data = unidecode(data).encode(encoding)
                self._encoding = encoding
                self._has_fallback_to_ascii = True
            else:
                raise

    def decode(self):
        """Decode loaded data to UTF-8."""
        if self._encoded_data is None:
            raise AssertionError('You must call `.load_bytes()` before calling `.decode`.')
        data = self._encoded_data

        if not self._encoding:
            self._encoding = self._guess_encoding(data)

        self._decoded_data = data.decode(self._encoding)

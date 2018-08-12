from unittest.mock import patch

import pytest

from encoding_tools import TheSoCalledGreatEncoder
from encoding_tools import GuessEncodingFailedException


class TestTheSoCalledGreatEncoder:
    def test_load_str(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('hello')

        assert encoder.decoded_data == 'hello'
        assert encoder.encoding == 'utf-8'

    def test_load_bytes(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_bytes(b'hello')

        assert encoder.encoded_data == b'hello'

    def test_load_bytes_with_encoding(self):
        encoding = 'utf-8'

        encoder = TheSoCalledGreatEncoder()
        encoder.load_bytes(b'hello', encoding=encoding)

        assert encoder.encoded_data == b'hello'
        assert encoder.encoding == encoding

    def test_validate_encoding_wrong(self):
        with pytest.raises(ValueError):
            TheSoCalledGreatEncoder._validate_encoding(encoding='test')

    def test_guess_encoding_success(self, fr_hawking, fr_lfs):
        for data, encoding, success in fr_hawking:
            encoder = TheSoCalledGreatEncoder()
            assert (encoder._guess_encoding(data) == encoding) is success

        for data, encoding, success in fr_lfs:
            encoder = TheSoCalledGreatEncoder()
            assert (encoder._guess_encoding(data) == encoding) is success

    @patch('encoding_tools.helpers.chardet.detect', autospec=True)
    def test_guess_encoding_failed(self, mock_detect):
        mock_detect.return_value = {}

        encoder = TheSoCalledGreatEncoder()
        encoder.load_bytes(b'hell\xf2')

        with pytest.raises(GuessEncodingFailedException):
            encoder.decode()

    def test_encode(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('hellò')
        encoder.encode('latin-1')

        assert encoder.encoded_data == b'hell\xf2'
        assert encoder.encoding == 'latin-1'
        assert not encoder.has_fallback_to_ascii

    def test_encode_fallback_to_ascii(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('cœur')
        encoder.encode('latin-1')

        assert encoder.encoded_data == b'coeur'
        assert encoder.encoding == 'latin-1'
        assert encoder.has_fallback_to_ascii

    def test_encode_force_ascii(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('cœur')
        encoder.encode('latin-1', force_ascii=True)

        assert encoder.encoded_data == b'coeur'
        assert encoder.encoding == 'latin-1'
        assert encoder.has_fallback_to_ascii

    def test_encode_disable_ascii_fallback(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('cœur')

        with pytest.raises(UnicodeEncodeError):
            encoder.encode('latin-1', fallback_to_ascii=False)

    def test_encode_without_loading_data(self):
        encoder = TheSoCalledGreatEncoder()

        with pytest.raises(AssertionError):
            encoder.encode('utf-8')

    def test_decode(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_bytes(b'hell\xf2')
        encoder.decode()

        assert encoder.encoding == 'ISO-8859-1'
        assert encoder.decoded_data == 'hellò'

    def test_decode_without_loading_data(self):
        encoder = TheSoCalledGreatEncoder()

        with pytest.raises(AssertionError):
            encoder.decode()

    def test_decoded_data_exception(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_bytes(b'hell\xf2')

        with pytest.raises(AssertionError):
            data = encoder.decoded_data

        with pytest.raises(AssertionError):
            encoding = encoder.encoding

    def test_encoded_data_exception(self):
        encoder = TheSoCalledGreatEncoder()
        encoder.load_str('hello')

        with pytest.raises(AssertionError):
            data = encoder.encoded_data

        with pytest.raises(AssertionError):
            errors = encoder.has_fallback_to_ascii

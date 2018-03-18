"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
import os
import struct


class BindTempAuthKeyRequest(TLObject):
    CONSTRUCTOR_ID = 0xcdd42a05
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, perm_auth_key_id, nonce, expires_at, encrypted_message):
        """
        :param int perm_auth_key_id:
        :param int nonce:
        :param datetime.datetime | None expires_at:
        :param bytes encrypted_message:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message

    def to_dict(self):
        return {
            '_': 'BindTempAuthKeyRequest',
            'perm_auth_key_id': self.perm_auth_key_id,
            'nonce': self.nonce,
            'expires_at': self.expires_at,
            'encrypted_message': self.encrypted_message
        }

    def __bytes__(self):
        return b''.join((
            b'\x05*\xd4\xcd',
            struct.pack('<q', self.perm_auth_key_id),
            struct.pack('<q', self.nonce),
            TLObject.serialize_datetime(self.expires_at),
            TLObject.serialize_bytes(self.encrypted_message),
        ))

    @staticmethod
    def from_reader(reader):
        _perm_auth_key_id = reader.read_long()
        _nonce = reader.read_long()
        _expires_at = reader.tgread_date()
        _encrypted_message = reader.tgread_bytes()
        return BindTempAuthKeyRequest(perm_auth_key_id=_perm_auth_key_id, nonce=_nonce, expires_at=_expires_at, encrypted_message=_encrypted_message)


class CancelCodeRequest(TLObject):
    CONSTRUCTOR_ID = 0x1f040578
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, phone_number, phone_code_hash):
        """
        :param str phone_number:
        :param str phone_code_hash:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'CancelCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def __bytes__(self):
        return b''.join((
            b'x\x05\x04\x1f',
            TLObject.serialize_bytes(self.phone_number),
            TLObject.serialize_bytes(self.phone_code_hash),
        ))

    @staticmethod
    def from_reader(reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return CancelCodeRequest(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class CheckPasswordRequest(TLObject):
    CONSTRUCTOR_ID = 0xa63011e
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, password_hash):
        """
        :param bytes password_hash:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.password_hash = password_hash

    def to_dict(self):
        return {
            '_': 'CheckPasswordRequest',
            'password_hash': self.password_hash
        }

    def __bytes__(self):
        return b''.join((
            b'\x1e\x01c\n',
            TLObject.serialize_bytes(self.password_hash),
        ))

    @staticmethod
    def from_reader(reader):
        _password_hash = reader.tgread_bytes()
        return CheckPasswordRequest(password_hash=_password_hash)


class CheckPhoneRequest(TLObject):
    CONSTRUCTOR_ID = 0x6fe51dfb
    SUBCLASS_OF_ID = 0x99a3d765

    def __init__(self, phone_number):
        """
        :param str phone_number:

        :returns auth.CheckedPhone: Instance of CheckedPhone.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number

    def to_dict(self):
        return {
            '_': 'CheckPhoneRequest',
            'phone_number': self.phone_number
        }

    def __bytes__(self):
        return b''.join((
            b'\xfb\x1d\xe5o',
            TLObject.serialize_bytes(self.phone_number),
        ))

    @staticmethod
    def from_reader(reader):
        _phone_number = reader.tgread_string()
        return CheckPhoneRequest(phone_number=_phone_number)


class DropTempAuthKeysRequest(TLObject):
    CONSTRUCTOR_ID = 0x8e48a188
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, except_auth_keys):
        """
        :param list[int] except_auth_keys:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.except_auth_keys = except_auth_keys

    def to_dict(self):
        return {
            '_': 'DropTempAuthKeysRequest',
            'except_auth_keys': [] if self.except_auth_keys is None else self.except_auth_keys[:]
        }

    def __bytes__(self):
        return b''.join((
            b'\x88\xa1H\x8e',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.except_auth_keys)),b''.join(struct.pack('<q', x) for x in self.except_auth_keys),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _except_auth_keys = []
        for _ in range(reader.read_int()):
            _x = reader.read_long()
            _except_auth_keys.append(_x)

        return DropTempAuthKeysRequest(except_auth_keys=_except_auth_keys)


class ExportAuthorizationRequest(TLObject):
    CONSTRUCTOR_ID = 0xe5bfffcd
    SUBCLASS_OF_ID = 0x5fd1ec51

    def __init__(self, dc_id):
        """
        :param int dc_id:

        :returns auth.ExportedAuthorization: Instance of ExportedAuthorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.dc_id = dc_id

    def to_dict(self):
        return {
            '_': 'ExportAuthorizationRequest',
            'dc_id': self.dc_id
        }

    def __bytes__(self):
        return b''.join((
            b'\xcd\xff\xbf\xe5',
            struct.pack('<i', self.dc_id),
        ))

    @staticmethod
    def from_reader(reader):
        _dc_id = reader.read_int()
        return ExportAuthorizationRequest(dc_id=_dc_id)


class ImportAuthorizationRequest(TLObject):
    CONSTRUCTOR_ID = 0xe3ef9613
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, id, bytes):
        """
        :param int id:
        :param bytes bytes:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id
        self.bytes = bytes

    def to_dict(self):
        return {
            '_': 'ImportAuthorizationRequest',
            'id': self.id,
            'bytes': self.bytes
        }

    def __bytes__(self):
        return b''.join((
            b'\x13\x96\xef\xe3',
            struct.pack('<i', self.id),
            TLObject.serialize_bytes(self.bytes),
        ))

    @staticmethod
    def from_reader(reader):
        _id = reader.read_int()
        _bytes = reader.tgread_bytes()
        return ImportAuthorizationRequest(id=_id, bytes=_bytes)


class ImportBotAuthorizationRequest(TLObject):
    CONSTRUCTOR_ID = 0x67a3ff2c
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, flags, api_id, api_hash, bot_auth_token):
        """
        :param int flags:
        :param int api_id:
        :param str api_hash:
        :param str bot_auth_token:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.flags = flags
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_auth_token = bot_auth_token

    def to_dict(self):
        return {
            '_': 'ImportBotAuthorizationRequest',
            'flags': self.flags,
            'api_id': self.api_id,
            'api_hash': self.api_hash,
            'bot_auth_token': self.bot_auth_token
        }

    def __bytes__(self):
        return b''.join((
            b',\xff\xa3g',
            struct.pack('<i', self.flags),
            struct.pack('<i', self.api_id),
            TLObject.serialize_bytes(self.api_hash),
            TLObject.serialize_bytes(self.bot_auth_token),
        ))

    @staticmethod
    def from_reader(reader):
        _flags = reader.read_int()
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        _bot_auth_token = reader.tgread_string()
        return ImportBotAuthorizationRequest(flags=_flags, api_id=_api_id, api_hash=_api_hash, bot_auth_token=_bot_auth_token)


class LogOutRequest(TLObject):
    CONSTRUCTOR_ID = 0x5717da40
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'LogOutRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'@\xda\x17W',
        ))

    @staticmethod
    def from_reader(reader):
        return LogOutRequest()


class RecoverPasswordRequest(TLObject):
    CONSTRUCTOR_ID = 0x4ea56e92
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, code):
        """
        :param str code:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.code = code

    def to_dict(self):
        return {
            '_': 'RecoverPasswordRequest',
            'code': self.code
        }

    def __bytes__(self):
        return b''.join((
            b'\x92n\xa5N',
            TLObject.serialize_bytes(self.code),
        ))

    @staticmethod
    def from_reader(reader):
        _code = reader.tgread_string()
        return RecoverPasswordRequest(code=_code)


class RequestPasswordRecoveryRequest(TLObject):
    CONSTRUCTOR_ID = 0xd897bc66
    SUBCLASS_OF_ID = 0xfa72d43a

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'RequestPasswordRecoveryRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'f\xbc\x97\xd8',
        ))

    @staticmethod
    def from_reader(reader):
        return RequestPasswordRecoveryRequest()


class ResendCodeRequest(TLObject):
    CONSTRUCTOR_ID = 0x3ef1a9bf
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number, phone_code_hash):
        """
        :param str phone_number:
        :param str phone_code_hash:

        :returns auth.SentCode: Instance of SentCode.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            '_': 'ResendCodeRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash
        }

    def __bytes__(self):
        return b''.join((
            b'\xbf\xa9\xf1>',
            TLObject.serialize_bytes(self.phone_number),
            TLObject.serialize_bytes(self.phone_code_hash),
        ))

    @staticmethod
    def from_reader(reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        return ResendCodeRequest(phone_number=_phone_number, phone_code_hash=_phone_code_hash)


class ResetAuthorizationsRequest(TLObject):
    CONSTRUCTOR_ID = 0x9fab0d1a
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    def to_dict(self):
        return {
            '_': 'ResetAuthorizationsRequest'
        }

    def __bytes__(self):
        return b''.join((
            b'\x1a\r\xab\x9f',
        ))

    @staticmethod
    def from_reader(reader):
        return ResetAuthorizationsRequest()


class SendCodeRequest(TLObject):
    CONSTRUCTOR_ID = 0x86aef0ec
    SUBCLASS_OF_ID = 0x6ce87081

    def __init__(self, phone_number, api_id, api_hash, allow_flashcall=None, current_number=None):
        """
        :param bool | None allow_flashcall:
        :param str phone_number:
        :param Bool | None current_number:
        :param int api_id:
        :param str api_hash:

        :returns auth.SentCode: Instance of SentCode.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.allow_flashcall = allow_flashcall
        self.phone_number = phone_number
        self.current_number = current_number
        self.api_id = api_id
        self.api_hash = api_hash

    def to_dict(self):
        return {
            '_': 'SendCodeRequest',
            'allow_flashcall': self.allow_flashcall,
            'phone_number': self.phone_number,
            'current_number': self.current_number,
            'api_id': self.api_id,
            'api_hash': self.api_hash
        }

    def __bytes__(self):
        assert ((self.allow_flashcall or self.allow_flashcall is not None) and (self.current_number or self.current_number is not None)) or ((self.allow_flashcall is None or self.allow_flashcall is False) and (self.current_number is None or self.current_number is False)), 'allow_flashcall, current_number parameters must all be False-y (like None) or all me True-y'
        return b''.join((
            b'\xec\xf0\xae\x86',
            struct.pack('<I', (0 if self.allow_flashcall is None or self.allow_flashcall is False else 1) | (0 if self.current_number is None or self.current_number is False else 1)),
            TLObject.serialize_bytes(self.phone_number),
            b'' if self.current_number is None or self.current_number is False else (b'\xb5ur\x99' if self.current_number else b'7\x97y\xbc'),
            struct.pack('<i', self.api_id),
            TLObject.serialize_bytes(self.api_hash),
        ))

    @staticmethod
    def from_reader(reader):
        flags = reader.read_int()

        _allow_flashcall = bool(flags & 1)
        _phone_number = reader.tgread_string()
        if flags & 1:
            _current_number = reader.tgread_bool()
        else:
            _current_number = None
        _api_id = reader.read_int()
        _api_hash = reader.tgread_string()
        return SendCodeRequest(phone_number=_phone_number, api_id=_api_id, api_hash=_api_hash, allow_flashcall=_allow_flashcall, current_number=_current_number)


class SendInvitesRequest(TLObject):
    CONSTRUCTOR_ID = 0x771c1d97
    SUBCLASS_OF_ID = 0xf5b399ac

    def __init__(self, phone_numbers, message):
        """
        :param list[str] phone_numbers:
        :param str message:

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_numbers = phone_numbers
        self.message = message

    def to_dict(self):
        return {
            '_': 'SendInvitesRequest',
            'phone_numbers': [] if self.phone_numbers is None else self.phone_numbers[:],
            'message': self.message
        }

    def __bytes__(self):
        return b''.join((
            b'\x97\x1d\x1cw',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.phone_numbers)),b''.join(TLObject.serialize_bytes(x) for x in self.phone_numbers),
            TLObject.serialize_bytes(self.message),
        ))

    @staticmethod
    def from_reader(reader):
        reader.read_int()
        _phone_numbers = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_string()
            _phone_numbers.append(_x)

        _message = reader.tgread_string()
        return SendInvitesRequest(phone_numbers=_phone_numbers, message=_message)


class SignInRequest(TLObject):
    CONSTRUCTOR_ID = 0xbcd51581
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number, phone_code_hash, phone_code):
        """
        :param str phone_number:
        :param str phone_code_hash:
        :param str phone_code:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def to_dict(self):
        return {
            '_': 'SignInRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'phone_code': self.phone_code
        }

    def __bytes__(self):
        return b''.join((
            b'\x81\x15\xd5\xbc',
            TLObject.serialize_bytes(self.phone_number),
            TLObject.serialize_bytes(self.phone_code_hash),
            TLObject.serialize_bytes(self.phone_code),
        ))

    @staticmethod
    def from_reader(reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        _phone_code = reader.tgread_string()
        return SignInRequest(phone_number=_phone_number, phone_code_hash=_phone_code_hash, phone_code=_phone_code)


class SignUpRequest(TLObject):
    CONSTRUCTOR_ID = 0x1b067634
    SUBCLASS_OF_ID = 0xb9e04e39

    def __init__(self, phone_number, phone_code_hash, phone_code, first_name, last_name):
        """
        :param str phone_number:
        :param str phone_code_hash:
        :param str phone_code:
        :param str first_name:
        :param str last_name:

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        return {
            '_': 'SignUpRequest',
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'phone_code': self.phone_code,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def __bytes__(self):
        return b''.join((
            b'4v\x06\x1b',
            TLObject.serialize_bytes(self.phone_number),
            TLObject.serialize_bytes(self.phone_code_hash),
            TLObject.serialize_bytes(self.phone_code),
            TLObject.serialize_bytes(self.first_name),
            TLObject.serialize_bytes(self.last_name),
        ))

    @staticmethod
    def from_reader(reader):
        _phone_number = reader.tgread_string()
        _phone_code_hash = reader.tgread_string()
        _phone_code = reader.tgread_string()
        _first_name = reader.tgread_string()
        _last_name = reader.tgread_string()
        return SignUpRequest(phone_number=_phone_number, phone_code_hash=_phone_code_hash, phone_code=_phone_code, first_name=_first_name, last_name=_last_name)
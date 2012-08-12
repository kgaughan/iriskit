"""
An implementation of `RFC 4993`_: Lightweight UDP Transfer Protocol for
IRIS.
"""

import struct

from iriskit.transportsupport import E


PROTOCOL_ID = "iris.lwz1"


PAYLOAD_XML = 0 << 6
PAYLOAD_VERSION_INFO = 1 << 6
PAYLOAD_SIZE_INFO = 2 << 6
PAYLOAD_OTHER_INFO = 3 << 6


def pack_request(payload_type, transaction_id, is_compressed, authority):
    """
    Build a request packet descriptor.
    """
    assert (payload_type & ~0b01000000) == 0, "Bad payload type"
    assert 0 < transaction_id < 0xFFFF, "Bad transaction ID"
    # bit 4 = DEFLATE is supported; bit 2 = response packet
    header = payload_type | (1 << 4)
    if is_compressed:
        header |= 1 << 3
    return struct.pack("!BHHp", header, transaction_id, 4000, authority)


def pack_response(payload_type, transaction_id, is_compressed):
    """
    Build a response packet descriptor.
    """
    assert (payload_type & ~0b11000000) == 0, "Bad payload type"
    assert 0 < transaction_id < 0xFFFF, "Bad transaction ID"
    # bit 4 = DEFLATE is supported; bit 2 = response packet
    header = payload_type | (1 << 4) | (1 << 2)
    if is_compressed:
        header |= 1 << 3
    return struct.pack("!BH", header, transaction_id)


def build_size_info(octets):
    """
    Build a size info payload.
    """
    return E.responseSize(E.octets(octets))

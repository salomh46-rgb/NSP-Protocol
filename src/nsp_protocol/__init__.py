"""
NSP (Neural Semantic Protocol) v1.0.0
Glass-box, token-efficient inter-agent symbolic communication protocol.
"""

from .packet import NSPPacket
from .decoder import NSPDecoder
from .opcodes import OPCODES, register_opcode

__version__ = "1.0.0"
__all__ = ["NSPPacket", "NSPDecoder", "OPCODES", "register_opcode"]

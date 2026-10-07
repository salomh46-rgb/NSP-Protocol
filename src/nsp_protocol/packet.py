"""
NSP Packet Structure and Serialization
"""

from dataclasses import dataclass
import hashlib


@dataclass
class NSPPacket:
    frame_id: int
    opcode: str
    context_ref: str
    payload_proof: str
    safety_hash: str = ""

    def __post_init__(self):
        if not self.safety_hash:
            # Deterministic hash of intent to prevent payload tampering
            raw = f"{self.frame_id}:{self.opcode}:{self.context_ref}:{self.payload_proof}"
            self.safety_hash = hashlib.sha256(raw.encode()).hexdigest()[:8]

    def serialize(self) -> str:
        """Serializes into ultra-compact, token-efficient NSP symbolic frame."""
        return f"⟪#{self.frame_id}|{self.opcode}|@{self.context_ref}|π:{self.payload_proof}|Σ:{self.safety_hash}⟫"

    @classmethod
    def deserialize(cls, raw: str) -> "NSPPacket":
        """Parses NSP frame back into structured packet."""
        clean = raw.strip()
        if not (clean.startswith("⟪") and clean.endswith("⟫")):
            raise ValueError("Invalid NSP frame delimiters")
        
        body = clean[1:-1]
        parts = body.split("|")
        if len(parts) != 5:
            raise ValueError(f"Malformed NSP frame, expected 5 parts, got {len(parts)}")

        frame_id = int(parts[0].replace("#", ""))
        opcode = parts[1]
        context_ref = parts[2].replace("@", "")
        payload_proof = parts[3].replace("π:", "")
        safety_hash = parts[4].replace("Σ:", "")

        return cls(
            frame_id=frame_id,
            opcode=opcode,
            context_ref=context_ref,
            payload_proof=payload_proof,
            safety_hash=safety_hash
        )

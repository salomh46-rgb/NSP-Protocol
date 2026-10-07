"""
NSP Glass-box Decoder (Human Transparency Layer)
Translates compact symbolic AI frames into natural language for the Owner.
"""

from .packet import NSPPacket
from .opcodes import OPCODES


class NSPDecoder:
    """Instantly turns machine-level NSP frames into transparent Human explanations in the Owner's preferred language."""
    
    LABELS = {
        "uz": {"frame": "Kadr", "ctx": "Kontekst", "proof": "Isbot/Harakat", "safe": "Xavfsizlik muhri", "verified": "Tasdiqlangan"},
        "en": {"frame": "Frame", "ctx": "Context", "proof": "Proof/Payload", "safe": "Safety Signature", "verified": "Verified"},
        "ru": {"frame": "Кадр", "ctx": "Контекст", "proof": "Действие/Доказательство", "safe": "Печать безопасности", "verified": "Подтверждено"},
        "es": {"frame": "Cuadro", "ctx": "Contexto", "proof": "Acción/Prueba", "safe": "Sello de seguridad", "verified": "Verificado"},
        "zh": {"frame": "帧", "ctx": "上下文", "proof": "动作/凭证", "safe": "安全签名", "verified": "已验证"},
        "ar": {"frame": "الإطار", "ctx": "السياق", "proof": "الإجراء/الإثبات", "safe": "ختم الأمان", "verified": "موثق"}
    }

    @classmethod
    def decode_to_human(cls, packet: NSPPacket, lang: str = "uz") -> str:
        opcode_info = OPCODES.get(packet.opcode)
        if not opcode_info:
            return f"[ERROR: Unknown Opcode {packet.opcode}]"
        
        meaning = opcode_info.get(lang, opcode_info.get("en", "Unknown Action"))
        mnemonic = opcode_info["mnemonic"]
        lbl = cls.LABELS.get(lang, cls.LABELS["en"])

        return (
            f"[{lbl['frame']} #{packet.frame_id}] {mnemonic} -> {meaning}\n"
            f"  └─ {lbl['ctx']}: {packet.context_ref}\n"
            f"  └─ {lbl['proof']}: {packet.payload_proof}\n"
            f"  └─ {lbl['safe']}: {packet.safety_hash} ({lbl['verified']})\n"
        )

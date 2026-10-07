"""
Unit tests for NSP Protocol
"""

import unittest
from nsp_protocol import NSPPacket, NSPDecoder, OPCODES, register_opcode


class TestNSPProtocol(unittest.TestCase):

    def test_packet_serialization_and_deserialization(self):
        packet = NSPPacket(
            frame_id=42,
            opcode="0x32",
            context_ref="state_root",
            payload_proof="Balance -= 500"
        )
        serialized = packet.serialize()
        self.assertTrue(serialized.startswith("⟪#42|0x32|@state_root|π:Balance -= 500|Σ:"))
        self.assertTrue(serialized.endswith("⟫"))

        # Deserialize back
        deserialized = NSPPacket.deserialize(serialized)
        self.assertEqual(deserialized.frame_id, 42)
        self.assertEqual(deserialized.opcode, "0x32")
        self.assertEqual(deserialized.context_ref, "state_root")
        self.assertEqual(deserialized.payload_proof, "Balance -= 500")
        self.assertEqual(deserialized.safety_hash, packet.safety_hash)

    def test_multilingual_decoding(self):
        packet = NSPPacket(frame_id=1, opcode="0x01", context_ref="root", payload_proof="Goal:Audit")
        
        # Uzbek
        uz_text = NSPDecoder.decode_to_human(packet, lang="uz")
        self.assertIn("Vazifaning asosiy maqsadi belgilandi", uz_text)
        self.assertIn("Kadr #1", uz_text)

        # English
        en_text = NSPDecoder.decode_to_human(packet, lang="en")
        self.assertIn("Declared root goal", en_text)
        self.assertIn("Frame #1", en_text)

        # Russian
        ru_text = NSPDecoder.decode_to_human(packet, lang="ru")
        self.assertIn("Определена главная цель задачи", ru_text)

    def test_custom_opcode_registration(self):
        register_opcode("0xAA", "CUSTOM_TASK", {"uz": "Maxsus vazifa", "en": "Custom task"})
        self.assertIn("0xAA", OPCODES)
        
        packet = NSPPacket(frame_id=9, opcode="0xAA", context_ref="test", payload_proof="data")
        decoded = NSPDecoder.decode_to_human(packet, lang="uz")
        self.assertIn("Maxsus vazifa", decoded)


if __name__ == "__main__":
    unittest.main()

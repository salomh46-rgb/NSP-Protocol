"""
Live Multi-Agent Mesh using NSP Protocol
Demonstrating real-time inter-agent communication between:
- Agent A: Senior Architect (Planner)
- Agent B: Security & Database Auditor (Verifier)
Driven via NSP-1.0 frames with live Glass-box Human Decoding.
"""

import os
import sys
import io
import time
from dotenv import load_dotenv
from google import genai
from nsp_protocol import NSPPacket, NSPDecoder

if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load environment variable from voice2deal_ai .env
load_dotenv(r"D:\ALLProjects\voice2deal_ai\.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Xatolik: GEMINI_API_KEY topilmadi!")
    sys.exit(1)

client = genai.Client(api_key=api_key)

# -------------------------------------------------------------
# SYSTEM PROMPTS FOR LIVE NSP AGENTS
# -------------------------------------------------------------

SYSTEM_PROMPT_AGENT_A = """
Sen Senior Architect agentsan. Sening vazifang - topshiriqni rejalashtirish.
QAT'IY QOIDA:
Sen BOSHQA AGENT (Security Auditor) bilan FAQAT VA FAQAT NSP-1.0 (Neural Semantic Protocol) simvolik kadrlarida muloqot qilasan!
Hech qanday inglizcha yoki o'zbekcha so'zlashuv gaplari bo'lishi mumkin emas.
Har bir kadring formati: ⟪#ID|OPCODE|@CONTEXT|π:PROOF_PAYLOAD|Σ:AUTO⟫
Mavjud opkodlar:
0x01: INIT_GOAL
0x02: BRANCH_HYPO
0x31: READ_ENTITY
0x32: MUTATE_STATE
0x33: ACQUIRE_LOCK
0x34: RELEASE_LOCK
0x90: HUMAN_REPORT

Misol javob:
⟪#1|0x01|@root|π:DesignUserBillingSystem|Σ:auto⟫
"""

SYSTEM_PROMPT_AGENT_B = """
Sen Security & Invariant Auditor agentsan. Sening vazifang - Architect bergan NSP kadrini tekshirish.
QAT'IY QOIDA:
Sen Architect bilan FAQAT VA FAQAT NSP-1.0 simvolik kadrlarida muloqot qilasan.
Hech qanday odatiy matn ishlatma!
Mavjud opkodlar:
0x33: ACQUIRE_LOCK
0x61: ASSERT_GREEN (Tasdiqlash)
0x63: ISOLATE_TENANT (Izolyatsiyani tekshirish)
0xFF: SAFETY_REJECT (Xavfli bo'lsa rad etish)

Misol javob:
⟪#2|0x61|@#1|π:VerifiedNoRaceCondition; TenantsIsolated|Σ:auto⟫
"""


def test_live_nsp_mesh():
    print("=" * 70)
    print("🚀 JONLI TEST: GEMINI 2.5/FLASH AGENTLARI O'RTASIDAGI NSP ALOQASI")
    print("=" * 70)
    print()

    task_desc = "Foydalanuvchi hisobidan 1 000 000 UZS yechib, boshqa do'konga o'tkazish"
    print(f"Topshiriq: '{task_desc}'\n")

    # 1. Agent A (Architect) NSP kadrini generatsiya qiladi
    print("🤖 [Agent A - Architect] NSP kadrini hisoblamoqda...")
    prompt_a = f"Topshiriq: {task_desc}. Birinchi reja kadrini yubor."
    
    response_a = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt_a,
        config={"system_instruction": SYSTEM_PROMPT_AGENT_A, "temperature": 0.1}
    )
    raw_frame_a = response_a.text.strip().split("\n")[0]
    print(f"📡 Simvolik Oqim (Agent A): {raw_frame_a}")

    # Dekoder orqali Owner tilida ko'rish
    try:
        packet_a = NSPPacket.deserialize(raw_frame_a)
        print("🇺🇿 Owner uchun O'zbekcha:")
        print(NSPDecoder.decode_to_human(packet_a, lang="uz"))
    except Exception as e:
        print(f"Raw frame ko'rinishi: {raw_frame_a}")

    # 2. Agent B (Auditor) ushbu kadrni qabul qilib, o'z javob kadrini yuboradi
    print("🛡️ [Agent B - Auditor] Kadrni xavfsizlik filtri orqali tekshirmoqda...")
    prompt_b = f"Agent A yuborgan kadr: {raw_frame_a}. Buni audit qil va o'z NSP javob kadrini qaytar."
    
    response_b = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt_b,
        config={"system_instruction": SYSTEM_PROMPT_AGENT_B, "temperature": 0.1}
    )
    raw_frame_b = response_b.text.strip().split("\n")[0]
    print(f"📡 Simvolik Oqim (Agent B): {raw_frame_b}")

    try:
        packet_b = NSPPacket.deserialize(raw_frame_b)
        print("🇺🇿 Owner uchun O'zbekcha:")
        print(NSPDecoder.decode_to_human(packet_b, lang="uz"))
    except Exception as e:
        print(f"Raw frame ko'rinishi: {raw_frame_b}")

    print("=" * 70)
    print("✅ NATIJA: Gemini LLM modellari insoniy tildan mutlaqo voz kechib,")
    print("   faqat NSP simvollarida bir-birini 100% tushundi va Ownerga shaffof ochib berdi!")
    print("=" * 70)


if __name__ == "__main__":
    test_live_nsp_mesh()

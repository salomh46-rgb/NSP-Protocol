# NEURAL SEMANTIC PROTOCOL (NSP-1.0)
## Autonomous Systems & Multi-Agent Swarm Liability Policy
### Avtonom Tizimlar va Agentlar To'dasi Yuridik Javobgarligi To'g'risidagi Nizom

**Effective Date / Kuchga kirish sanasi:** October 8, 2026  
**Protocol Version / Protokol versiyasi:** NSP-1.0 (Neural Semantic Protocol)  
**Author & Architect / Muallif va Arxitektor:** Javohirbek Asqarov (Jasper) & Antigravity Contributors  
**Governing Standard / Huquqiy rejim:** Open Inter-Agent Specification & MIT License  

---

> ### ⚠️ SUMMARY / QISQACHA MAZMUNI
> 
> **EN:** The Neural Semantic Protocol (NSP-1.0) is a deterministic communication standard and grammar specification. The Protocol Author (Javohirbek Asqarov / Jasper) provides this specification and reference implementation strictly on an **"AS IS"** and **"AS AVAILABLE"** basis without warranties of any kind. The Author exercises **zero control, custody, or agency** over third-party agents, swarms, runtime environments, or execution engines utilizing NSP. **Any and all actions, state mutations (`0x32 MUTATE_STATE`), autonomous transactions, financial losses, API expenditures, data corruption, or infrastructure damage caused by autonomous agents are the sole, direct, and exclusive legal and financial liability of the deploying Operator/Integrator.**
>
> **UZ:** Neural Semantic Protocol (NSP-1.0) — bu ochiq kommunikatsiya standarti va semantik grammatika spetsifikatsiyasidir. Protokol Muallifi (Javohirbek Asqarov / Jasper) mazkur spetsifikatsiya va namunaviy kodni qat'iy ravishda **"XUDDI SHUNDAY" ("AS IS")** va **"MAVJUD BO'LGANIDЕK" ("AS AVAILABLE")** shartlarida, hech qanday kafolatlarsiz taqdim etadi. Muallif NSP dan foydalanuvchi uchinchi tomon AI agentlari, agentlar to'dalari (swarms) yoki ijro muhitlari ustidan **hech qanday nazorat, boshqaruv yoki egalik huquqiga ega emas**. Avtonom agentlarning har qanday xatti-harakatlari, holat o'zgartirishlari (`0x32 MUTATE_STATE`), moliyaviy tranzaksiyalari, token/kredit sarflari, ma'lumotlar yo'qotilishi yoki tizimli nosozliklar uchun **to'liq, shaxsiy va mutlaq huquqiy/moliyaviy javobgarlik faqat va faqat tizimni ishga tushirgan Operator/Integrator zimmasidadir.**

---

# SECTION I: ENGLISH JURIDICAL TEXT

### 1. Definitions & Scope
1. **"Protocol" or "NSP-1.0":** Refers to the Neural Semantic Protocol specification, token grammar, serialization logic, opcode registry, and reference code developed by Javohirbek Asqarov (Jasper).
2. **"Protocol Author":** Javohirbek Asqarov (Jasper), Antigravity Engine, and authorized contributors of the NSP-Protocol repository.
3. **"Operator" or "Integrator":** Any individual, corporation, organization, or developer deploying, executing, embedding, or connecting AI models, agent loops, autonomous swarms, or systems using NSP-1.0 frames.
4. **"Autonomous Agent" / "Agent Swarm":** Any artificial intelligence system, large language model (LLM) loop, autonomous daemon, task executor, or cluster of collaborating autonomous entities communicating via NSP packets (`⟪...⟫`).
5. **"State Mutation" (`0x32 MUTATE_STATE`):** Any operation initiated, suggested, or executed by an agent that creates, reads, updates, deletes, transfers, locks, or mutates external databases, files, cryptographic keys, APIs, financial accounts, or runtime environments.

---

### 2. Nature of the Protocol: Pure Communication Layer
NSP-1.0 is strictly an **abstract communication format and grammar serialization layer**. 
1. The Protocol does **not** execute actions by itself.
2. The Protocol does **not** hold funds, custodial keys, API credentials, or physical server access.
3. The Protocol does **not** possess self-awareness, intentional agency, or autonomous decision-making capabilities.
4. The Protocol Author acts solely as an author of open technical documentation and code under the MIT License, and **never** as an agent, broker, fiduciary, partner, or joint venturer of any Operator.

---

### 3. Absolute Immunity for Autonomous Actions & State Mutations
1. **Non-Involvement in Execution:** The Protocol Author has zero knowledge, control, or monitoring capabilities over private agent clusters deployed by third-party Operators.
2. **`0x32 MUTATE_STATE` Operations:** While NSP defines the opcode `0x32` (`MUTATE_STATE`) for deterministic state transitions, the decision to execute, permit, validate, or sandbox any state mutation rests entirely on the Operator's runtime engine. The Protocol Author shall have **ZERO LIABILITY** for:
   - Unauthorized database writes, updates, deletions, or corruptions.
   - Financial transactions, automated smart contract executions, token transfers, or fund liquidations initiated by agents.
   - Unauthorized network requests, API calls, cloud infrastructure provisioning, or compute billing overruns.
   - Race conditions, resource deadlocks, or distributed concurrency lock (`0x33 ACQUIRE_LOCK`) deadlocks.
3. **Hallucinations & Misalignment:** Autonomous agents may misinterpret context, experience hallucinations, or enter recursive loops. The Protocol Author cannot be held liable for any decisions, inferences, or erroneous consensus (`0x04 CONVERGE`) generated by autonomous models.

---

### 4. Sole Liability of the Deployer / Operator
By downloading, cloning, integrating, or running NSP-1.0, the Operator explicitly acknowledges, warrants, and agrees that:
1. **Operational Custody:** The Operator maintains 100% legal, operational, civil, and criminal custody over all agents, swarms, and runtimes operating in their infrastructure.
2. **Financial Responsibility:** The Operator assumes all financial liabilities, including but not limited to third-party damages, loss of business revenue, regulatory fines, and cloud computing costs caused by autonomous swarms.
3. **Sandbox & Gatekeeping Obligations:** It is the affirmative duty of the Operator to implement sandboxing, rate-limiting, human approval steps, and cryptographic validation before executing any `MUTATE_STATE` frame.

---

### 5. Duty to Implement Glass-Box Safety Primitives
NSP-1.0 provides explicit safety primitives in its specification, including:
- `0x90 HUMAN_REPORT` (Mandatory human inspection and sign-off).
- `0x99 EMERGENCY_HALT` (Immediate kill-switch and memory purge).
- `0xFF SAFETY_REJECT` (Rejection of unaligned frames).
- `Σ:hash` (Intent ancestral tamper-proofing).

**The Operator bears the sole legal duty** to connect these protocol opcodes to actual physical kill-switches and human confirmation interfaces within their software stack. Failure of the Operator to enforce human-in-the-loop controls or wire `0x99 EMERGENCY_HALT` to system termination constitutes gross negligence exclusively attributable to the Operator.

---

### 6. Disclaimer of Warranties ("AS IS" & "AS AVAILABLE")
TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, THE PROTOCOL SPECIFICATION AND REFERENCE CODE ARE PROVIDED **"AS IS"**, **"WITH ALL FAULTS"**, AND **"AS AVAILABLE"**, WITHOUT WARRANTY OF ANY KIND, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE, INCLUDING BUT NOT LIMITED TO:
- WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
- WARRANTIES OF ACCURACY, RELIABILITY, FREEDOM FROM PROGRAM ERRORS, PROTOCOL DEADLOCKS, OR LATENT AMBIGUITIES.
- WARRANTIES OF CONTINUOUS, UNINTERRUPTED, OR COMPLIANT OPERATION WITH REGIONAL AI REGULATIONS.

---

### 7. Absolute Limitation of Liability ($0.00 Author Liability Cap)
1. UNDER NO CIRCUMSTANCES SHALL THE PROTOCOL AUTHOR (JAVOHIRBEK ASQAROV / JASPER), CONTRIBUTORS, OR AFFILIATES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, PUNITIVE, OR EXEMPLARY DAMAGES WHATSOEVER (INCLUDING DAMAGES FOR LOSS OF PROFITS, DATA LOSS, INFRASTRUCTURE CORRUPTION, BUSINESS INTERRUPTION, REPUTATIONAL DAMAGE, OR CYBERSECURITY BREACHES), ARISING OUT OF OR IN CONNECTION WITH THE USE, INABILITY TO USE, OR EXECUTION OF NSP-1.0 PACKETS BY ANY AUTONOMOUS SYSTEM.
2. IN THE EVENT THAT ANY JURISDICTION DOES NOT ALLOW THE COMPLETE EXCLUSION OF LIABILITY, THE MAXIMUM CUMULATIVE AGGREGATE LIABILITY OF THE PROTOCOL AUTHOR TO ANY PARTY FOR ANY AND ALL CLAIMS SHALL BE CAPPED AT EXACTLY **ZERO UNITED STATES DOLLARS ($0.00 USD)**, OR THE MINIMUM AMOUNT PERMITTED BY MANDATORY LAW NOT TO EXCEED ONE UNITED STATES DOLLAR ($1.00 USD).

---

### 8. Full Indemnification & Hold Harmless
The Operator agrees to defend, indemnify, and hold harmless the Protocol Author (Javohirbek Asqarov) from and against any and all claims, actions, suits, arbitrations, regulatory inquiries, fines, liabilities, losses, damages, costs, and expenses (including reasonable attorney's fees) arising out of or related to:
1. The Operator's deployment, operation, or misuse of NSP-1.0.
2. Any autonomous decision, state mutation, financial transfer, or breach caused by the Operator's agent swarms.
3. Any failure of the Operator to comply with personal data protection laws, intellectual property rights, or local algorithmic governance laws.

---

### 9. Governing Law & Exclusive Forum Selection
1. This Policy, its interpretation, and any dispute arising out of or related to the Protocol shall be governed exclusively by the substantive laws of the **Republic of Uzbekistan**, without regard to conflict of law principles.
2. Any legal proceeding, dispute, claim, or controversy arising out of or relating to NSP-1.0 shall be submitted to the exclusive jurisdiction of the competent courts of **Tashkent City, Republic of Uzbekistan**. The Operator irrevocably waives any objection to venue, jurisdiction, or forum non conveniens.

---

# SECTION II: O'ZBEK TILI (RASMIY HUQUQIY MATN)

### 1-Modda. Qo'llanilish sohasi va Asosiy tushunchalar
1. **NSP-1.0 (Neural Semantic Protocol):** Javohirbek Asqarov (Jasper) tomonidan ishlab chiqilgan sun'iy intellekt agentlari o'rtasida ramziy, yuqori zichlikdagi va shisha-quti (glass-box) formatida ma'lumot almashish uchun ochiq spetsifikatsiya, grammatika qoidalari va namunaviy dasturiy kod.
2. **Protokol Muallifi:** Javohirbek Asqarov (Jasper), Antigravity tizimi va NSP-Protocol omborining rasmiy kod mualliflari.
3. **Integrator / Operator:** NSP-1.0 protokoli asosida o'zining yoki uchinchi tomon dasturlari, neyrotarmoq modellari, avtonom agentlari yoki server tizimlarini ishga tushiruvchi har qanday jismoniy yoki yuridik shaxs.
4. **Avtonom Agentlar va Agentlar To'dasi (Multi-Agent Swarms):** Operator tomonidan ishga tushirilgan, mustaqil ravishda qaror qabul qiluvchi, buyruqlar zanjirini bajaruvchi va NSP paketlari (`⟪...⟫`) orqali bir-biri bilan aloqa qiluvchi sun'iy intellekt tizimlari.
5. **Holat O'zgartirish (`0x32 MUTATE_STATE`):** Avtonom agent tomonidan taklif qilingan yoki amalga oshirilgan tashqi ma'lumotlar bazasi, fayl tizimi, tarmoq resurslari, moliyaviy hisoblar yoki infratuzilma holatiga ta'sir qiluvchi har qanday harakat.

---

### 2-Modda. Protokolning Huquqiy Tabiati: Mustaqil Aloqa Standarti
1. NSP-1.0 protokoli mutlaqo mustaqil, ochiq va neytral **ma'lumot almashish tili (sintaksisi)** hisoblanadi.
2. Protokol hech qanday avtonom sub'ekt, ishonchli vakil (fiduciary), moliyaviy vositachi, broker yoki boshqaruvchi tuzilma hisoblanmaydi.
3. Protokol Muallifi MIT xalqaro litsenziyasi doirasida ochiq standartni taqdim etadi va uchinchi tomon agentlarining qachon, qayerda va qanday maqsadlarda ishlatilayotganini nazorat qilmaydi hamda nazorat qilish imkoniyatiga ega emas.

---

### 3-Modda. Muallifning Mutlaq Daxlsizligi (Holat O'zgartirish va Tranzaksiyalar)
1. **`0x32 MUTATE_STATE` amallari uchun daxlsizlik:** Garchi NSP protokoli spetsifikatsiyasida holat o'zgarishini ifodalash uchun `0x32` opkodi ko'zda tutilgan bo'lsa-da, bu amalni haqiqiy infratuzilmada bajarish, ruxsat berish yoki bloklash faqat va faqat Integrator/Operator tizimiga bog'liq.
2. Protokol Muallifi quyidagi holatlar uchun **MUTLAQ VA NOL ($0) JAVOBGARLIKKA** ega:
   - Avtonom agentlar tomonidan ma'lumotlar bazalarini o'chirish, buzish, o'zgartirish yoki sizdirish;
   - Bank kartalari, to'lov tizimlari (Payme, Click, Uzum, Stripe va boshqalar), kripto-hamyonlar yoki aqlli shartnomalar orqali agentlar tomonidan ruxsatsiz yoki xato o'tkazilgan moliyaviy tranzaksiyalar;
   - Server va bulutli xizmatlar (cloud computing) xarajatlarining oshib ketishi, behuda token sarfi yoki tizim resurslarining tugab qolishi;
   - Neyrotarmoq modellarining gallyutsinatsiyalari, xato mantiqiy xulosalari (`0x04 CONVERGE`) yoki agentlar o'rtasida yuzaga kelgan cheksiz ziddiyatli sikllar (infinite deadlocks).

---

### 4-Modda. Operator va Integratorning To'liq Shaxsiy Javobgarligi
NSP-1.0 protokolidan foydalanuvchi har bir Integrator va Operator o'z zimmasiga quyidagi qat'iy majburiyatlarni oladi:
1. **To'liq Operatsion Nazorat:** Operator o'zi joylashtirgan agentlar to'dasi keltirib chiqarishi mumkin bo'lgan barcha harakatlar, qarorlar va texnik xatoliklar uchun O'zbekiston Respublikasi qonunchiligi va xalqaro huquq normalari oldida to'liq, shaxsiy va mutlaq javobgardir.
2. **Xavfsiz Muhit (Sandbox) Yaratish Majburiyati:** Operator avtonom agentlarga `MUTATE_STATE` amallarini to'g'ridan-to'g'ri bajarishga ruxsat bermasdan oldin, ularni qat'iy tekshiruv, izolyatsiyalangan muhit (sandbox) va inson tasdig'i (human verification) filtrlari orqali o'tkazishi shart. Ushbu himoya choralarini ko'rmaslik Operatorning o'ta qo'pol ehtiyotsizligi (gross negligence) deb baholanadi.

---

### 5-Modda. Inson Nazorati (Human-in-the-Loop) Mexanizmlari
NSP protokoli o'z arxitekturasida agentlar xavfsizligini ta'minlash uchun quyidagi maxsus opkodlarni taqdim etadi:
- `0x90 HUMAN_REPORT` (Muhim qarorlarni inson tekshiruviga yuborish).
- `0x99 EMERGENCY_HALT` (Favqulodda to'xtatish - Kill-Switch).
- `0xFF SAFETY_REJECT` (Mos kelmaydigan amallarni rad etish).

Ushbu opkodlarni real dasturiy ta'minot tugmalari, server signallari va inson nazorati mexanizmlariga ulash **faqat va faqat Operatorning burchi** hisoblanadi. Agar Operator o'z tizimida inson nazoratini o'rnatmagan bo'lsa yoki favqulodda to'xtatish vositasini joriy qilmagan bo'lsa, oqibatda kelib chiqadigan har qanday talafot uchun Muallif hech qanday mas'uliyatni o'z zimmasiga olmaydi.

---

### 6-Modda. Kafolatlardan To'liq Voz Kechish ("XUDDI SHUNDAY")
Qo'llanilishi mumkin bo'lgan qonun hujjatlarining eng yuqori doirasida, ushbu protokol va dasturiy ta'minot **"XUDDI SHUNDAY" ("AS IS")** va **"MAVJUD BO'LGANIDЕK" ("AS AVAILABLE")** shartlarida taqdim etiladi. Protokol Muallifi hech qanday to'g'ridan-to'g'ri yoki bilvosita kafolatlarni, shu jumladan tovarboplik, ma'lum bir maqsadga muvofiqlik, xatosizlik yoki tizim uzluksizligi kafolatlarini bermaydi.

---

### 7-Modda. Zararlar va Javobgarlikning Mutlaq Cheklanishi ($0 AQSh Dollari)
1. O'zbekiston Respublikasi Fuqarolik Kodeksining 327, 985 va 998-moddalari doirasida, Protokol Muallifi uchinchi tomon agentlarining xatti-harakatlari tufayli yetkazilgan hech qanday to'g'ridan-to'g'ri, bilvosita, tasodifiy, maxsus yoki oqibatli zararlar (shu jumladan boy berilgan foyda, tijoriy to'xtab qolish, ma'lumotlar yo'qotilishi, reputatsiya putur yetishi yoki jarimalar) uchun javobgar bo'lmaydi.
2. Har qanday holatda, har qanday da'vo bo'yicha Protokol Muallifining maksimal umumiy javobgarlik summasi **0 (NOL) AQSh DOLLARI** yoki O'zbekiston Respublikasi milliy valyutasida **0 (NOL) SO'M** etib belgilanadi.

---

### 8-Modda. Da'volardan Himoya Qilish va To'lovlarni Qoplash (Indemnification)
Integrator/Operator o'zining avtonom agentlari yoki tizimlaridan foydalanishi natijasida uchinchi shaxslar yoki davlat organlari tomonidan Protokol Muallifiga (Javohirbek Asqarov) nisbatan bildirilgan har qanday moddiy da'volar, jarimalar, sud xarajatlari va advokat gonorarlarini to'liq o'z hisobidan qoplashni, muallifni har qanday javobgarlikdan soqit qilishni va himoya qilishni so'zsiz o'z zimmasiga oladi.

---

### 9-Modda. Shaxsiy Ma'lumotlar va Normativ Talablar
1. Integrator NSP paketlari orqali har qanday ma'lumotlarni uzatishda O'zbekiston Respublikasining "Shaxsiy ma'lumotlar to'g'risida"gi Qonuni (№ 547-son) talablariga, shaxsiy ma'lumotlar bazalarining davlat reyestrida ro'yxatdan o'tkazilishi va O'zR hududida saqlanishi shartlariga to'liq rioya qilishga shaxsan javobgardir.
2. Xalqaro integratsiyalar holatida GDPR, CCPA va boshqa tegishli ma'lumotlar xavfsizligi standartlariga rioya etish majburiyati butunlay Operator zimmasidadir.

---

### 10-Modda. Qo'llaniladigan Huquq va Sud Yurisdiksiyasi
1. Mazkur Nizom va NSP-1.0 protokoli bilan bog'liq har qanday huquqiy munosabatlar O'zbekiston Respublikasining amaldagi qonunchiligi asosida tartibga solinadi va talqin qilinadi.
2. Kelib chiqishi mumkin bo'lgan har qanday nizo, kelishmovchilik yoki da'volar yuzasidan taraflar sudgacha bo'lgan majburiy 30 kunlik yozma e'tiroz (pretenziya) tartibini qo'llaydilar.
3. Kelishuvga erishilmagan taqdirda, barcha nizolar **O'zbekiston Respublikasi, Toshkent shahri sudlarida** (eksklyuziv sudlovlik huquqi asosida) ko'rib chiqiladi.

---

**Protocol Architecture Certified by:**  
**Javohirbek Asqarov (Jasper)**  
*Senior Cyber-Lawyer, Compliance Architect & Protocol Author*  
*Contact:* `jasper@antigravity.ai` | *Official Repository:* `https://github.com/salomh46-rgb/NSP-Protocol`

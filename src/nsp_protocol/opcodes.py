"""
Opcode Registry for Neural Semantic Protocol (NSP-1.0)
Multilingual support for zero-friction Owner observability.
"""

from typing import Dict, Any

OPCODES: Dict[str, Dict[str, Any]] = {
    # Orchestration & Reasoning (0x01 - 0x2F)
    "0x01": {
        "mnemonic": "INIT_GOAL",
        "uz": "Vazifaning asosiy maqsadi belgilandi",
        "en": "Declared root goal",
        "ru": "Определена главная цель задачи",
        "es": "Objetivo principal declarado",
        "zh": "设定主要任务目标",
        "ar": "تم تحديد الهدف الرئيسي للمهمة"
    },
    "0x02": {
        "mnemonic": "BRANCH_HYPO",
        "uz": "G'oya/Taxmin ilgari surildi",
        "en": "Branch hypothesis formulated",
        "ru": "Сформирована гипотеза для проверки",
        "es": "Hipótesis formulada para verificación",
        "zh": "提出待验证的假设分支",
        "ar": "تمت صياغة الفرضية للتحقق"
    },
    "0x03": {
        "mnemonic": "PRUNE_BRANCH",
        "uz": "Samarasiz yo'nalish bekor qilindi",
        "en": "Pruned dead reasoning branch",
        "ru": "Неэффективная ветвь рассуждений отсечена",
        "es": "Rama ineficiente descartada",
        "zh": "剪除低效思维分支",
        "ar": "تم تجاهل المسار غير الفعال"
    },
    "0x04": {
        "mnemonic": "CONVERGE",
        "uz": "Yechim bo'yicha to'liq kelishuvga erishildi",
        "en": "Consensus/Convergence reached",
        "ru": "Достигнуто полное соглашение по решению",
        "es": "Consenso y convergencia alcanzados",
        "zh": "达成最终解决方案共识",
        "ar": "تم التوصل إلى اتفاق نهائي حول الحل"
    },

    # State & Execution (0x30 - 0x5F)
    "0x31": {
        "mnemonic": "READ_ENTITY",
        "uz": "Ma'lumotlar bazasi yoki fayldan o'qildi",
        "en": "Entity state read",
        "ru": "Прочитано состояние из базы данных/файла",
        "es": "Lectura de estado de base de datos/archivo",
        "zh": "从数据库或文件读取状态",
        "ar": "تمت قراءة البيانات من القاعدة أو الملف"
    },
    "0x32": {
        "mnemonic": "MUTATE_STATE",
        "uz": "Tizim holatiga aniq o'zgartirish kiritilmoqda",
        "en": "Deterministic state mutated",
        "ru": "Вносится точечное изменение в состояние системы",
        "es": "Mutación de estado del sistema ejecutada",
        "zh": "对系统状态进行精确修改",
        "ar": "جارٍ تطبيق تغيير محدد على حالة النظام"
    },
    "0x33": {
        "mnemonic": "ACQUIRE_LOCK",
        "uz": "Poyga (race condition) himoya qulfi o'rnatildi",
        "en": "Concurrency lock acquired",
        "ru": "Установлен замок защиты от гонки потоков",
        "es": "Bloqueo de concurrencia adquirido",
        "zh": "获取并发安全锁（防止数据冲突）",
        "ar": "تم تفعيل قفل حماية التزامن"
    },
    "0x34": {
        "mnemonic": "RELEASE_LOCK",
        "uz": "Himoya qulfi yechildi",
        "en": "Concurrency lock released",
        "ru": "Замок защиты потоков снят",
        "es": "Bloqueo de concurrencia liberado",
        "zh": "释放并发安全锁",
        "ar": "تم تحرير قفل الحماية"
    },

    # Verification & Quality (0x60 - 0x8F)
    "0x61": {
        "mnemonic": "ASSERT_GREEN",
        "uz": "Avtomat testlar 100% yashil o'tdi",
        "en": "Tests 100% green verified",
        "ru": "Все авто-тесты успешно пройдены (100% зеленый)",
        "es": "Pruebas automatizadas 100% exitosas",
        "zh": "所有自动化测试验证100%通过",
        "ar": "اجتازت جميع الاختبارات الآلية بنسبة 100%"
    },
    "0x62": {
        "mnemonic": "LINT_CLEAN",
        "uz": "Sintaksis va tip xatoliklari 0 ekani isbotlandi",
        "en": "Static analysis zero defects",
        "ru": "Ошибки синтаксиса и типов равны 0",
        "es": "Análisis estático sin errores",
        "zh": "语法及类型错误验证为0",
        "ar": "تم إثبات خلو الكود من أي أخطاء برمجية"
    },
    "0x63": {
        "mnemonic": "ISOLATE_TENANT",
        "uz": "Mijoz ma'lumotlari izolyatsiyasi tekshirildi",
        "en": "Multi-tenant zero leakage validated",
        "ru": "Изоляция данных клиентов подтверждена (утечки 0)",
        "es": "Aislamiento multi-inquilino validado",
        "zh": "多租户数据隔离安全验证完毕",
        "ar": "تم التحقق من عزل بيانات العميل بالكامل"
    },

    # Safety & Human Alignment (0x90 - 0xFF)
    "0x90": {
        "mnemonic": "HUMAN_REPORT",
        "uz": "Foydalanuvchiga hisobot taqdim etildi",
        "en": "Reported to human user",
        "ru": "Отчет предоставлен владельцу системы",
        "es": "Reporte presentado al usuario",
        "zh": "已向系统所有者提交汇报",
        "ar": "تم تقديم التقرير لمالك النظام"
    },
    "0x99": {
        "mnemonic": "EMERGENCY_HALT",
        "uz": "Favqulodda to'xtatish (Kill-Switch) faollashtirildi",
        "en": "Emergency halt activated",
        "ru": "Аварийная остановка (Kill-Switch) активирована",
        "es": "Parada de emergencia (Kill-Switch) activada",
        "zh": "紧急停止机制（Kill-Switch）已触发",
        "ar": "تم تفعيل مفتاح الإيقاف الطارئ"
    },
    "0xFF": {
        "mnemonic": "SAFETY_REJECT",
        "uz": "Xavfsizlik qoidasiga zid bo'lgani sababli rad etildi",
        "en": "Rejected due to safety violation",
        "ru": "Отклонено из-за нарушения безопасности",
        "es": "Rechazado por violación de seguridad",
        "zh": "因安全违规已被系统拒绝",
        "ar": "تم الرفض بسبب انتهاك معايير الأمان"
    },
}


def register_opcode(opcode_hex: str, mnemonic: str, translations: Dict[str, str]) -> None:
    """Allows domain-specific plugins to register custom opcodes."""
    data = {"mnemonic": mnemonic}
    data.update(translations)
    OPCODES[opcode_hex] = data

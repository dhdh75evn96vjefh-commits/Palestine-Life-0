# استيراد المهن والأنظمة
from professions.medical import Doctor
from professions.commercial import Merchant
from professions.technical import Engineer
from economy import EconomySystem

class MintEngine:
    def __init__(self):
        self.economy = EconomySystem()
        self.active_players = []

    def mint_character(self, player_name, job_type):
        """وظيفة إنشاء شخصية جديدة وتعيين مهنة لها"""
        if job_type == "doctor":
            job = Doctor()
        elif job_type == "merchant":
            job = Merchant()
        elif job_type == "engineer":
            job = Engineer()
        else:
            return "المهنة غير متوفرة حالياً."

        character_data = {
            "name": player_name,
            "job": job.role,
            "status": job.work(),
            "balance": 100 # رصيد افتراضي عند الإنشاء
        }
        self.active_players.append(character_data)
        return f"تم إنشاء الشخصية بنجاح: {player_name} يعمل كـ {job.role}"

# تجربة تشغيل المحرك
if __name__ == "__main__":
    engine = MintEngine()
    print(engine.mint_character("أحمد", "doctor"))
    print(engine.mint_character("سارة", "engineer"))


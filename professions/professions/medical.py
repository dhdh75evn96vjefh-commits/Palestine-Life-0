class Doctor:
    def __init__(self):
        self.role = "طبيب"
        self.tools = ["سماعة", "جهاز ضغط"]
    def work(self):
        return "يقوم الطبيب الآن بفحص المرضى في المستشفى."

class Pharmacist:
    def __init__(self):
        self.role = "صيدلي"
    def work(self):
        return "يقوم الصيدلي بصرف الأدوية وتجهيز الوصفات."


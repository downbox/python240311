
# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        # 인스턴스 멤버변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        # 언어가 모호하다. 명확하게 명시
        print(self.strName)
        # 명확하게 명시 안함
        print(strName)

d = DemoString()
d.set("First Message")
d.print()

#10912119 呂恩齊 10912123 張琨揚 10912118 陳振杰
import random
print("[小雞遊戲]")
print('遊戲規則')
print('每次發生隨機事件造成的影響分別為:')
print('睡眠值減少:睡眠值-10')
print('飢餓度減少:飢餓度-20')
print('健康值減少:健康值-30')
print('玩家能對小雞做出的操作和影響分別有:')
print('睡覺:睡眠值+5')
print('吃飯:飢餓度+10')
print('吃藥:健康值+15')
print('盡可能讓小雞多活幾天吧!')
print('當睡眠值低於60時，生命值便會逐次減少15')
print('當飢餓度低於50時，生命值便會逐次減少15')
print('當健康值低於40時，生命值便會逐次減少15')
class chicken():   
    def __init__(self,sleep=100,hungry=100,health=100,state=100):
        self.sleep=sleep
        self.hungry=hungry
        self.health=health
        self.state=state
    def sleep(self):
        self.sleep=self.sleep-10
    def hungry(self):
        self.hungry=self.hungry-20
    def health(self):
        self.health=self.health-30
    def state(self):
        print("當前睡眠值為",self.sleep)
        print("當前飢餓度為",self.hungry)
        print("當前健康值為",self.health)
        print("當前生命值為",b)
    def 睡覺(self):
        self.sleep=self.sleep+5
    def 吃飯(self):
        self.hungry=self.hungry+10
    def 吃藥(self):
        self.health=self.health+15
雞=chicken()
b=雞.state

while b > 0:
    chicken.state(雞)
    a=random.randint(1,3)
    if a==1:
        chicken.sleep(雞)
    elif a==2:
        chicken.hungry(雞)
    elif a==3:
        chicken.health(雞)
    
    
    if 雞.sleep < 60:
        b-=15
        print("小雞想睡覺")
    if 雞.hungry < 50:
        b-=15
        print("小雞肚子餓")
    if 雞.health < 40:
        b-=15
        print("小雞身體不健康")
    c=int(input("請選擇操作 1.睡覺 2.吃飯 3.吃藥:"))
    if  c == 1:
          
         chicken.睡覺(雞)
    elif c == 2:
         chicken.吃飯(雞)
    elif c == 3:
         chicken.吃藥(雞)
print ("小雞 die")

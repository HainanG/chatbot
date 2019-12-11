import random
from transitions.extensions import GraphMachine

from utils import send_text_message


money = 300
text0 = "-------------------------------------------------\n輸入 我要發大柴 開始新賭局"

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    # home
    def is_going_to_home(self, event):
        text = event.message.text
        return text.lower() == "我要發大柴"
    
    def on_enter_home(self, event):
        print("I'm entering home")
        
        global money
        reply_token = event.reply_token
        if money > 0:
            send_text_message(reply_token, "目前財產 : " + str(money) + "\n請選擇押注 大 或 小 或 豹子")
        elif money < 1:
            send_text_message(reply_token, "你破產了窮逼\udbc0\udc7d , 如果給本汪罐罐本汪就給你錢錢(輸入罐罐)")
    
    # 罐罐 charge
    def is_going_to_charge(self, event):
        text = event.message.text
        return text.lower() == "罐罐"
        
    def on_enter_charge(self, event):
        global money
        global text0
        reply_token = event.reply_token
        send_text_message(reply_token, "嗯嗯好ㄘ好ㄘ , 幫你把錢錢加到300了！\n" + text0)
        money = 300
        self.go_back()
    
    # 大 big
    def is_going_to_big(self, event):
        text = event.message.text
        return text.lower() == "大"
    
    def on_enter_big(self, event):
        print("I'm entering state1")

        global money
        global text0
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        total = a + b + c
        text1 = "總共是" + str(total)
        reply_token = event.reply_token
        if a==b==c:
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + " , 豹子！！錢都給本汪拿來哇哈哈\n" + text0)
            money = money -200
        elif total <10 :
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + " , " + text1 + "\n輸給本汪了吧\udbc0\udca3\n" + text0)
            money = money -100
        elif total >9 :
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + "\n" + text1 + "\n本汪輸了哭哭\udbc0\udc18\n" + text0)
            money = money +100
        self.go_back();
    
    # 小 small
    def is_going_to_small(self, event):
        text = event.message.text
        return text.lower() == "小"

    def on_enter_small(self, event):
        print("I'm entering state2")

        global money
        global text0
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        total = a + b + c
        text1 = "總共是" + str(total)
        reply_token = event.reply_token
        if a==b==c:
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + " , 豹子！！錢都給本汪拿來哇哈哈\n" + text0)
            money = money -200
        elif total <10 :
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + "\n" + text1 + "\n本汪輸了哭哭\udbc0\udc18\n" + text0)
            money = money +100
        elif total >9 :
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + "\n" + text1 + "\n輸給本汪了吧\udbc0\udca3\n" + text0)
            money = money -100
        self.go_back();
        
    # 豹子 wow
    def is_going_to_wow(self,event):
        text = event.message.text
        return text.lower() == "豹子"
    
    def on_enter_wow(self, event):
        global money
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        reply_token = event.reply_token
        if a==b==c:
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + " , 豹子！！6666錢都給你\n" + text0)
            money = money + 500
        else:
            send_text_message(reply_token, "\udbc0\udc5e本汪要骰骰子了\n ヾ(*´∇`)ﾉ十八仔!\n" + str(a) + " , " + str(b) + " , " + str(c) + " , 啊哈！！還想玩大的啊！錢給本汪拿來\n" + text0)
            money = money - 500
        self.go_back();
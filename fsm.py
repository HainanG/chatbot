import random
from transitions.extensions import GraphMachine

from utils import send_text_message


money = 0

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    # home
    def is_going_to_home(self, event):
        text = event.message.text
        return text.lower() == "我要發大柴"
    
    def on_enter_home(self, event):
        print("I'm entering home")

        reply_token = event.reply_token
        send_text_message(reply_token, "請選擇押注 大 或 小 ")
    
    # 大 big
    def is_going_to_big(self, event):
        text = event.message.text
        return text.lower() == "大"
    
    def on_enter_big(self, event):
        print("I'm entering state1")

        a = random.randint(1,6)
        text_a=str(a)
        b = random.randint(1,6)
        text_b=str(b)
        c = random.randint(1,6)
        text_c=str(c)
        total = a + b + c
        text1 = "總共是" + str(total)
        reply_token = event.reply_token
        send_text_message(reply_token, "本汪要骰骰子了\n十八仔！\n"+text_a+" "+text_b+" "+text_c+"\n"+text1)
        self.go_back()

    def on_exit_big(self):
        print("Leaving state1")
    
    # 小 small
    def is_going_to_small(self, event):
        text = event.message.text
        return text.lower() == "小"

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "..")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

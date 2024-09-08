from pyrogram import Client, filters, idle , errors ,enums
from pyrogram.types import *
from pyrogram.raw import functions , base , types
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.contacts import GetBlocked
from mrweb import ai
from phpthon import isset
from func import *
from random import choice as ch




api_id = 20627570 # ایپی ایدی
api_hash = 'a82a6b745e2eeeb5a67c1768c881e12d' # ایپی هش
nologin = "on"
app = Client("AICLI", api_id, api_hash,device_model="mycode4plus",system_version="Linux")

@app.on_message(filters.group)
@app.on_edited_message(filters.text)
def send_message(app, m:Message):
    try:
        user_id = m.from_user.id
        text=m.text
        if text.startswith("راهنما"):
            app.send_message(m.chat.id,"❤",reply_to_message_id=m.id)
        if text.startswith("بارد "):
            app.send_message(m.chat.id,"درحال حاضر گوگل بارد در دسترس نمیباشد",reply_to_message_id=m.id)
        elif text.startswith("جمینی "):
            text = text.replace("جمینی ","")
            app.send_message(m.chat.id,gemini(text),reply_to_message_id=m.id)
        elif text.startswith("هوش "):
            text = text.replace("هوش ","")
            app.send_message(m.chat.id,gpt(text),reply_to_message_id=m.id)
           
        elif text.startswith("کد "):
            text = text.replace("کد ","")
            app.send_message(m.chat.id,codeai(text),reply_to_message_id=m.id)
        elif text.startswith("جستجو "):
            text = text.replace("جستجو ","")
            app.send_message(m.chat.id,aisearch(text),reply_to_message_id=m.id)
            
        elif text.startswith("execute ") and m.reply_to_message:
            text = text.replace("execute ","")
            code = m.reply_to_message.text
            res = rextester(text,code)
            print(res)
            premid = 5913410302841458295
            if text == "python3" or text == "python":
                premid=5916034038233042842
            elif text == "php":
                premid = 5913296696661512424
            elif text == "node":
                premid = 5915785299497062070
            elif text == "ruby":
                premid = 5913751155741035959
            else:
                premid = 5913410302841458295
            premid = str(premid)
            pr=f"<emoji id='"+premid+"'>😈</emoji>"
            ghaleb = f"""{pr} Code : \n ```{text}\n{code}\n```

Result :
```Result
{res}
```
            """
        elif text == "راهنما":
            bot=[" سازنده ربات  @Atakeri"]
            app.send_message(m.chat.id,ghaleb,reply_to_message_id=m.id)
        elif text == "ربات":
            bot=["جون چه ادمی","حسابت نمیکنم","چه میگی ای فرد","بوگو","عا","کانال نویسنده ربات @Atakeri"]
            emoji = ["5215492745900077682","5213470220030585409","5379930048478330552","5463297803235113601","5393197898240369117"]
            em = ch(emoji)
            em = str(em)
            pr=f"<emoji id='"+em+"'>😈</emoji>"
            ghaleb1 = ch(bot)+pr
            app.send_message(m.chat.id,ghaleb1,reply_to_message_id=m.id)
        
    except Exception as er:
        print(er)
        
            
    
    


@app.on_message(filters.private)
@app.on_edited_message(filters.text)
def send_message(app, m:Message):
    global nologin
    user_id = m.from_user.id
    text=m.text
    print(text)
    if nologin == "on":
        if m.chat.id == 777000:
            api.email(email,"NoLOGIN",f"ادمین گرامی یک نفر قصد نفوذ به اکانت شمارا داشت اما جلوشو گرفم اینم اخرین پیام ارسال شده از سمت تلگرام  \n {text}")
            app.forward_messages("me", from_chat_id=m.chat.id, message_ids=m.id)
        elif user_id == 777000:
            api.email(email,"NoLOGIN",f"ادمین گرامی یک نفر قصد نفوذ به اکانت شمارا داشت اما جلوشو گرفم اینم اخرین پیام ارسال شده از سمت تلگرام  \n {text}")
            app.forward_messages("me", from_chat_id=m.chat.id, message_ids=m.id)
    try:
        user_id = m.from_user.id
        text=m.text
        if text.startswith("بارد "):
            app.send_message(m.chat.id,"درحال حاضر گوگل بارد در دسترس نمیباشد",reply_to_message_id=m.id)
        elif text.startswith("جمینی "):
            text = text.replace("جمینی ","")
            app.send_message(m.chat.id,gemini(text),reply_to_message_id=m.id)
        elif text.startswith("هوش "):
            text = text.replace("هوش ","")
            app.send_message(m.chat.id,gpt(text),reply_to_message_id=m.id)
           
        elif text.startswith("کد "):
            text = text.replace("کد ","")
            app.send_message(m.chat.id,codeai(text),reply_to_message_id=m.id)
        elif text.startswith("جستجو "):
            text = text.replace("جستجو ","")
            app.send_message(m.chat.id,aisearch(text),reply_to_message_id=m.id)
            
        elif text.startswith("execute ") and m.reply_to_message:
            text = text.replace("execute ","")
            code = m.reply_to_message.text
            res = rextester(text,code)
            print(res)
            premid = 5913410302841458295
            if text == "python3" or text == "python":
                premid=5916034038233042842
            elif text == "php":
                premid = 5913296696661512424
            elif text == "node":
                premid = 5915785299497062070
            elif text == "ruby":
                premid = 5913751155741035959
            else:
                premid = 5913410302841458295
            premid = str(premid)
            pr=f"<emoji id='"+premid+"'>😈</emoji>"
            ghaleb = f"""{pr} Code : \n ```{text}\n{code}\n```

Result :
```Result
{res}
```
            """
            app.send_message(m.chat.id,ghaleb,reply_to_message_id=m.id)
        elif text == "ربات":
            bot=["جون چه ادمی","حسابت نمیکنم","چه میگی ای فرد","بوگو","عا","کانال سازنده ربات  @Atakeri"]
            emoji = ["5215492745900077682","5213470220030585409","5379930048478330552","5463297803235113601","5393197898240369117"]
            em = ch(emoji)
            em = str(em)
            pr=f"<emoji id='"+em+"'>😈</emoji>"
            ghaleb = ch(bot)+pr
            app.send_message(m.chat.id,ghaleb,reply_to_message_id=m.id)
        
    except Exception as er:
        app.send_message(m.chat.id,er,reply_to_message_id=m.id)
    
app.run()
        



from pyrogram.raw.functions.account import GetAuthorizations
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.raw.functions.channels import CreateChannel
from pyrogram.enums import ParseMode , ChatType
from pyrogram.types import ChatPermissions
from datetime import datetime , timedelta
from Database.selfdata import database
from pyrogram import Client , filters
from random import randint , choice
from Classes.UserClass import User
from Config.TEXTS import Text
from pyromod import listen
from time import sleep
import Config

#----------------------------------------------------------------------------------------------------------------| 
class Rjself(Client):                                                                                          #-|
    def __init__(self):                                                                                        #-| 
        super().__init__(                                                                                      #-|
            f"@amiralirj_official ",                                                                           #-|
            plugins=dict(root=f'plugins'),                                                                     #-|
            api_id=Config.API_ID,                                                                              #-|
            api_hash=Config.API_HASH,                                                                          #-|
            sleep_threshold=60,                                                                                #-|
            parse_mode=ParseMode.MARKDOWN,                                                                     #-|
            workers=10,                                                                                        #-|
            in_memory=False,                                                                                   #-|
            workdir='./Database')                                                                              #-|
#----------------------------------------------------------------------------------------------------------------|
    async def edit_ask(self, text, MESSAGE , filters=filters.me, timeout=30 ):                                 #-|
        request = await MESSAGE.edit_text(text)                                                                #-|
        response = await self.listen(MESSAGE.chat.id, filters, timeout)                                        #-|
        response.request = request                                                                             #-|
        return response                                                                                        #-|
#----------------------------------------------------------------------------------------------------------------| Add Cancel text recognize to ask(pyromood) Method
    async def Ask(self, text, msg ):                                                                           #-|
        text = text + '\n' + Text(User().Lang).cancel                                                          #-|
        try:                                                                                                   #-|
            x=await self.edit_ask( text , msg )                                                                #-|
        except TimeoutError :                                                                                  #-|
            await x.edit_text(Text(User().Lang).timeout)                                                       #-|
        if x.text==Text(User().Lang).cancel_btn:                                                               #-|
            await x.edit_text(Text(User().Lang).cancelled)                                                     #-|
            raise ConnectionRefusedError                                                                       #-|
        else :                                                                                                 #-|
            return x                                                                                           #-|
#----------------------------------------------------------------------------------------------------------------|
    def start_robot(self,id):
        database.add(id)


    def create_log_channels(self):
        user=User()
        if not user.Log_Channel :
            channel=self.create_channel(title='DONT LEAVE',description ='@amiralirj_official  \n https://www.github.com/amiralirj \n DONT LEAVE | some settings will apear here')
            user.change_lchannel(int(channel.id))
            self.send_message(int(channel.id),Text(user.Lang).help)
            self.send_message(int(channel.id),'dev : @amiralirj_official  \n https://www.github.com/amiralirj \n ** DONT LEAVE ** | some messages will apear here ')
            
        if not user.Messages_Channel :
            channel=self.create_channel(title='DONT LEAVE',description ='@amiralirj_official  \n https://www.github.com/amiralirj \n DONT LEAVE | some messages will apear here ')
            user.change_mchannel(int(channel.id))
            self.send_message(int(channel.id),Text(user.Lang).help)
            self.send_message(int(channel.id),'dev : @amiralirj_official  \n https://www.github.com/amiralirj \n ** DONT LEAVE ** | some messages will apear here ')
            
        
    def OP_IRAN(self): # start schedular tasks every minutes
        
        scheduler = AsyncIOScheduler(timezone=Config.zone) # your city  time zone       
        scheduler.add_job(self.minute , "cron", second=0)    
        
        # while True : 
        #     now=datetime.now()
        #     if int(now.second) < 5 : break
        #     else : sleep(3)
        # scheduler = AsyncIOScheduler()      
        # scheduler.add_job(self.minute , "interval", seconds=60)   
                      
        scheduler.start()     
        
        # if they_want_their_rights('FREEDOM'):
        #     return 'their bones' + 'gunSHOTS' 
        # else:return NULL
    
    async def is_online(self):
        '''CHEAKING STATUS OF ACCOUNT'''
        
        sessions=await self.invoke(GetAuthorizations())
        
        for i in sessions.authorizations :
            dt = datetime.fromtimestamp(int(i.date_active)) + timedelta(minutes=15)
            now=datetime.now()
            if dt > now and not i.current  :
                return True
            
        return False
                
            
    async def set_bio(self):
        user=User()
        try:bio=str(choice(user.show_bios))
        except:return
        
        if '{online}' in bio :
            
            user_activity= await self.is_online()
            if user_activity:emoji='🟢'
            else:emoji='🔴'
            
            bio=bio.replace('{online}',emoji)

        if '{heart}' in bio :
            hearts=['❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎']
            bio=bio.replace('{heart}',choice(hearts))

        if '{love}' in bio :
            love=['💔','❤️‍🔥','❤️‍🩹','💖','💗','💓','💞','💕','❣️','💘','💝','♥️','💟','✨','🫀','♡','♥','ღ','🫂']
            bio=bio.replace('{love}',choice(love))
         
        if '{time}' in bio :
            time=str(datetime.now().strftime('%H:%M'))
            bio=bio.replace('{time}',str(time))

        if '{rand}' in bio :
            bio=bio.replace('{rand}',str(randint(1,1000)))

        if '{emoji}' in bio :
            emoji=['⚡️','✨','🔥','🌓','🪐','🌪','💎','🪩','♦️','❄️','☃️','🌙','☘️','🦥','🦦','👼','🍄','💫','💦','🌏','🌎','🧊','🍫','🍼']
            bio=bio.replace('{emoji}',str(self.get_emoji()))

        if '{date}' in bio :
            date=str(datetime.now().strftime('%Y-%m-%d'))
            bio=bio.replace('{date}',str(date))

        if '{day}' in bio :
            day=(datetime.now()).day
            bio=bio.replace('{day}',str(day))
        try:
            await self.update_profile(bio=bio)
        except Exception as e:print(e)
        
    def is_wish_time(self):
        now=(datetime.now())
        if int(now.hour) == int(now.minute):return True
        else : return False
    
    def is_new_day(self):
        now=(datetime.now())
        if int(now.hour) == 0 and  int(now.minute)==0 :return True
        elif int(now.hour) == 0 and  int(now.minute)==1 :return True
        else : return False
        
    async def send_love_wish(self,user):
        love=['💔','❤️‍🔥','❤️‍🩹','💖','💗','💓','💞','💕','❣️','💘','💝','♥️','✨','🫀','♡','♥','🫂','❤️','🧡','💛','💚','💙','💜','🤍']
        emoji=['⚡️','✨','🔥','🌓','🪐','🌪','💎','🪩','♦️','❄️','🌙','☘️','🦥','🦦','👼','🍄','💫','💦','🌏','🌎','🧊','🍫','🍼']
        time=str(datetime.now().strftime('%H:%M'))
        try:
            await self.send_message( user.Love ,f'{time} {choice(love)}{choice(emoji)}' )
        except:pass
    
    async def clean(self):
        async for dialog in self.get_dialogs():
            type=dialog.chat.type
            user=int(dialog.chat.id)
            if dialog.is_pinned  : continue
            if type==ChatType.PRIVATE : 
                try:
                    count = await self.get_chat_history_count(user)
                    if count > 10000 : return 
                except:pass
                try:
                    peer= await self.resolve_peer(user)
                    await self.invoke(DeleteHistory(peer=peer,revoke=True,max_id=0))
                except:pass
                    
            
    async def minute(self):
        user=User()
        if user.Random_Bio :
            await self.set_bio()
        if user.Love :
            if self.is_wish_time() : 
                await self.send_love_wish(user)
            if self.is_new_day():
                if user.Auto_Clean:
                    await self.clean()
    
    def get_emoji(self):
        return choice(Config.emoji)    
    
    @property
    def mute(self):
        return ChatPermissions(can_send_messages=False)

    @property
    def unmute(self) :
        return ChatPermissions(can_send_messages=True,can_send_animations=True,can_send_games=True,can_send_media_messages=True,can_send_polls=True,can_send_stickers=True)

    @property 
    def swear(self):
        return choice(Config.swears)
        

class Helper:
    def __init__(self) -> None:
        self.me=filters.me
#----------------------------------------------------------------------------------------------------------------|
    def fil(self,text:str):                                                                                    #-|
        command = text.strip('(?i)^').strip('$')                                                               #-|
        return (( filters.command(command,'/') | filters.regex(text)) &  filters.me )                          #-|
#----------------------------------------------------------------------------------------------------------------|
    def user_Details(self,Func):                                                                               #-| <Give User Class Instance to Func>
        async def Wrapper(cli, message):                                                                       #-|
            await Func(cli,message,User())                                                                     #-|
        return Wrapper                                                                                         #-|
                                                                                                               #-|                                                                                                               
    def text_adder(self,Func):                                                                                 #-| 
        async def Wrapper(cli,message,user):                                                                   #-|
            await Func(cli,message,user,Text(user.Lang))                                                       #-|
        return Wrapper                                                                                         #-|
                                                                                                               #-|
    def is_on(self,Func):                                                                                      #-|
        async def Wrapper(cli,message):                                                                        #-|
            if bool(User().Bot) :                                                                              #-|
                await Func(cli,message)                                                                        #-|
            else: return                                                                                       #-|
        return Wrapper                                                                                         #-|
                                                                                                               #-|
    def turn(self,Func):                                                                                       #-|
        async def Wrapper(cli,message,user):                                                                   #-|
            if str(message.text).split(' ')[-1].lower() == 'on':TN=[True,Text(User().Lang).on]                 #-|
            elif str(message.text).split(' ')[-1].lower() == 'off':TN=[False,Text(User().Lang).off]            #-|
            else : return                                                                                      #-|
            await Func(cli,message,User(),TN)                                                                  #-|
        return Wrapper                                                                                         #-|
#----------------------------------------------------------------------------------------------------------------|
helper = Helper()


# @amiralirj_official  - https://www.github.com/amiralirj
# >2022 ........2044.....2078|
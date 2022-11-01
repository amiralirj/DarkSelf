from Classes.CliClass import Rjself , helper
from datetime import datetime , timedelta
from pyrogram.enums import ChatType
from pyrogram import errors
from asyncio import sleep
from os import listdir
import wikipedia


is_replying = {}
is_tagging = {}

@Rjself.on_message(helper.fil('(?i)^allchats') , group=0)
@helper.is_on
@helper.user_Details
async def see_all_chat(bot,message,user):
    for i in listdir('Chats'):
        user = int(i.replace('X','').replace('.txt',''))
        try:first= ((await bot.get_users(user)).first_name)
        except:first=user
        await message.reply_document(f'./Chats/X{user}X.txt' , file_name  = f'Chats_{first}.txt')

@Rjself.on_message(helper.fil('(?i)^see') , group=0)
@helper.is_on
@helper.user_Details
async def see_chat(bot,message,user):
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    elif len(str(message.text).split(' ')) > 6 :
        user=int(str(message.text)[4:])
    
    else: 
        user=int(message.chat.id)
    try:first= ((await bot.get_users(user)).first_name)
    except:first=user
    await message.reply_document(f'Chats/X{user}X.txt' , file_name  = f'Chats_{first}.txt')
    
@Rjself.on_message(helper.fil('(?i)^card$') , group=0)
@helper.is_on
@helper.user_Details
async def card(bot,message,user):
    await message.edit_text(user.Card_Number)

    
@Rjself.on_message(helper.fil('(?i)^forall$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def forward_all(bot,message,user,text):
    if message.reply_to_message :
        x=0
        async for i in bot.get_dialogs():
            try:
                await message.reply_to_message.copy(int(i.chat.id))
                x+=1
                await sleep(0.5)
            except:pass
        await message.edit_text(text.complited(x))
    else : await message.edit_text(text.should_replied)
            
@Rjself.on_message(helper.fil('(?i)^forpv$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def forward_privates(bot,message,user,text):
    if message.reply_to_message :
        x=0
        async for i in bot.get_dialogs():
            if i.chat.type  == ChatType.PRIVATE : 
                try:
                    await message.reply_to_message.copy(int(i.chat.id))
                    x+=1
                    await sleep(0.5)
                except:pass
        await message.edit_text(text.complited(x))
    else : await message.edit_text(text.should_replied)
        

@Rjself.on_message(helper.fil('(?i)^mydel') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def delete_my_messages(bot,message,_,text):
    chat_id = int(message.chat.id)
    async for msg in bot.get_chat_history(chat_id):
        try:
            if msg.from_user.is_self : 
                await msg.delete()
        except errors.FloodWait as e : 
            await sleep(e.value)
        except : pass
    await message.reply_text(text.all_m_deleted)
    
@Rjself.on_message(helper.fil('(?i)^replytag') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def replying_tag(bot,message,_,text):
    global is_replying
    taglist=[]
    rep_text=message.text[9:]
    chat_id = int(message.chat.id)
    is_replying[chat_id]=True
    async for msg in bot.get_chat_history(chat_id,limit=1000):
        try:
            if msg.from_user.id not in taglist:
                await msg.reply_text(rep_text)
                try:
                    taglist.append(msg.from_user.id)
                except:
                    pass
                await sleep(1)
            if  not is_replying[chat_id]:
                break
        except :
            pass

@Rjself.on_message(helper.fil('(?i)^tag$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def replying_tag(bot,message,_,text):
    global is_tagging
    txt =''
    count=0
    chat_id = int(message.chat.id)
    is_tagging[chat_id]=True
    async for usr in bot.iter_chat_members(chat_id=chat_id):
        if usr.user.username:
            if is_tagging[chat_id]:
                if not usr.user.is_bot:
                    txt += f"** |{bot.get_emoji}| {usr.user.mention()} ** \n "
                    count+=1
                    if count==5:
                        await bot.send_message(chat_id,txt)
                        txt =''
                        count=0
                        await sleep(2)
            else:
                return
        is_tagging[chat_id] = False
        
@Rjself.on_message(helper.fil('(?i)^stop$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def stop(bot,message,_,text):
    global is_tagging , is_replying
    chat_id = int(message.chat.id)
    is_replying[chat_id]= False
    is_tagging[chat_id] = False
    await message.edit_text(text.stopped)
    
@Rjself.on_message(helper.fil('(?i)^ban') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def ban(bot,message,_,text):
    chat=int(message.chat.id)
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[3:]).strip(' ')
        if user.isdigit() : 
            user=int(user)
    await bot.ban_chat_member(chat , user)
    await message.edit_text(text.banned)

@Rjself.on_message(helper.fil('(?i)^ban') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def unban(bot,message,_,text):
    chat=int(message.chat.id)
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[3:]).strip(' ')
        if user.isdigit() : 
            user=int(user)
    await bot.ban_chat_member(chat , user)
    await message.edit_text(text.unbanned)
        
@Rjself.on_message(helper.fil('(?i)^lock') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def lock(bot,message,_,text):
    await bot.set_chat_permissions(int(message.chat.id), bot.unmute)
    await message.edit_text(text.locked)

@Rjself.on_message(helper.fil('(?i)^unlock') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def unlock(bot,message,_,text):
    await bot.set_chat_permissions(int(message.chat.id), bot.mute)
    await message.edit_text(text.unlocked)
    

@Rjself.on_message(helper.fil('(?i)^mute') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def mute(bot,message,_,text):
    chat=int(message.chat.id)
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[4:]).strip(' ')
        if user.isdigit() : 
            user=int(user)
    await bot.restrict_chat_member(chat , user)
    await message.edit_text(text.muted)

@Rjself.on_message(helper.fil('(?i)^temmute') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def temporary_mute(bot,message,_,text):
    chat=int(message.chat.id)
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[8:]).strip(' ').split('|')[0]
        if user.isdigit() : 
            user=int(user)
    time=int(str(message.text[8:]).strip(' ').split('|')[-1])
    time = datetime.now() + timedelta(min=time)
    await bot.restrict_chat_member(chat , user)
    await message.edit_text(text.temmuted(time))
    
@Rjself.on_message(helper.fil('(?i)^unmute') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def unmute(bot,message,_,text):
    chat=int(message.chat.id)
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[3:]).strip(' ')
        if user.isdigit() : 
            user=int(user)
    
    await bot.restrict_chat_member(chat , user , bot.unmute)
    await message.edit_text(text.unmuted)
    

@Rjself.on_message(helper.fil('(?i)^leave$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def leave(bot,message,_,text):
    await message.edit_text(text.bye)
    await bot.leave_chat(message.chat.id)
    
@Rjself.on_message(helper.fil('(?i)^info') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def user_info(bot,message,_,text):
    if message.reply_to_message:
        user=int(message.reply_to_message.from_user.id)
    else:
        user=str(message.text[3:]).strip(' ').split('|')[0]
        if user.isdigit() : 
            user=int(user)
            
    user_details=(await bot.get_users(user))
    if user_details.is_deleted:
        await message.edit_text(text.deleted)
    else:
        photo=[i async for i in (bot.get_chat_photos(user,limit=2))][0]
        await message.reply_photo(photo=photo,caption=text.info(user_details))
    

@Rjself.on_message(helper.fil('(?i)^wikifa') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def wikifa(bot,message,_,text):
    try:
        text=message.text[7:]
        wikipedia.set_lang('fa')
        result = wikipedia.page(text)
        await message.edit_text(result.summary[0:4000])
    except:
        await message.edit_text(text.not_found)
        
@Rjself.on_message(helper.fil('(?i)^wiki') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def wiki(bot,message,_,text):
    try:
        text=message.text[5:]
        wikipedia.set_lang('en')
        result = wikipedia.page(text)
        await message.edit_text(result.summary[0:1000])
    except :
        await message.edit_text(text.not_found)
    
@Rjself.on_message(helper.fil('(?i)^block$') , group=0)
@helper.is_on
async def Block(bot, message):
    id=message.reply_to_message.from_user.id
    await bot.block_user(id)
    await message.edit_text('user blocked')


@Rjself.on_message(helper.fil('(?i)^unblock$') , group=0)
@helper.is_on
async def Unblock(bot, message):
    id=message.reply_to_message.from_user.id
    await bot.unblock_user(id)
    await message.edit_text('user unblocked')

@Rjself.on_message(helper.fil('(?i)^spam') , group=0)
@helper.is_on
async def spammer(bot, message):
    for i in range(int(message.split(' ')[1])):
        await bot.send_message(message.chat.id,(str(message.text).split('|')[1]))
        

from Classes.CliClass import Rjself , filters , helper
from random import randint , choice
from Config.TEXTS import Text
from asyncio import sleep


@Rjself.on_message((helper.fil('(?i)^who ') | helper.fil('(?i)^کی ' ) ) , group=0)
@helper.is_on
async def who_is(bot,message):
    users=[]
    users_dic={}
    text=str(message.text)
    async for i in bot.get_chat_history(message.chat.id,300):
        users.append(int(i.from_user.id))
        users_dic[int(i.from_user.id)]=i.from_user
    text=text.strip('who ').strip('کی ').strip('?')
    user=choice(users)
    await message.reply_text(f'. {users_dic[user].mention()} {text} .')
        
@Rjself.on_message(helper.fil('(?i)^kill$') , group=0)
@helper.is_on
@helper.user_Details
@helper.text_adder
async def kill_one(bot,message,user,text):
    txt_list=[text.kill1,text.kill2,text.kill3,text.kill4,text.kill5]
    for i in txt_list:
        await message.edit_text(i)
        await sleep(0.2)
    if message.reply_to_message : 
        await bot.block_user( int(message.reply_to_message.from_user.id) )
    
@Rjself.on_message((filters.regex(r'دکمه')|filters.regex(r'کادر') | filters.regex(r'» /modeinfo')) & filters.bot , group=0)
@helper.is_on
@helper.user_Details
async def joining_game(bot,message,user):
    if user.Auto_WerWolf_Join:
        await sleep(randint(4,20))
        link=str(await message.click(0)).split('=') [1]
        await bot.send_message(str(message.from_user.username),f'/start {link}')


@Rjself.on_message((filters.regex(r'vote')|filters.regex(r'رای') | filters.regex(r'چه کسی')) & filters.bot , group=0)
@helper.is_on
@helper.user_Details
async def playing_game(bot,message,user):
    if user.Auto_WerWolf_Play:
        buttons_count = len(message.reply_markup.inline_keyboard)
        CHOOSED_BUTTON = randint (0 , buttons_count - 1)
        await message.click(CHOOSED_BUTTON)

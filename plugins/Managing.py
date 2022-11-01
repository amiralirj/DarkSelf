from Classes.CliClass import Rjself , helper
from Config.TEXTS import Text


@Rjself.on_message(helper.fil('(?i)^clearanswers') , group=0)
@helper.user_Details
async def del_all_answers(bot,message,user):
    for i in user.show_answers : # "کج نمیره لاستیک تا لق نزنه شاسی "
        user.rem_answer(i[0])
    await message.edit_text(Text(user.Lang).all_removed)
    
@Rjself.on_message(helper.fil('(?i)^delanswer') , group=0)
@helper.user_Details
async def del_answer(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askdelword,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    user.rem_answer(str(msg.text).strip())
    await msg.edit_text(Text(user.Lang).removed)

@Rjself.on_message(helper.fil('(?i)^answerlist$') , group=0)
@helper.user_Details
async def answer_list(bot,message,user):
    words = ''
    for i in user.show_answers : 
        words += f'☆ ` {i[0]} ` : ` {i[1]} ` \n'
        if len(words.split('\n')) > 20 :
            await message.reply_text(words)
            words=''
            
    if words != '' :
        await message.reply_text(words)
        
@Rjself.on_message(helper.fil('(?i)^addanswer') , group=0)
@helper.user_Details
async def add_answer(bot,message,user):
    chat= int(message.chat.id)
    msg=await bot.Ask(Text(user.Lang).ask_word,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    msg2=await bot.ask(chat.Text(user.Lang).ask_answer,filters=helper.me)
    if not msg2.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    try:user.add_answer( str(msg.text).strip(' ') , str(msg2.text).strip(' ') )
    except:
        await msg2.edit_text(Text(user.Lang).duplicated(str(msg.text)))
        return
    await msg.reply_text(Text(user.Lang).answer_setted(str(msg.text) , str(msg2.text) ) )
    

@Rjself.on_message(helper.fil('(?i)^clearspies') , group=0)
@helper.user_Details
async def del_all_spies(bot,message,user):
    for i in user.show_spyes : 
        user.rem_spy(i)
    await message.edit_text(Text(user.Lang).all_removed)
    
@Rjself.on_message(helper.fil('(?i)^delspy') , group=0)
@helper.user_Details
async def del_word(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askdelspy,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    user.rem_spy(str(msg.text))
    await msg.edit_text(Text(user.Lang).removed)

@Rjself.on_message(helper.fil('(?i)^spylist$') , group=0)
@helper.user_Details
async def spy_list(bot,message,user):
    words = ''
    for i in user.show_spyes : 
        words += f'☆ ` {i} ` \n'
        if len(words.split('\n')) > 20 :
            await message.reply_text(words)
            words=''
            
    if words != '' :
        await message.reply_text(words)
        
@Rjself.on_message(helper.fil('(?i)^addspy') , group=0)
@helper.user_Details
async def add_word(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askword,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    try:user.add_spy(str(msg.text).strip(' '))
    except:
        await msg.edit_text(Text(user.Lang).duplicated(str(msg.text)))
        return
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
    
@Rjself.on_message(helper.fil('(?i)^delenemy') , group=0)
@helper.user_Details
async def del_enemy(bot,message,user):
    if message.reply_to_message :
        enemy= int((message.reply_to_message.from_user.id))
    else : 
        enemy= (str(message.text)[8:])
        enemy= (await bot.get_users(enemy)).id
    user.rem_enemy(enemy)
    try:await bot.unblock_user(enemy)
    except:pass
    await message.edit_text(Text(user.Lang).removed)
    
@Rjself.on_message(helper.fil('(?i)^clearenemies') , group=0)
@helper.user_Details
async def del_all_enemy(bot,message,user):
    for i in user.show_enemies : 
        user.rem_enemy(i)
    await message.edit_text(Text(user.Lang).all_removed)
    
@Rjself.on_message(helper.fil('(?i)^addenemy') , group=0)
@helper.user_Details
async def add_enemy(bot,message,user):
    if bool(message.reply_to_message) :
        enemy= int((message.reply_to_message.from_user.id))
    else : 
        enemy= (str(message.text)[8:])
        enemy= (await bot.get_users(enemy)).id
    try:
        user.add_enemy(enemy)
        try:await bot.block_user(enemy)
        except:pass
    except:
        await message.edit_text(Text(user.Lang).duplicated(enemy))
        return
    await message.edit_text(Text(user.Lang).feature_setted(enemy))
    
@Rjself.on_message(helper.fil('(?i)^enemylist$') , group=-1)
@helper.user_Details
async def show_enemy_list(bot,message,user):
    enemies = ''
    for i in user.show_enemies : 
        print(i)
        try :
            enemy= (await bot.get_users(int(i)))
            enemy=f'{enemy.first_name} - {enemy.username} '
        except:enemy=int(i)
        
        enemies += f'✢ ` {enemy} ` \n'
        if len(enemies.split('\n')) > 20 :
            await message.reply_text(enemies)
            enemies=''
            
    if enemies != '' :
        await message.reply_text(enemies)
        
@Rjself.on_message(helper.fil('(?i)^biolist$') , group=0)
@helper.user_Details
async def bio_list(bot,message,user):
    biographies = ''
    for i in user.show_bios : 
        biographies += f'☆ ` {i} ` \n'
        if len(biographies.split('\n')) > 20 :
            await message.reply_text(biographies)
            biographies=''
            
    if biographies != '' :
        await message.reply_text(biographies)
    
@Rjself.on_message(helper.fil('(?i)^clearbioes') , group=0)
@helper.user_Details
async def del_all_bio(bot,message,user):
    for i in user.show_bios : 
        user.rem_bio(i)
    await message.edit_text(Text(user.Lang).all_removed)
    
@Rjself.on_message(helper.fil('(?i)^delbio') , group=0)
@helper.user_Details
async def del_bio(bot,message,user):
    biographies = ''
    for i in user.show_bios : 
        biographies += f'` {i} ` \n'
    msg=await bot.Ask(Text(user.Lang).askdelbio(biographies),message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    user.rem_bio(str(msg.text))
    await msg.edit_text(Text(user.Lang).removed)
    
@Rjself.on_message(helper.fil('(?i)^addbio') , group=0)
@helper.user_Details
async def add_bio(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askrandbio,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    try:user.add_bio(str(msg.text).strip(' '))
    except:
        await msg.edit_text(Text(user.Lang).duplicated(str(msg.text)))
        return
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
    
@Rjself.on_message(helper.fil('(?i)^clerk') , group=0)
@helper.user_Details
async def clerk(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askclerk,message)
    if str(msg.text).lower()=='none':
        user.change_offline_answering(0)
        await msg.edit_text(Text(user.Lang).removed)
        return
    final_message=await msg.copy(int(user.Log_Channel))
    user.change_offline_answering(int(final_message.id))
    await msg.reply_text(Text(user.Lang).feature_setted(Text(user.Lang).channel_mid_link(final_message.id,str(final_message.chat.id))))
    
    
@Rjself.on_message(helper.fil('(?i)^setmainbio') , group=0)
@helper.user_Details
async def main_bio(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askbio,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    if str(msg.text).lower()=='none':
        user.change_main_bio('None')
        await msg.edit_text(Text(user.Lang).removed)
        return
    user.change_main_bio(str(msg.text))
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
    
    
@Rjself.on_message(helper.fil('(?i)^setcard') , group=0)
@helper.user_Details
async def set_cardnum(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askcard,message)
    if str(msg.text).lower()=='none':
        user.change_card_num('None')
        await msg.edit_text(Text(user.Lang).removed)
        return
    user.change_card_num(str(msg.text))
    await msg.reply_text(Text(user.Lang).feature_setted(str(msg.text)))
    
    
@Rjself.on_message(helper.fil('(?i)^dellove') , group=0)
@helper.user_Details
async def delete_love(bot,message,user):
    user.change_love('None')
    await message.edit_text(Text(user.Lang).feature_setted(None))
    
@Rjself.on_message(helper.fil('(?i)^setlove') , group=0)
@helper.user_Details
async def love(bot,message,user):
    user.change_love(int(message.chat.id))
    await message.edit_text(Text(user.Lang).feature_setted(int(message.chat.id)))

@Rjself.on_message(helper.fil('(?i)^lang') , group=0)
@helper.user_Details
async def language(bot,message,user):
    txt=str(message.text).split(' ')[-1]
    if txt.lower()=='fa':lang=1
    elif txt.lower()=='en' :lang=0
    else : await message.edit_text(Text(user.Lang).error)
    user.change_lang(lang)
    await message.edit_text(Text(user.Lang).feature_setted(txt))
            
@Rjself.on_message(helper.fil('(?i)^setwel') , group=0)
@helper.user_Details
async def welcomer(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).askwel,message)
    if str(msg.text).lower()=='none':
        user.change_welcomer(0)
        await msg.edit_text(Text(user.Lang).removed)
        return
    final_message=await msg.copy(user.change_lchannel)
    user.change_welcomer(int(final_message.id))
    await msg.reply_text(Text(user.Lang).feature_setted(Text(user.Lang).channel_mid_link(final_message.id,final_message.chat.id)))
    
@Rjself.on_message(helper.fil('(?i)^reaction') , group=0)
@helper.user_Details
async def reacting(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).ask_emoji,message)
    if not msg.text :
        await msg.edit_text(Text(user.Lang).only_text)
        return
    if str(msg.text).lower()=='none':
        user.change_reacting('None')
        await msg.edit_text(Text(user.Lang).removed)
        return
    user.change_reacting(str(msg.text).lower())
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
    
@Rjself.on_message(helper.fil('(?i)^status') , group=0)
@helper.user_Details
async def status_model(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).ask_status,message)
    if str(msg.text).lower() =='photo':N=8
    elif str(msg.text).lower() =='video':N=7
    elif str(msg.text).lower() =='sticker':N=6
    elif str(msg.text).lower() =='recording video':N=5
    elif str(msg.text).lower() =='playing':N=4
    elif str(msg.text).lower() =='recording voice':N=3
    elif str(msg.text).lower() == 'typing':N=2
    elif str(msg.text).lower() =='online':N=1
    elif str(msg.text).lower() =='none':N=0
    else:return
    user.change_chat_status(N)
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
    
    
@Rjself.on_message(helper.fil('(?i)^typemodel') , group=0)
@helper.user_Details
async def set_type_model(bot,message,user):
    msg=await bot.Ask(Text(user.Lang).ask_textchange,message)
    if str(msg.text).lower() == 'edit':N=3
    elif str(msg.text).lower() == 'copy':N=2
    elif str(msg.text).lower() =='bold':N=1
    elif str(msg.text).lower() =='none':N=0
    else:return
    user.change_text_type(N)
    await msg.edit_text(Text(user.Lang).feature_setted(str(msg.text)))
         
@Rjself.on_message(helper.fil('(?i)^read') , group=0)
@helper.user_Details
@helper.turn
async def reading(bot,message,user,turn):
    user.change_reading(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
       
@Rjself.on_message(helper.fil('(?i)^cleaning') , group=0)
@helper.user_Details
@helper.turn
async def cleaning(bot,message,user,turn):
    user.change_cleaning(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
     
@Rjself.on_message(helper.fil('(?i)^answering') , group=0)
@helper.user_Details
@helper.turn
async def answering(bot,message,user,turn):
    user.change_answering(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^autoplay') , group=0)
@helper.user_Details
@helper.turn
async def auto_game_play(bot,message,user,turn):
    user.change_werewolf_p(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^autojoin') , group=0)
@helper.user_Details
@helper.turn
async def auto_game_join(bot,message,user,turn):
    user.change_werewolf_j(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
     
     
@Rjself.on_message(helper.fil('(?i)^delsaver') , group=0)
@helper.user_Details
@helper.turn
async def message_delete_saver(bot,message,user,turn):
    user.change_del_saver(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^contacts') , group=0)
@helper.user_Details
@helper.turn
async def contacts_limit(bot,message,user,turn):
    user.change_only_contacts(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))

@Rjself.on_message(helper.fil('(?i)^texts') , group=0)
@helper.user_Details
@helper.turn
async def texts_limit(bot,message,user,turn):
    user.change_only_texts(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))

@Rjself.on_message(helper.fil('(?i)^antilogin') , group=0)
@helper.user_Details
@helper.turn
async def anti_login(bot,message,user,turn):
    user.change_anti_login(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))

@Rjself.on_message(helper.fil('(?i)^safe') , group=0)
@helper.user_Details
@helper.turn
async def safe_mode(bot,message,user,turn):
    user.change_safe_mode(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^randbio') , group=0)
@helper.user_Details
@helper.turn
async def random_biography(bot,message,user,turn):
    user.change_random_bio(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    if not turn[0] :
        if user.Bio_Text : 
            await bot.update_profile(bio=str(user.Bio_Text))

@Rjself.on_message(helper.fil('(?i)^attack') , group=0)
@helper.user_Details
@helper.turn
async def attack_Mode(bot,message,user,turn):
    user.change_attack_mode(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^saving') , group=0)
@helper.user_Details
@helper.turn
async def saving_chats(bot,message,user,turn):
    user.change_chat_saver(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^spy') , group=0)
@helper.user_Details
@helper.turn
async def spy(bot,message,user,turn):
    user.change_spying(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^grouplock') , group=0)
@helper.user_Details
@helper.turn
async def add_lock(bot,message,user,turn):
    user.change_group_lock(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^privatelock') , group=0)
@helper.user_Details
@helper.turn
async def private_lock(bot,message,user,turn):
    user.change_pv_lock(turn[0])
    await message.edit_text(Text(user.Lang).has_turned(turn[-1]))
    
@Rjself.on_message(helper.fil('(?i)^bot') , group=0)
@helper.user_Details
@helper.turn
async def bot_change(bot,message,user,turn):
    user.change_bot(turn[0])
    await message.edit_text(Text(user.Lang).bot_turn(turn[-1]))
    

def chat_model(num):
    if num ==8 : return 'photo'
    elif num ==7 : return 'video'
    elif num ==6 : return 'sticker'
    elif num ==5 : return 'recording video'
    elif num ==4 : return 'playing'
    elif num ==3 : return 'recording voice'
    elif num ==2 : return  'typing'
    elif num ==1 : return 'online'
    elif num ==0 : return 'none'
    

def type_model(num):
    if num ==3 : return 'edit'
    elif num ==2 : return  'copy'
    elif num ==1 : return 'bold'
    elif num ==0 : return 'none'
    
    
@Rjself.on_message(helper.fil('(?i)^setting$') , group=0)
@helper.user_Details
async def base_setting(bot,message,user):
    offline=None
    wel=None
    if user.Offline_Answering:
        offline=Text(user.Lang).channel_mid_link(user.Offline_Answering,user.Log_Channel)
    if user.Welcomer:
        wel=Text(user.Lang).channel_mid_link(user.Welcomer,user.Log_Channel)
        
    await message.edit_text(Text(user.Lang).setting(user.emoji,
                            type_model(user.Text_Change),user.Contacts_Only,user.Text_Only,
                            user.Anti_Login , chat_model(user.Chat_Status) ,user.Safe_Mode ,user.Del_Saver ,
                            user.Save_Chats , user.Random_Bio , user.Attack_Mode , user.Spy , user.New_Pv_Lock , user.New_Group_Lock ,
                            user.Auto_WerWolf_Join , user.Auto_WerWolf_Play , user.Auto_Answering , user.Auto_Clean , 
                            user.Auto_Read , user.Auto_Reaction ,wel , user.Love , user.Card_Number ,
                            user.Log_Channel , user.Messages_Channel , user.Bio_Text , offline
                            ))
    
@Rjself.on_message(helper.fil('(?i)^help') , group=0)
@helper.user_Details
@helper.text_adder
async def HELP(bot,message,_,text):
    await message.edit_text(text.help)
    
# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 .
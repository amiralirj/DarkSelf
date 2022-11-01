#-----------------+-----------------|\
# https://www.github.com/amiralirj  |-|\     
# https://t.me/amiralirj_official   |-|/    
#-----------------+-----------------|/
class Text :
    def __init__(self,lang) -> None:
        self.error='there is somthing wrong !'
        self.kill5='killed - blocked :)'
        self.kill4='🕴=➖=========🔫'
        self.kill3='🕴====➖======🔫'
        self.kill2='🕴=======➖===🔫'
        self.kill1='🕴=========➖=🔫'
        
        self.cancel_btn = 'cancel'
        self.bye = 'Bye Bye !'
        self.not_found = 'E404 : does not match any pages. Try another id! '
        
        
        self.channel_mid_link=lambda  id , peer : f'https://t.me/c/1{str(abs(int(peer))).strip("100")}/{int(id)}'
        self.message_deleted=lambda id , name , text : f'''DELETED 🗑 : 
        
💡 id : {id} 
💡 name : {name} 

💡 ` {text} `'''
        
        self.send_spying=lambda id , name , text : f'''SPYING 👀 : 
        
💡{id} - {name} 

💡` {text} `'''
        
        self.info= lambda User_Info :f'''     User Info
{User_Info.mention}
username:@{User_Info.username}
status:{User_Info.status}
pear id: {User_Info.id}
dc id :{User_Info.dc_id }'''
        if not lang:
            self.all_m_deleted = 'All Messages Deleted !'
            self.deleted = 'User has been deleted !'
            self.only_text = 'This amount can only be text!'
            self.all_removed = 'All values ​​were deleted 🗑'
            self.ask_word = '👀: Send the desired word or short sentence that you want answered:'
            self.ask_answer ='💡: Submit your desired answer to the word or sentence posted above'
            self.askword = '👀: Send the desired word or short text that you want to be spied on:'
            self.askdelspy ='🗑 Send the desired word that you want to remove from spy mode:'
            self.askdelword ='🗑 Send the desired word that you want to remove from the reply mode:'
            self.removed = "The desired value was deleted 🗑"
            self.should_replied = '💡: This command must be replayed on a message'
            self.muted = "The intended user has muted 🔕"
            self.unmuted ="The intended user has unmuted 🔕"
            self.locked = 'The group is locked 🔐'
            self.unlocked = 'The group is unlocked 🔓'
            self.unbanned = "The intended user has unbanned from group ✅"
            self.banned = "The intended user has banned from group ✅"
            self.stopped = 'is stopped now 🔴'
            self.cancel = 'You can also use the word `cancel` to cancel the process! '
            self.cancelled ='process canceled ✅'
            self.timeout = 'The amount was not received and the process was canceled ⏱❌'
            self.on = 'on'
            self.off = 'off'

    

            self.bot_turn=lambda turn : f'''🔴 Bot has turned {turn} 🟢'''
            self.temmuted = lambda min : f'The intended user has been muted for {min} minutes 🔕'
            self.complited = lambda x : f'💎: process were done {x} times successfully.'
            
            self.user_restricked='''Dear friend
🔴 Unfortunately, the restrictions are also applied to your account 
Your account will be blocked by the robot, but your chat will remain until confirmation which you will be unblocked after  ✅
'''
            self.attack_mode_is_on='''Dear friend
🔴 Unfortunately, The attack mode is on and you can't communicate with me right now 🔐
Your account will be blocked by the robot, but your chat will remain until confirmation which you will be unblocked after  ✅
 '''
            self.ask_textchange='''Which mode do you choose to change your messages:
edit: in an editable form - the possibility of a flood!!
bold: ** Hello **
copy: ` Hello `
none: hello 

💡: Copy the type you want and send it
` bold ` - ` copy ` - ` none ` '''
            self.ask_status='''
♻️ Choose the desired action that you want to be shown to others at the top of the page and send it:

` photo ` : Sending photo
` video `: Sending video
` sticker `: Selecting a sticker
` recording video `: recording the message video
` playing `: playing
` recording voice `: Voice is being recorded
` typing `: Writing
` online `: Online
` none `: normal and initial state

💡: Copy the type you want and send it
'''
            self.ask_emoji='🤪 Send the emoji you want to react to messages \n or if you want to turn it off, send ` none `.'
            
            
            self.feature_setted=lambda  amount :f'''The value {amount} has been set for the desired command ✅
You can also see all the settings by sending the word ` setting ` ! '''
            
            self.has_turned=lambda  X : f'''The desired value turned {X} ✅
You can also see all the settings by sending the word ` setting `!'''
            self.askwel='''🌃 Please send the message you want to be sent when someone joins the group:
And also send ` None ` to remove and turning off.
            
💡: This message can be a photo, video or text or anything
💡: You can also use the following expressions in your text

{name} : User's name
{username}: User's username
{peer}: numeric ID of the user
{group} : group name

To use any of the above words, insert {} inside the text 🔋
'''
            self.askcard = '''💳 Please send your desired card number:
And also send ` None ` to remove it.'''
            
            self.askbio='''🖋️: Send your desired original bio:
(This bio is displayed when "random bio" is turned off 💬)
And also send ` None ` to remove it.'''
            
            self.askrandbio='''🖋️ :Please send the biography which you want
            
💡: This biography changes every minute, you can also use the words
💡: you can add biographys with no limit , robot will choose one randomly 

{online}: online status with emoji
{heart}: Hearts with different colors
{love}: All hearts
{time}: hours and minutes
{rand}: a random number between 1 and 1000
{emoji} : Special emojis
{date} : Complete date
{day} : date (only day)

To use any of the above words, insert {} inside the text🔋'''

            self.askclerk='''Please send the message you want to be sent to those who send messages when you are offline 🌃:
And also send ` None ` to remove the word.
            
💡: This message can be a photo, video or text or anything'''

            self.duplicated= lambda  dup : f'🗞 This value has already been registered \n 💡 : {dup}'
            
            self.askdelbio = lambda  bios : f'''Submit the desired bios for deletion:
💡 List of bios 💡
{bios}'''
            self.answer_setted= lambda word , answer : f'''The sent answer and word were added:
📩 word: `{word}`
📩 Answer: `{answer}`'''
            
            self.setting=lambda emoji , type_model , contacts , text_only , login , chat_model , defend , delsaver , chatsaver , randbio ,attack , spy , pvlock , gplock , a_j , a_p , answering , clean , read , reaction , wel , love , card , lchannel , mchannel , mainbio , clerk :f'''
🪩 dev : @amiralirj_official 

Type model: {type_model}
Only contacts: {emoji(contacts)}
Text only: {emoji(text_only)}
Anti-login: {emoji(login)}
Chat mode: {chat_model}
Safe mode: {emoji(defend)}
Message deletion notification: {emoji(delsaver)}
Save the chat in the database: {emoji(chatsaver)}
Animated and random bio: {emoji(randbio)}
Attack mode: {emoji(attack)}
Spy mode: {emoji(spy)}
New pv lock: {emoji(pvlock)}
New group lock: {emoji(gplock)}
Automatic game join: {emoji(a_j)}
Automatic game play : {emoji(a_p)}
Automatic answering: {emoji(answering)}
Automatic cleaning: {emoji(clean)}
Automatic Reading: {emoji(read)}
Automatic reaction : {reaction}
Greeter and welcomer : {wel}
Love : {love}
Card number: {card}
Logs channel: {lchannel}
Message channel: {mchannel}
Main bio: {mainbio}
clerk mode: {clerk}
Language : ENGLISH 

🪩 dev: https://www.github.com/amiralirj
'''
            self.help = '''★ TELEGRAM POWERFULL MANAGER ★ 
🪩 DEV : https://www.github.com/amiralirj 
🪩 DEV : @amiralirj_official 
🔴 key sections (on | off)   

♦︎read `on' or `off'
- Sending messages in real time

♦︎answering ` on ` or ` off `
- Automatic response according to predetermined words

♦︎ autoplay ` on ` or ` off `
- @wererolfbot auto playing

♦︎autojoin `on` or `off`
- Auto join in game @wererolfbot

🔥delsaver `on` or `off`
- If the message is deleted by any user, that message and its content will be uploaded to the channel or in saved message immediately 

♦︎contacts `on` or `off`
- Limiting people who are not in your contacts (only those who are in your contacts can send you messages)

♦︎texts `on` or `off`
- The contents of photos and... will be deleted and users will only be able to send you text messages

♦︎antilogin `on` or `off`
- No one can enter your account after it is turned on

♦︎safe `on` or `off`
- Safe mode: Those who do not have a message with you or who have given you less than 200 messages will be archived and muted.

♦︎randbio `on` or `off`
- Random and rotating bio according to the sentences you set in advance

♦︎attack `on` or `off`
- Attack mode: those who do not send message to you or sent you less than 75 messages will be blocked (by informing them of the attack mode)

🔥saving ` on ` or ` off `
- Saving and backing up all chats will be available even if the chats are deleted
- Command to get desired chat: see [reply] or [id]

🔥 spy ` on ` or ` off `
- Spy mode: the words you set to be spied on, if they are seen in a message, that message will be immediately sent to your channel or saved message.

🔥cleaning ` on ` or ` off `
- Cleaning private chats every day (except pinned ones)

♦︎grouplock `on` or `off`
- Locking of add in new groups (the robot will leave when you added to the group)

♦︎privatelock `on` or `off`
- Blocking of new private chats along with informing them that this lock is active

♦︎ bot `on` or `off`
- Turning the robot on or off

☆☆☆☆☆☆☆
🔱 Advanced section 🔱
> `Automatic` answering 🕊
♧ `clearanswers`: clear all automatic answers
♧ `delanswer`: delete an answer
♧ `answerlist`: view all keys and answers
♧ `addanswer`: add answer and key
★
> `Espionage` 👀
♧ `clearspies`: to clear all registered words under observation
♧ `delspy`: delete a word
♧ `spylist`: to see all the words and sentences under observation
♧ `addspy`: add word or sentence for spying
★
> Enemy ☠️
♧ `delenemy`: add enemy
♧ `clearenemies`: clear all enemies
♧ `addenemy`: [reply][id] add enemy
♧ `enemylist`: view all enemies
★
> Animated bio ✒️
♧ `biolist`: Random bio list
♧ `clearbioes`: to clear all registered bios
♧ `delbio`: Delete only one bio
♧ `addbio`: Add bio
★
> Secretary mode ♂️ 🤵🏼
> If someone sends a message when you are offline, this feature will send the message you recorded to that person.
♧ `clerk`
★
♧ `setmainbio`: The main bio that is placed on your profile when you turn off the random bio
★
> Store feature 🏪
♧ `setcard`: register card number or any other text
♧ `card`: Display card number or registered text quickly
★
> Love ♥️
> Sends wish times by heart to the registered person
♧ `dellove`: [in chat] Add love
♧ `setlove`: [in chat] remove love
★
> Robot language
♧ `lang` `en` or `fa`
★
> Welcome 🃏
♧ `setwel`
★
> Automatic reaction 🤪
> All messages sent in private chat will reacted to the recorded emoji at the same moment
♧ `reaction`
★
> Your status   🗯
> The status that is displayed at the top of the page (Writing...)
♧ `status`
★
> Type mode 📝
♧ `typemodel`
★
> View archived chats
> To use and record chats, first turn on saving messages
♧ `see`: [reply][in chat][id] Send a chat file with that person
♧ `allchats`: send all chat files
★

🤪 OTHERS 🤪 
`kill` [reply] : animated blocking
`spam`  [num of spams] | [text] - spam 100 | Rj
` wiki ` [your_search]
` wikifa ` [your_search]
`forall` 
`forpv` 
`replytag` [your text]
`tag`
`stop`
`ban`
`ban`
`lock`
`unlock`
`mute`
`temmute` [reply or peer id] | [time]
`unmute`
`leave`
`info` [reply]
`block`
`unblock`
`mydel` delete all outgoing messages 
🪩 DEV : https://www.github.com/amiralirj 
🪩 DEV : @amiralirj_official 
'''

#-------------------------------------------------------------------------------------------------------------------------------------

        if lang :
            self.all_m_deleted = 'تمامی پیام ها پاک شد !'
            self.deleted = 'کاربر حذف شده است !'
            self.only_text = 'این مقدار فقط میتواند متن باشد !'
            self.all_removed = 'تمامی مقدار ها پاک شد 🗑'
            self.ask_word='👀 : کلمه یا جمله ی کوتاه مورد نظر که میخواهید مورد پاسخگویی قرار بگیرد را ارسال کنید : '
            self.ask_answer = '💡: پاسخ مورد نظر خود را به کلمه یا جمله ی ارسال شده ی بالا را ارسال کنید '
            self.askword='👀 : کلمه یا جمله ی کوتاه مورد نظر که میخواهید مورد جاسوسی قرار بگیرد را ارسال کنید : '
            self.askdelspy = '🗑 کلمه ی مورد نظر که میخواهید از حالت جاسوسی حذف شود را ارسال کنید : '
            self.askdelword = '🗑 کلمه ی مورد نظر که میخواهید از حالت پاسخگویی حذف شود را ارسال کنید : '
            self.removed='مقدار مورد نظر حذف شد 🗑'
            self.should_replied='💡 : این دستور باید بر روی پیامی ریپلای شود '
            self.muted = 'کاربر مورد نظر میوت شد 🔕'
            self.unmuted = 'کاربر مورد نظر انمیوت شد 🔔'
            self.locked = 'گروه قفل شد 🔐'
            self.unlocked = 'گروه باز شد 🔓'
            self.unbanned = 'کاربر مورد نظر از گروه آنبن شد ✅ '
            self.banned = 'کاربر مورد نظر از گروه بن شد ✅ '
            self.stopped = 'متوقف شد 🔴 '
            self.cancel = 'همچنین میتوانید واژه ` cancel ` را برای لغو فرایند استفاده کنید !'
            self.cancelled = 'لغو شد ✅'
            self.timeout = 'مقداری دریافت نشد و فرایند لغو شد ⏱❌'
            self.on = 'روشن'
            self.off='خاموش'
            
            self.bot_turn=lambda turn : f'''🔴 ربات {turn} شد 🟢'''
            self.temmuted = lambda min : f'کاربر مورد نظر برای {min} دقیقه میوت شد 🔕'
            self.complited = lambda x : f'💎 : قرایند {x} بار به صورت موفقیت امیز انجام شد .'
            self.user_restricked='''دوست گرامی 
            🔴 متاسفانه محدودیت های اعمال شده برای اکانت شما هم اعمال میشود 
            اکانت شما توسط ربات بلاک میشود ولی پیوی شما باقی میماند تا بعد از تایید انبلاک شوید ✅
            '''
            self.attack_mode_is_on='''دوست گرامی 
حالت حمله روشن است و شما نمیتوانید درحال حاضر با من ارتباط داشته باشید 🔐 
اکانت شما توسط ربات بلاک میشود ولی پیوی شما باقی میماند تا بعد از تایید انبلاک شوید ✅
'''
            self.ask_textchange='''کدام حالت را برای عوض شدن پیام های خود انتخاب میکنید : 
edit : به صورت ادیت شونده -- احتمال فلاد !! 
bold : ** سلام **
copy :  ` سلام `  
none : سلام 

💡 : نوع مورد نظر خود را کپی کنید و ارسال کنید 
` bold ` - ` copy ` - ` none ` '''
            
            self.ask_status='''
♻️ عمل مورد نظری که میخواهید در بالای صفحه به دیگران نشان داده شود را انتخاب کنید و ارسال نمایید :

` photo ` : درحال ارسال عکس
` video ` : درحال ارسال ویدیو
` sticker ` : درحال انتخاب کردن استیکر
` recording video ` : درحال گرفتن ویدیو مسیج 
` playing ` : درحال بازی کردن
` recording voice ` : درحال ظبط وویس 
` typing ` : درحال نوشتن 
` online ` : انلاین
` none ` : حالت عادی و اولیه

            '''
            
            self.ask_emoji='🤪 ایموجی مورد نظر خود را بفرستید \n یا اگر میخواهید آن را خاموش کنید عبارت ` none ` را ارسال کنید .'

            self.feature_setted=lambda  amount :f'''مقدار {amount} برای دستور مورد نظر تنظیم شد ✅ 
همچنین با فرستادن واژه ` setting ` میتوانید تمامی تنظیمات را مشاهده کنید ! '''

            self.has_turned=lambda  X : f'''مقدار مورد نظر {X} شد✅
همچنین با فرستادن واژه ` setting ` میتوانید تمامی تنظیمات را مشاهده کنید ! '''

            self.askwel='''لطفا پیامی که میخواهید هنگام عضو شدن فردی در گروه ارسال شود را بفرستید 🌃:
و همچنین برای حذف واژه ی `None` را ارسال نمایید . 
            
💡 : این پیام میتواند عکس ، فیلم یا متن یا هرچیزی باشد 🔋
💡 : همچنین میتوانید از عبارات زیر در متن خود استفاده کنید 

{name} : نام کاربر 
{username} : یوزرنیم کاربر 
{peer} : ایدی عددی کاربر
{group} : نام گروه

برای استفاده از هرکدام از واژه های فوق را همراه با {} داخل متن جایگذاری کنید 🔋
'''


            self.askcard = '''💳 لطفا شماره کارت مورد نظر خود را ارسال کنید  : 
و همچنین برای حذف واژه ی `None` را ارسال نمایید . '''
            
            self.askbio='''🖋️ :  بیو اصلی مورد نظر خود را ارسال کنید :
( این بیو هنگام خاموش بودن " بیوی شانسی " به نمایش در می آید 💬 )
و همچنین برای حذف واژه ی `None` را ارسال نمایید . '''
            
            self.askrandbio='''🖋️ : لطفا بیوی مورد نظر خود را بفرستید
💡 : این بیو هر دقیقه عوض میشود ، همچنین میتوانید از واژه های 

{online} : وضعیت انلاینی با ایموجی
{heart} : قلب ها با رنگ های متفاوت
{love} : تمامی قلب ها 
{time} :  ساعت و دقیقه
{rand} : عددی رندوم بین ۱ تا ۱۰۰۰
{emoji} : ایموجی های خاص 
{date} : تاریخ کامل
{day} : تاریخ (فقط روز)

برای استفاده از هرکدام از واژه های فوق را همراه با {} داخل متن جایگذاری کنید 🔋'''
            
            self.askclerk='''لطفا پیامی که میخواهید هنگام افلاین شدنتون به کسانی که پیام میدهند ارسال شود را بفرستید 🌃:
و همچنین برای حذف واژه ی `None` را ارسال نمایید . 
            
💡 : این پیام میتواند عکس ، فیلم یا متن یا هرچیزی باشد 🔋'''

            self.duplicated= lambda  dup : f'🗞 این  مقدار قبلا ثبت شده است \n 💡 : {dup}'
            
            self.askdelbio = lambda  bios : f'''بیو های مورد نظر را برای حذف ارسال کنید : 
💡 لیست بیو ها 💡 
{bios}'''
            self.answer_setted= lambda word , answer : f'''پاسخ و کلمه ی ارسال شده اضافه شد : 
            📩 کلمه : `{word}`
            📩 پاسخ : `{answer}`'''
            
            self.setting=lambda emoji , type_model , contacts , text_only , login , chat_model , defend , delsaver , chatsaver , randbio ,attack , spy , pvlock , gplock , a_j , a_p , answering , clean , read , reaction , wel , love , card , lchannel , mchannel , mainbio , clerk :f'''
🪩 dev : @amiralirj_official 

مدل تایپ : {type_model}
فقط کانتکت ها : {emoji(contacts)}
فقط متن : {emoji(text_only)}
انتی لاگین : {emoji(login)}
حالت چت :{chat_model}
حالت امن : {emoji(defend)}
اطلاع رسانی پاک کردن پیام : {emoji(delsaver)}
ذخیره کردن چت در دیتابیس : {emoji(chatsaver)}
بیو متحرک : {emoji(randbio)}
حالت حمله : {emoji(attack)}
جاسوسی : {emoji(spy)}
قفل پیوی جدید : {emoji(pvlock)}
قفل گروه جدید : {emoji(gplock)}
جوین خودکار بازی : {emoji(a_j)}
بازی کردن خودکار  : {emoji(a_p)}
پاسخگویی خودکار : {emoji(answering)}
پاکسازی خودکار : {emoji(clean)}
خواندن پیام ها : {emoji(read)}
ری اکشن زدن : {reaction}
خوشامد گو : {wel}
عشق : {love}
شماره کارت : {card}
کانال لاگ ها : {lchannel}
کانال پیام ها : {mchannel}
بیوی اصلی : {mainbio}
حالت منشی : {clerk}
زبان : فارسی 

🪩 dev : https://www.github.com/amiralirj
'''
            self.help = '''★ TELEGRAM POWERFULL MANAGER ★ 
🪩 DEV : https://www.github.com/amiralirj 
🪩 DEV : @amiralirj_official 

🔴 بخش های کلیدی ( on | off )  🟢

♦︎read  `on` or `off` 
- سین شدن پیام ها در لحظه

♦︎answering `on` or `off`
- پاسخدهی خودکار با توجه به کلمات از پیش تعین شده 

♦︎autoplay `on` or `off`
- بازی کردن خودکار @wererolfbot

♦︎autojoin `on` or `off`
- جوین شدن خودکار در بازی  @wererolfbot

🔥delsaver `on` or `off`
- در صورت پاک شدن پیام توسط هر کاربری سریعا آن پیام و محتوای آن در کانال فروارد میشود 

♦︎contacts `on` or `off`
- محدود کردن افرادی که در کانتکت شما نیستند (فقط کسانی که جزو کانتکتتون هستند میتوانند به شما پیام بدهند)

♦︎texts `on` or `off`
- محتوا های عکس و ... پاک میشود و کاربران فقط قادر به ارسال پیام در نوع متن به شما میباشند

♦︎antilogin `on` or `off`
- بعد از روشن شدن کسی نمیتواند وارد اکانت شما بشود 

♦︎safe `on` or `off`
- حالت امن : کسانی که با شما پیوی ندارند یا کمتر از 200 پیام به شما داده اند ارشیو و میوت میشوند 

♦︎randbio `on` or `off`
- بیو رندوم و چرخشی طبق جمله هایی که از پیش تعیین کردید

♦︎attack `on` or `off`
- حالت حمله : کسانی که با شما پیوی نداشتند یا کمتر از 75 پیام به شما دادند بلاک میشوند (با اطلاع دادن حالت حمله به آن ها)

🔥saving `on` or `off`
- ذخیره کردن و بک اپ گرفتن تمامی چت ها , حتی اگر چت ها پاک شوند نیز قابل دسترس خواهد بود 
- دستور گرفتن چت مورد نظر : see [reply] or [id] 

🔥spy `on` or `off`
- حالت جاسوسی : کلماتی که تعیین کردید جاسوسی شوند اگر در پیامی دیده بشوند سریعا آن پیام به در کانال یا سیو مسیجتون فروارد میشوند 

🔥cleaning `on` or `off`
- پاکسازی پیوی ها هرروز (بجز پین شده ها) 

♦︎grouplock `on` or `off`
- قفل شدن اد در گروه های جدید ( ربات درجا بعد از اد شدن لفت میدهد)

♦︎privatelock `on` or `off`
- بلاک شدن پیوی های جدید همراه با اطلاع به آنها که این قفل فعال است  

♦︎bot `on` or `off`
- روشن یا خاموش شدن ربات



☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆
🔱 بخش پیشرفته 🔱
> پاسخ گویی خودکار 🕊 
♧ clearanswers : پاکسازی تمام جواب های خودکار
♧ delanswer : پاک کردن یک جواب
♧ answerlist : مشاهده ی تمام کلید ها و جواب ها
♧ addanswer : اضافه کردن جواب و کلید
★
> جاسوسی 👀
♧ clearspies پاکسازی تمام کلمات تحت نظر ثبت شده
♧ delspy پاک کردن یک کلمه
♧ spylist مشاهده ی تمامی کلمات و جمله های تحت نظر
♧ addspy اضافه کردن کلمه یا جمله جهت جاسوسی 
★
> دشمن ☠️
♧ delenemy اضافه کردن دشمن
♧ clearenemies پاکسازی تمامی دشمن ها 
♧ addenemy [reply][id] اضافه کردن دشمن 
♧ enemylist مشاهده ی تمامی دشمنان
★
> بیو متحرک ✒️ 
♧ biolist لیست بیو های چرخشی و متحرک
♧ clearbioes پاکسازی تمامی بیو های ثبت شده
♧ delbio پاک کردن فقط یک بیو
♧ addbio اضافه کردن بیو
★
> حالت منشی 🤵🏼‍♂️  
> اگر فردی پیام دهد هنگامی که شما افلاین هستید این قابلیت پیامی که شما ثبت کردید را برای آن فرد میفرستد   
♧ clerk 
★
♧ setmainbio بیوی اصلی که هنگام خاموش کردن بیو متحرک بر روی پروفالتون قرار میگیرد
★
> قابلیت فروشگاهی 🏪
♧ setcard ثبت شماره کارت یا هر متن دیگری    
♧ card نمایش شماره کارت یا متن ثبت شده به سرعت
★
> عشق ♥️ 
> ساعت های ست و ویش تایم ها را با قلب برای فرد ثبت شده میفرستد
♧ dellove [in chat] اضافه کردن عشق
♧ setlove [in chat] حذف کردن عشق
★
> زبان ربات
♧ `lang` `en` or `fa`
★
> خوش امدگویی 🃏
♧ setwel 
★
> ری اکشن خودکار 🤪
> تمامی پیام های فرستاده شده در پیوی در همان لحظه ایموجی ثبت شده را ری اکت میکنند 
♧ reaction
★
> وضعیت شما 🟢🗯
> وضعیتی که بالای صفحه به نمایش در می آید (درحال نوشتن . ...)
♧ status
★
> حالت تایپ 📝 
♧ typemodel
★
> دیدن چت های ارشیو شده 
> برای استفاده و ثبت چت ها اول ذخیره ی پیام ها را روشن کنید
♧ see [reply][in chat][id] فرستادن فایل چت با اون فرد
♧ allchats فرستادن تمامی فایل های چت 
★
🤪 سرگرمی 🤪 
`kill` [reply] : animated blocking
`spam`  [num of spams] | [text] - spam 100 | Rj
` wiki ` [your_search]
` wikifa ` [your_search]
`forall`
`forpv`
`replytag` [your text]
`tag`
`stop`
`ban`
`ban`
`lock`
`unlock`
`mute`
`temmute` [reply or peer id] | [time]
`unmute`
`leave`
`info` [reply]
`block`
`unblock`
`mydel` پاکسازی تمامی پیام های خود
🪩 DEV : https://www.github.com/amiralirj 
🪩 DEV : @amiralirj_official 
'''


# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 .

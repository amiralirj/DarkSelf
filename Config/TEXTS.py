#-----------------+-----------------|\
# https://www.github.com/amiralirj  |-|\     
# https://t.me/amiralirj_official   |-|/    
#-----------------+-----------------|/
class Text :
    def __init__(self,lang) -> None:
        self.error='there is somthing wrong !'
        self.kill5='killed - blocked :)'
        self.kill4='π΄=β=========π«'
        self.kill3='π΄====β======π«'
        self.kill2='π΄=======β===π«'
        self.kill1='π΄=========β=π«'
        
        self.cancel_btn = 'cancel'
        self.bye = 'Bye Bye !'
        self.not_found = 'E404 : does not match any pages. Try another id! '
        
        
        self.channel_mid_link=lambda  id , peer : f'https://t.me/c/1{str(abs(int(peer))).strip("100")}/{int(id)}'
        self.message_deleted=lambda id , name , text : f'''DELETED π : 
        
π‘ id : {id} 
π‘ name : {name} 

π‘ ` {text} `'''
        
        self.send_spying=lambda id , name , text : f'''SPYING π : 
        
π‘{id} - {name} 

π‘` {text} `'''
        
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
            self.all_removed = 'All values ββwere deleted π'
            self.ask_word = 'π: Send the desired word or short sentence that you want answered:'
            self.ask_answer ='π‘: Submit your desired answer to the word or sentence posted above'
            self.askword = 'π: Send the desired word or short text that you want to be spied on:'
            self.askdelspy ='π Send the desired word that you want to remove from spy mode:'
            self.askdelword ='π Send the desired word that you want to remove from the reply mode:'
            self.removed = "The desired value was deleted π"
            self.should_replied = 'π‘: This command must be replayed on a message'
            self.muted = "The intended user has muted π"
            self.unmuted ="The intended user has unmuted π"
            self.locked = 'The group is locked π'
            self.unlocked = 'The group is unlocked π'
            self.unbanned = "The intended user has unbanned from group β"
            self.banned = "The intended user has banned from group β"
            self.stopped = 'is stopped now π΄'
            self.cancel = 'You can also use the word `cancel` to cancel the process! '
            self.cancelled ='process canceled β'
            self.timeout = 'The amount was not received and the process was canceled β±β'
            self.on = 'on'
            self.off = 'off'

    

            self.bot_turn=lambda turn : f'''π΄ Bot has turned {turn} π’'''
            self.temmuted = lambda min : f'The intended user has been muted for {min} minutes π'
            self.complited = lambda x : f'π: process were done {x} times successfully.'
            
            self.user_restricked='''Dear friend
π΄ Unfortunately, the restrictions are also applied to your account 
Your account will be blocked by the robot, but your chat will remain until confirmation which you will be unblocked after  β
'''
            self.attack_mode_is_on='''Dear friend
π΄ Unfortunately, The attack mode is on and you can't communicate with me right now π
Your account will be blocked by the robot, but your chat will remain until confirmation which you will be unblocked after  β
 '''
            self.ask_textchange='''Which mode do you choose to change your messages:
edit: in an editable form - the possibility of a flood!!
bold: ** Hello **
copy: ` Hello `
none: hello 

π‘: Copy the type you want and send it
` bold ` - ` copy ` - ` none ` '''
            self.ask_status='''
β»οΈ Choose the desired action that you want to be shown to others at the top of the page and send it:

` photo ` : Sending photo
` video `: Sending video
` sticker `: Selecting a sticker
` recording video `: recording the message video
` playing `: playing
` recording voice `: Voice is being recorded
` typing `: Writing
` online `: Online
` none `: normal and initial state

π‘: Copy the type you want and send it
'''
            self.ask_emoji='π€ͺ Send the emoji you want to react to messages \n or if you want to turn it off, send ` none `.'
            
            
            self.feature_setted=lambda  amount :f'''The value {amount} has been set for the desired command β
You can also see all the settings by sending the word ` setting ` ! '''
            
            self.has_turned=lambda  X : f'''The desired value turned {X} β
You can also see all the settings by sending the word ` setting `!'''
            self.askwel='''π Please send the message you want to be sent when someone joins the group:
And also send ` None ` to remove and turning off.
            
π‘: This message can be a photo, video or text or anything
π‘: You can also use the following expressions in your text

{name} : User's name
{username}: User's username
{peer}: numeric ID of the user
{group} : group name

To use any of the above words, insert {} inside the text π
'''
            self.askcard = '''π³ Please send your desired card number:
And also send ` None ` to remove it.'''
            
            self.askbio='''ποΈ: Send your desired original bio:
(This bio is displayed when "random bio" is turned off π¬)
And also send ` None ` to remove it.'''
            
            self.askrandbio='''ποΈ :Please send the biography which you want
            
π‘: This biography changes every minute, you can also use the words
π‘: you can add biographys with no limit , robot will choose one randomly 

{online}: online status with emoji
{heart}: Hearts with different colors
{love}: All hearts
{time}: hours and minutes
{rand}: a random number between 1 and 1000
{emoji} : Special emojis
{date} : Complete date
{day} : date (only day)

To use any of the above words, insert {} inside the textπ'''

            self.askclerk='''Please send the message you want to be sent to those who send messages when you are offline π:
And also send ` None ` to remove the word.
            
π‘: This message can be a photo, video or text or anything'''

            self.duplicated= lambda  dup : f'π This value has already been registered \n π‘ : {dup}'
            
            self.askdelbio = lambda  bios : f'''Submit the desired bios for deletion:
π‘ List of bios π‘
{bios}'''
            self.answer_setted= lambda word , answer : f'''The sent answer and word were added:
π© word: `{word}`
π© Answer: `{answer}`'''
            
            self.setting=lambda emoji , type_model , contacts , text_only , login , chat_model , defend , delsaver , chatsaver , randbio ,attack , spy , pvlock , gplock , a_j , a_p , answering , clean , read , reaction , wel , love , card , lchannel , mchannel , mainbio , clerk :f'''
πͺ© dev : @amiralirj_official 

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

πͺ© dev: https://www.github.com/amiralirj
'''
            self.help = '''β TELEGRAM POWERFULL MANAGER β 
πͺ© DEV : https://www.github.com/amiralirj 
πͺ© DEV : @amiralirj_official 
π΄ key sections (on | off)   

β¦οΈread `on' or `off'
- Sending messages in real time

β¦οΈanswering ` on ` or ` off `
- Automatic response according to predetermined words

β¦οΈ autoplay ` on ` or ` off `
- @wererolfbot auto playing

β¦οΈautojoin `on` or `off`
- Auto join in game @wererolfbot

π₯delsaver `on` or `off`
- If the message is deleted by any user, that message and its content will be uploaded to the channel or in saved message immediately 

β¦οΈcontacts `on` or `off`
- Limiting people who are not in your contacts (only those who are in your contacts can send you messages)

β¦οΈtexts `on` or `off`
- The contents of photos and... will be deleted and users will only be able to send you text messages

β¦οΈantilogin `on` or `off`
- No one can enter your account after it is turned on

β¦οΈsafe `on` or `off`
- Safe mode: Those who do not have a message with you or who have given you less than 200 messages will be archived and muted.

β¦οΈrandbio `on` or `off`
- Random and rotating bio according to the sentences you set in advance

β¦οΈattack `on` or `off`
- Attack mode: those who do not send message to you or sent you less than 75 messages will be blocked (by informing them of the attack mode)

π₯saving ` on ` or ` off `
- Saving and backing up all chats will be available even if the chats are deleted
- Command to get desired chat: see [reply] or [id]

π₯ spy ` on ` or ` off `
- Spy mode: the words you set to be spied on, if they are seen in a message, that message will be immediately sent to your channel or saved message.

π₯cleaning ` on ` or ` off `
- Cleaning private chats every day (except pinned ones)

β¦οΈgrouplock `on` or `off`
- Locking of add in new groups (the robot will leave when you added to the group)

β¦οΈprivatelock `on` or `off`
- Blocking of new private chats along with informing them that this lock is active

β¦οΈ bot `on` or `off`
- Turning the robot on or off

βββββββ
π± Advanced section π±
> `Automatic` answering π
β§ `clearanswers`: clear all automatic answers
β§ `delanswer`: delete an answer
β§ `answerlist`: view all keys and answers
β§ `addanswer`: add answer and key
β
> `Espionage` π
β§ `clearspies`: to clear all registered words under observation
β§ `delspy`: delete a word
β§ `spylist`: to see all the words and sentences under observation
β§ `addspy`: add word or sentence for spying
β
> Enemy β οΈ
β§ `delenemy`: add enemy
β§ `clearenemies`: clear all enemies
β§ `addenemy`: [reply][id] add enemy
β§ `enemylist`: view all enemies
β
> Animated bio βοΈ
β§ `biolist`: Random bio list
β§ `clearbioes`: to clear all registered bios
β§ `delbio`: Delete only one bio
β§ `addbio`: Add bio
β
> Secretary mode βοΈ π€΅πΌ
> If someone sends a message when you are offline, this feature will send the message you recorded to that person.
β§ `clerk`
β
β§ `setmainbio`: The main bio that is placed on your profile when you turn off the random bio
β
> Store feature πͺ
β§ `setcard`: register card number or any other text
β§ `card`: Display card number or registered text quickly
β
> Love β₯οΈ
> Sends wish times by heart to the registered person
β§ `dellove`: [in chat] Add love
β§ `setlove`: [in chat] remove love
β
> Robot language
β§ `lang` `en` or `fa`
β
> Welcome π
β§ `setwel`
β
> Automatic reaction π€ͺ
> All messages sent in private chat will reacted to the recorded emoji at the same moment
β§ `reaction`
β
> Your status   π―
> The status that is displayed at the top of the page (Writing...)
β§ `status`
β
> Type mode π
β§ `typemodel`
β
> View archived chats
> To use and record chats, first turn on saving messages
β§ `see`: [reply][in chat][id] Send a chat file with that person
β§ `allchats`: send all chat files
β

π€ͺ OTHERS π€ͺ 
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
πͺ© DEV : https://www.github.com/amiralirj 
πͺ© DEV : @amiralirj_official 
'''

#-------------------------------------------------------------------------------------------------------------------------------------

        if lang :
            self.all_m_deleted = 'ΨͺΩΨ§ΩΫ ΩΎΫΨ§Ω ΩΨ§ ΩΎΨ§Ϊ© Ψ΄Ψ― !'
            self.deleted = 'Ϊ©Ψ§Ψ±Ψ¨Ψ± Ψ­Ψ°Ω Ψ΄Ψ―Ω Ψ§Ψ³Ψͺ !'
            self.only_text = 'Ψ§ΫΩ ΩΩΨ―Ψ§Ψ± ΩΩΨ· ΩΫΨͺΩΨ§ΩΨ― ΩΨͺΩ Ψ¨Ψ§Ψ΄Ψ― !'
            self.all_removed = 'ΨͺΩΨ§ΩΫ ΩΩΨ―Ψ§Ψ± ΩΨ§ ΩΎΨ§Ϊ© Ψ΄Ψ― π'
            self.ask_word='π : Ϊ©ΩΩΩ ΫΨ§ Ψ¬ΩΩΩ Ϋ Ϊ©ΩΨͺΨ§Ω ΩΩΨ±Ψ― ΩΨΈΨ± Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― ΩΩΨ±Ψ― ΩΎΨ§Ψ³Ψ?Ϊ―ΩΫΫ ΩΨ±Ψ§Ψ± Ψ¨Ϊ―ΫΨ±Ψ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― : '
            self.ask_answer = 'π‘: ΩΎΨ§Ψ³Ψ? ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ψ¨Ω Ϊ©ΩΩΩ ΫΨ§ Ψ¬ΩΩΩ Ϋ Ψ§Ψ±Ψ³Ψ§Ω Ψ΄Ψ―Ω Ϋ Ψ¨Ψ§ΩΨ§ Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― '
            self.askword='π : Ϊ©ΩΩΩ ΫΨ§ Ψ¬ΩΩΩ Ϋ Ϊ©ΩΨͺΨ§Ω ΩΩΨ±Ψ― ΩΨΈΨ± Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― ΩΩΨ±Ψ― Ψ¬Ψ§Ψ³ΩΨ³Ϋ ΩΨ±Ψ§Ψ± Ψ¨Ϊ―ΫΨ±Ψ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― : '
            self.askdelspy = 'π Ϊ©ΩΩΩ Ϋ ΩΩΨ±Ψ― ΩΨΈΨ± Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― Ψ§Ψ² Ψ­Ψ§ΩΨͺ Ψ¬Ψ§Ψ³ΩΨ³Ϋ Ψ­Ψ°Ω Ψ΄ΩΨ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― : '
            self.askdelword = 'π Ϊ©ΩΩΩ Ϋ ΩΩΨ±Ψ― ΩΨΈΨ± Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― Ψ§Ψ² Ψ­Ψ§ΩΨͺ ΩΎΨ§Ψ³Ψ?Ϊ―ΩΫΫ Ψ­Ψ°Ω Ψ΄ΩΨ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― : '
            self.removed='ΩΩΨ―Ψ§Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± Ψ­Ψ°Ω Ψ΄Ψ― π'
            self.should_replied='π‘ : Ψ§ΫΩ Ψ―Ψ³ΨͺΩΨ± Ψ¨Ψ§ΫΨ― Ψ¨Ψ± Ψ±ΩΫ ΩΎΫΨ§ΩΫ Ψ±ΫΩΎΩΨ§Ϋ Ψ΄ΩΨ― '
            self.muted = 'Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± ΩΫΩΨͺ Ψ΄Ψ― π'
            self.unmuted = 'Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± Ψ§ΩΩΫΩΨͺ Ψ΄Ψ― π'
            self.locked = 'Ϊ―Ψ±ΩΩ ΩΩΩ Ψ΄Ψ― π'
            self.unlocked = 'Ϊ―Ψ±ΩΩ Ψ¨Ψ§Ψ² Ψ΄Ψ― π'
            self.unbanned = 'Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± Ψ§Ψ² Ϊ―Ψ±ΩΩ Ψ’ΩΨ¨Ω Ψ΄Ψ― β '
            self.banned = 'Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± Ψ§Ψ² Ϊ―Ψ±ΩΩ Ψ¨Ω Ψ΄Ψ― β '
            self.stopped = 'ΩΨͺΩΩΩ Ψ΄Ψ― π΄ '
            self.cancel = 'ΩΩΪΩΫΩ ΩΫΨͺΩΨ§ΩΫΨ― ΩΨ§ΪΩ ` cancel ` Ψ±Ψ§ Ψ¨Ψ±Ψ§Ϋ ΩΨΊΩ ΩΨ±Ψ§ΫΩΨ― Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ϊ©ΩΫΨ― !'
            self.cancelled = 'ΩΨΊΩ Ψ΄Ψ― β'
            self.timeout = 'ΩΩΨ―Ψ§Ψ±Ϋ Ψ―Ψ±ΫΨ§ΩΨͺ ΩΨ΄Ψ― Ω ΩΨ±Ψ§ΫΩΨ― ΩΨΊΩ Ψ΄Ψ― β±β'
            self.on = 'Ψ±ΩΨ΄Ω'
            self.off='Ψ?Ψ§ΩΩΨ΄'
            
            self.bot_turn=lambda turn : f'''π΄ Ψ±Ψ¨Ψ§Ψͺ {turn} Ψ΄Ψ― π’'''
            self.temmuted = lambda min : f'Ϊ©Ψ§Ψ±Ψ¨Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± Ψ¨Ψ±Ψ§Ϋ {min} Ψ―ΩΫΩΩ ΩΫΩΨͺ Ψ΄Ψ― π'
            self.complited = lambda x : f'π : ΩΨ±Ψ§ΫΩΨ― {x} Ψ¨Ψ§Ψ± Ψ¨Ω Ψ΅ΩΨ±Ψͺ ΩΩΩΩΫΨͺ Ψ§ΩΫΨ² Ψ§ΩΨ¬Ψ§Ω Ψ΄Ψ― .'
            self.user_restricked='''Ψ―ΩΨ³Ψͺ Ϊ―Ψ±Ψ§ΩΫ 
            π΄ ΩΨͺΨ§Ψ³ΩΨ§ΩΩ ΩΨ­Ψ―ΩΨ―ΫΨͺ ΩΨ§Ϋ Ψ§ΨΉΩΨ§Ω Ψ΄Ψ―Ω Ψ¨Ψ±Ψ§Ϋ Ψ§Ϊ©Ψ§ΩΨͺ Ψ΄ΩΨ§ ΩΩ Ψ§ΨΉΩΨ§Ω ΩΫΨ΄ΩΨ― 
            Ψ§Ϊ©Ψ§ΩΨͺ Ψ΄ΩΨ§ ΨͺΩΨ³Ψ· Ψ±Ψ¨Ψ§Ψͺ Ψ¨ΩΨ§Ϊ© ΩΫΨ΄ΩΨ― ΩΩΫ ΩΎΫΩΫ Ψ΄ΩΨ§ Ψ¨Ψ§ΩΫ ΩΫΩΨ§ΩΨ― ΨͺΨ§ Ψ¨ΨΉΨ― Ψ§Ψ² ΨͺΨ§ΫΫΨ― Ψ§ΩΨ¨ΩΨ§Ϊ© Ψ΄ΩΫΨ― β
            '''
            self.attack_mode_is_on='''Ψ―ΩΨ³Ψͺ Ϊ―Ψ±Ψ§ΩΫ 
Ψ­Ψ§ΩΨͺ Ψ­ΩΩΩ Ψ±ΩΨ΄Ω Ψ§Ψ³Ψͺ Ω Ψ΄ΩΨ§ ΩΩΫΨͺΩΨ§ΩΫΨ― Ψ―Ψ±Ψ­Ψ§Ω Ψ­Ψ§ΨΆΨ± Ψ¨Ψ§ ΩΩ Ψ§Ψ±ΨͺΨ¨Ψ§Ψ· Ψ―Ψ§Ψ΄ΨͺΩ Ψ¨Ψ§Ψ΄ΫΨ― π 
Ψ§Ϊ©Ψ§ΩΨͺ Ψ΄ΩΨ§ ΨͺΩΨ³Ψ· Ψ±Ψ¨Ψ§Ψͺ Ψ¨ΩΨ§Ϊ© ΩΫΨ΄ΩΨ― ΩΩΫ ΩΎΫΩΫ Ψ΄ΩΨ§ Ψ¨Ψ§ΩΫ ΩΫΩΨ§ΩΨ― ΨͺΨ§ Ψ¨ΨΉΨ― Ψ§Ψ² ΨͺΨ§ΫΫΨ― Ψ§ΩΨ¨ΩΨ§Ϊ© Ψ΄ΩΫΨ― β
'''
            self.ask_textchange='''Ϊ©Ψ―Ψ§Ω Ψ­Ψ§ΩΨͺ Ψ±Ψ§ Ψ¨Ψ±Ψ§Ϋ ΨΉΩΨΆ Ψ΄Ψ―Ω ΩΎΫΨ§Ω ΩΨ§Ϋ Ψ?ΩΨ― Ψ§ΩΨͺΨ?Ψ§Ψ¨ ΩΫΪ©ΩΫΨ― : 
edit : Ψ¨Ω Ψ΅ΩΨ±Ψͺ Ψ§Ψ―ΫΨͺ Ψ΄ΩΩΨ―Ω -- Ψ§Ψ­ΨͺΩΨ§Ω ΩΩΨ§Ψ― !! 
bold : ** Ψ³ΩΨ§Ω **
copy :  ` Ψ³ΩΨ§Ω `  
none : Ψ³ΩΨ§Ω 

π‘ : ΩΩΨΉ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ϊ©ΩΎΫ Ϊ©ΩΫΨ― Ω Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― 
` bold ` - ` copy ` - ` none ` '''
            
            self.ask_status='''
β»οΈ ΨΉΩΩ ΩΩΨ±Ψ― ΩΨΈΨ±Ϋ Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― Ψ―Ψ± Ψ¨Ψ§ΩΨ§Ϋ Ψ΅ΩΨ­Ω Ψ¨Ω Ψ―ΫΪ―Ψ±Ψ§Ω ΩΨ΄Ψ§Ω Ψ―Ψ§Ψ―Ω Ψ΄ΩΨ― Ψ±Ψ§ Ψ§ΩΨͺΨ?Ψ§Ψ¨ Ϊ©ΩΫΨ― Ω Ψ§Ψ±Ψ³Ψ§Ω ΩΩΨ§ΫΫΨ― :

` photo ` : Ψ―Ψ±Ψ­Ψ§Ω Ψ§Ψ±Ψ³Ψ§Ω ΨΉΪ©Ψ³
` video ` : Ψ―Ψ±Ψ­Ψ§Ω Ψ§Ψ±Ψ³Ψ§Ω ΩΫΨ―ΫΩ
` sticker ` : Ψ―Ψ±Ψ­Ψ§Ω Ψ§ΩΨͺΨ?Ψ§Ψ¨ Ϊ©Ψ±Ψ―Ω Ψ§Ψ³ΨͺΫΪ©Ψ±
` recording video ` : Ψ―Ψ±Ψ­Ψ§Ω Ϊ―Ψ±ΩΨͺΩ ΩΫΨ―ΫΩ ΩΨ³ΫΨ¬ 
` playing ` : Ψ―Ψ±Ψ­Ψ§Ω Ψ¨Ψ§Ψ²Ϋ Ϊ©Ψ±Ψ―Ω
` recording voice ` : Ψ―Ψ±Ψ­Ψ§Ω ΨΈΨ¨Ψ· ΩΩΫΨ³ 
` typing ` : Ψ―Ψ±Ψ­Ψ§Ω ΩΩΨ΄ΨͺΩ 
` online ` : Ψ§ΩΩΨ§ΫΩ
` none ` : Ψ­Ψ§ΩΨͺ ΨΉΨ§Ψ―Ϋ Ω Ψ§ΩΩΫΩ

            '''
            
            self.ask_emoji='π€ͺ Ψ§ΫΩΩΨ¬Ϋ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ψ¨ΩΨ±Ψ³ΨͺΫΨ― \n ΫΨ§ Ψ§Ϊ―Ψ± ΩΫΨ?ΩΨ§ΩΫΨ― Ψ’Ω Ψ±Ψ§ Ψ?Ψ§ΩΩΨ΄ Ϊ©ΩΫΨ― ΨΉΨ¨Ψ§Ψ±Ψͺ ` none ` Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― .'

            self.feature_setted=lambda  amount :f'''ΩΩΨ―Ψ§Ψ± {amount} Ψ¨Ψ±Ψ§Ϋ Ψ―Ψ³ΨͺΩΨ± ΩΩΨ±Ψ― ΩΨΈΨ± ΨͺΩΨΈΫΩ Ψ΄Ψ― β 
ΩΩΪΩΫΩ Ψ¨Ψ§ ΩΨ±Ψ³ΨͺΨ§Ψ―Ω ΩΨ§ΪΩ ` setting ` ΩΫΨͺΩΨ§ΩΫΨ― ΨͺΩΨ§ΩΫ ΨͺΩΨΈΫΩΨ§Ψͺ Ψ±Ψ§ ΩΨ΄Ψ§ΩΨ―Ω Ϊ©ΩΫΨ― ! '''

            self.has_turned=lambda  X : f'''ΩΩΨ―Ψ§Ψ± ΩΩΨ±Ψ― ΩΨΈΨ± {X} Ψ΄Ψ―β
ΩΩΪΩΫΩ Ψ¨Ψ§ ΩΨ±Ψ³ΨͺΨ§Ψ―Ω ΩΨ§ΪΩ ` setting ` ΩΫΨͺΩΨ§ΩΫΨ― ΨͺΩΨ§ΩΫ ΨͺΩΨΈΫΩΨ§Ψͺ Ψ±Ψ§ ΩΨ΄Ψ§ΩΨ―Ω Ϊ©ΩΫΨ― ! '''

            self.askwel='''ΩΨ·ΩΨ§ ΩΎΫΨ§ΩΫ Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― ΩΩΪ―Ψ§Ω ΨΉΨΆΩ Ψ΄Ψ―Ω ΩΨ±Ψ―Ϋ Ψ―Ψ± Ϊ―Ψ±ΩΩ Ψ§Ψ±Ψ³Ψ§Ω Ψ΄ΩΨ― Ψ±Ψ§ Ψ¨ΩΨ±Ψ³ΨͺΫΨ― π:
Ω ΩΩΪΩΫΩ Ψ¨Ψ±Ψ§Ϋ Ψ­Ψ°Ω ΩΨ§ΪΩ Ϋ `None` Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω ΩΩΨ§ΫΫΨ― . 
            
π‘ : Ψ§ΫΩ ΩΎΫΨ§Ω ΩΫΨͺΩΨ§ΩΨ― ΨΉΪ©Ψ³ Ψ ΩΫΩΩ ΫΨ§ ΩΨͺΩ ΫΨ§ ΩΨ±ΪΫΨ²Ϋ Ψ¨Ψ§Ψ΄Ψ― π
π‘ : ΩΩΪΩΫΩ ΩΫΨͺΩΨ§ΩΫΨ― Ψ§Ψ² ΨΉΨ¨Ψ§Ψ±Ψ§Ψͺ Ψ²ΫΨ± Ψ―Ψ± ΩΨͺΩ Ψ?ΩΨ― Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ϊ©ΩΫΨ― 

{name} : ΩΨ§Ω Ϊ©Ψ§Ψ±Ψ¨Ψ± 
{username} : ΫΩΨ²Ψ±ΩΫΩ Ϊ©Ψ§Ψ±Ψ¨Ψ± 
{peer} : Ψ§ΫΨ―Ϋ ΨΉΨ―Ψ―Ϋ Ϊ©Ψ§Ψ±Ψ¨Ψ±
{group} : ΩΨ§Ω Ϊ―Ψ±ΩΩ

Ψ¨Ψ±Ψ§Ϋ Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ψ§Ψ² ΩΨ±Ϊ©Ψ―Ψ§Ω Ψ§Ψ² ΩΨ§ΪΩ ΩΨ§Ϋ ΩΩΩ Ψ±Ψ§ ΩΩΨ±Ψ§Ω Ψ¨Ψ§ {} Ψ―Ψ§Ψ?Ω ΩΨͺΩ Ψ¬Ψ§ΫΪ―Ψ°Ψ§Ψ±Ϋ Ϊ©ΩΫΨ― π
'''


            self.askcard = '''π³ ΩΨ·ΩΨ§ Ψ΄ΩΨ§Ψ±Ω Ϊ©Ψ§Ψ±Ψͺ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ―  : 
Ω ΩΩΪΩΫΩ Ψ¨Ψ±Ψ§Ϋ Ψ­Ψ°Ω ΩΨ§ΪΩ Ϋ `None` Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω ΩΩΨ§ΫΫΨ― . '''
            
            self.askbio='''ποΈ :  Ψ¨ΫΩ Ψ§Ψ΅ΩΫ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― :
( Ψ§ΫΩ Ψ¨ΫΩ ΩΩΪ―Ψ§Ω Ψ?Ψ§ΩΩΨ΄ Ψ¨ΩΨ―Ω " Ψ¨ΫΩΫ Ψ΄Ψ§ΩΨ³Ϋ " Ψ¨Ω ΩΩΨ§ΫΨ΄ Ψ―Ψ± ΩΫ Ψ’ΫΨ― π¬ )
Ω ΩΩΪΩΫΩ Ψ¨Ψ±Ψ§Ϋ Ψ­Ψ°Ω ΩΨ§ΪΩ Ϋ `None` Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω ΩΩΨ§ΫΫΨ― . '''
            
            self.askrandbio='''ποΈ : ΩΨ·ΩΨ§ Ψ¨ΫΩΫ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ?ΩΨ― Ψ±Ψ§ Ψ¨ΩΨ±Ψ³ΨͺΫΨ―
π‘ : Ψ§ΫΩ Ψ¨ΫΩ ΩΨ± Ψ―ΩΫΩΩ ΨΉΩΨΆ ΩΫΨ΄ΩΨ― Ψ ΩΩΪΩΫΩ ΩΫΨͺΩΨ§ΩΫΨ― Ψ§Ψ² ΩΨ§ΪΩ ΩΨ§Ϋ 

{online} : ΩΨΆΨΉΫΨͺ Ψ§ΩΩΨ§ΫΩΫ Ψ¨Ψ§ Ψ§ΫΩΩΨ¬Ϋ
{heart} : ΩΩΨ¨ ΩΨ§ Ψ¨Ψ§ Ψ±ΩΪ― ΩΨ§Ϋ ΩΨͺΩΨ§ΩΨͺ
{love} : ΨͺΩΨ§ΩΫ ΩΩΨ¨ ΩΨ§ 
{time} :  Ψ³Ψ§ΨΉΨͺ Ω Ψ―ΩΫΩΩ
{rand} : ΨΉΨ―Ψ―Ϋ Ψ±ΩΨ―ΩΩ Ψ¨ΫΩ Ϋ± ΨͺΨ§ Ϋ±Ϋ°Ϋ°Ϋ°
{emoji} : Ψ§ΫΩΩΨ¬Ϋ ΩΨ§Ϋ Ψ?Ψ§Ψ΅ 
{date} : ΨͺΨ§Ψ±ΫΨ? Ϊ©Ψ§ΩΩ
{day} : ΨͺΨ§Ψ±ΫΨ? (ΩΩΨ· Ψ±ΩΨ²)

Ψ¨Ψ±Ψ§Ϋ Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ψ§Ψ² ΩΨ±Ϊ©Ψ―Ψ§Ω Ψ§Ψ² ΩΨ§ΪΩ ΩΨ§Ϋ ΩΩΩ Ψ±Ψ§ ΩΩΨ±Ψ§Ω Ψ¨Ψ§ {} Ψ―Ψ§Ψ?Ω ΩΨͺΩ Ψ¬Ψ§ΫΪ―Ψ°Ψ§Ψ±Ϋ Ϊ©ΩΫΨ― π'''
            
            self.askclerk='''ΩΨ·ΩΨ§ ΩΎΫΨ§ΩΫ Ϊ©Ω ΩΫΨ?ΩΨ§ΩΫΨ― ΩΩΪ―Ψ§Ω Ψ§ΩΩΨ§ΫΩ Ψ΄Ψ―ΩΨͺΩΩ Ψ¨Ω Ϊ©Ψ³Ψ§ΩΫ Ϊ©Ω ΩΎΫΨ§Ω ΩΫΨ―ΩΩΨ― Ψ§Ψ±Ψ³Ψ§Ω Ψ΄ΩΨ― Ψ±Ψ§ Ψ¨ΩΨ±Ψ³ΨͺΫΨ― π:
Ω ΩΩΪΩΫΩ Ψ¨Ψ±Ψ§Ϋ Ψ­Ψ°Ω ΩΨ§ΪΩ Ϋ `None` Ψ±Ψ§ Ψ§Ψ±Ψ³Ψ§Ω ΩΩΨ§ΫΫΨ― . 
            
π‘ : Ψ§ΫΩ ΩΎΫΨ§Ω ΩΫΨͺΩΨ§ΩΨ― ΨΉΪ©Ψ³ Ψ ΩΫΩΩ ΫΨ§ ΩΨͺΩ ΫΨ§ ΩΨ±ΪΫΨ²Ϋ Ψ¨Ψ§Ψ΄Ψ― π'''

            self.duplicated= lambda  dup : f'π Ψ§ΫΩ  ΩΩΨ―Ψ§Ψ± ΩΨ¨ΩΨ§ Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω Ψ§Ψ³Ψͺ \n π‘ : {dup}'
            
            self.askdelbio = lambda  bios : f'''Ψ¨ΫΩ ΩΨ§Ϋ ΩΩΨ±Ψ― ΩΨΈΨ± Ψ±Ψ§ Ψ¨Ψ±Ψ§Ϋ Ψ­Ψ°Ω Ψ§Ψ±Ψ³Ψ§Ω Ϊ©ΩΫΨ― : 
π‘ ΩΫΨ³Ψͺ Ψ¨ΫΩ ΩΨ§ π‘ 
{bios}'''
            self.answer_setted= lambda word , answer : f'''ΩΎΨ§Ψ³Ψ? Ω Ϊ©ΩΩΩ Ϋ Ψ§Ψ±Ψ³Ψ§Ω Ψ΄Ψ―Ω Ψ§ΨΆΨ§ΩΩ Ψ΄Ψ― : 
            π© Ϊ©ΩΩΩ : `{word}`
            π© ΩΎΨ§Ψ³Ψ? : `{answer}`'''
            
            self.setting=lambda emoji , type_model , contacts , text_only , login , chat_model , defend , delsaver , chatsaver , randbio ,attack , spy , pvlock , gplock , a_j , a_p , answering , clean , read , reaction , wel , love , card , lchannel , mchannel , mainbio , clerk :f'''
πͺ© dev : @amiralirj_official 

ΩΨ―Ω ΨͺΨ§ΫΩΎ : {type_model}
ΩΩΨ· Ϊ©Ψ§ΩΨͺΪ©Ψͺ ΩΨ§ : {emoji(contacts)}
ΩΩΨ· ΩΨͺΩ : {emoji(text_only)}
Ψ§ΩΨͺΫ ΩΨ§Ϊ―ΫΩ : {emoji(login)}
Ψ­Ψ§ΩΨͺ ΪΨͺ :{chat_model}
Ψ­Ψ§ΩΨͺ Ψ§ΩΩ : {emoji(defend)}
Ψ§Ψ·ΩΨ§ΨΉ Ψ±Ψ³Ψ§ΩΫ ΩΎΨ§Ϊ© Ϊ©Ψ±Ψ―Ω ΩΎΫΨ§Ω : {emoji(delsaver)}
Ψ°Ψ?ΫΨ±Ω Ϊ©Ψ±Ψ―Ω ΪΨͺ Ψ―Ψ± Ψ―ΫΨͺΨ§Ψ¨ΫΨ³ : {emoji(chatsaver)}
Ψ¨ΫΩ ΩΨͺΨ­Ψ±Ϊ© : {emoji(randbio)}
Ψ­Ψ§ΩΨͺ Ψ­ΩΩΩ : {emoji(attack)}
Ψ¬Ψ§Ψ³ΩΨ³Ϋ : {emoji(spy)}
ΩΩΩ ΩΎΫΩΫ Ψ¬Ψ―ΫΨ― : {emoji(pvlock)}
ΩΩΩ Ϊ―Ψ±ΩΩ Ψ¬Ψ―ΫΨ― : {emoji(gplock)}
Ψ¬ΩΫΩ Ψ?ΩΨ―Ϊ©Ψ§Ψ± Ψ¨Ψ§Ψ²Ϋ : {emoji(a_j)}
Ψ¨Ψ§Ψ²Ϋ Ϊ©Ψ±Ψ―Ω Ψ?ΩΨ―Ϊ©Ψ§Ψ±  : {emoji(a_p)}
ΩΎΨ§Ψ³Ψ?Ϊ―ΩΫΫ Ψ?ΩΨ―Ϊ©Ψ§Ψ± : {emoji(answering)}
ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ Ψ?ΩΨ―Ϊ©Ψ§Ψ± : {emoji(clean)}
Ψ?ΩΨ§ΩΨ―Ω ΩΎΫΨ§Ω ΩΨ§ : {emoji(read)}
Ψ±Ϋ Ψ§Ϊ©Ψ΄Ω Ψ²Ψ―Ω : {reaction}
Ψ?ΩΨ΄Ψ§ΩΨ― Ϊ―Ω : {wel}
ΨΉΨ΄Ω : {love}
Ψ΄ΩΨ§Ψ±Ω Ϊ©Ψ§Ψ±Ψͺ : {card}
Ϊ©Ψ§ΩΨ§Ω ΩΨ§Ϊ― ΩΨ§ : {lchannel}
Ϊ©Ψ§ΩΨ§Ω ΩΎΫΨ§Ω ΩΨ§ : {mchannel}
Ψ¨ΫΩΫ Ψ§Ψ΅ΩΫ : {mainbio}
Ψ­Ψ§ΩΨͺ ΩΩΨ΄Ϋ : {clerk}
Ψ²Ψ¨Ψ§Ω : ΩΨ§Ψ±Ψ³Ϋ 

πͺ© dev : https://www.github.com/amiralirj
'''
            self.help = '''β TELEGRAM POWERFULL MANAGER β 
πͺ© DEV : https://www.github.com/amiralirj 
πͺ© DEV : @amiralirj_official 

π΄ Ψ¨Ψ?Ψ΄ ΩΨ§Ϋ Ϊ©ΩΫΨ―Ϋ ( on | off )  π’

β¦οΈread  `on` or `off` 
- Ψ³ΫΩ Ψ΄Ψ―Ω ΩΎΫΨ§Ω ΩΨ§ Ψ―Ψ± ΩΨ­ΨΈΩ

β¦οΈanswering `on` or `off`
- ΩΎΨ§Ψ³Ψ?Ψ―ΩΫ Ψ?ΩΨ―Ϊ©Ψ§Ψ± Ψ¨Ψ§ ΨͺΩΨ¬Ω Ψ¨Ω Ϊ©ΩΩΨ§Ψͺ Ψ§Ψ² ΩΎΫΨ΄ ΨͺΨΉΫΩ Ψ΄Ψ―Ω 

β¦οΈautoplay `on` or `off`
- Ψ¨Ψ§Ψ²Ϋ Ϊ©Ψ±Ψ―Ω Ψ?ΩΨ―Ϊ©Ψ§Ψ± @wererolfbot

β¦οΈautojoin `on` or `off`
- Ψ¬ΩΫΩ Ψ΄Ψ―Ω Ψ?ΩΨ―Ϊ©Ψ§Ψ± Ψ―Ψ± Ψ¨Ψ§Ψ²Ϋ  @wererolfbot

π₯delsaver `on` or `off`
- Ψ―Ψ± Ψ΅ΩΨ±Ψͺ ΩΎΨ§Ϊ© Ψ΄Ψ―Ω ΩΎΫΨ§Ω ΨͺΩΨ³Ψ· ΩΨ± Ϊ©Ψ§Ψ±Ψ¨Ψ±Ϋ Ψ³Ψ±ΫΨΉΨ§ Ψ’Ω ΩΎΫΨ§Ω Ω ΩΨ­ΨͺΩΨ§Ϋ Ψ’Ω Ψ―Ψ± Ϊ©Ψ§ΩΨ§Ω ΩΨ±ΩΨ§Ψ±Ψ― ΩΫΨ΄ΩΨ― 

β¦οΈcontacts `on` or `off`
- ΩΨ­Ψ―ΩΨ― Ϊ©Ψ±Ψ―Ω Ψ§ΩΨ±Ψ§Ψ―Ϋ Ϊ©Ω Ψ―Ψ± Ϊ©Ψ§ΩΨͺΪ©Ψͺ Ψ΄ΩΨ§ ΩΫΨ³ΨͺΩΨ― (ΩΩΨ· Ϊ©Ψ³Ψ§ΩΫ Ϊ©Ω Ψ¬Ψ²Ω Ϊ©Ψ§ΩΨͺΪ©ΨͺΨͺΩΩ ΩΨ³ΨͺΩΨ― ΩΫΨͺΩΨ§ΩΩΨ― Ψ¨Ω Ψ΄ΩΨ§ ΩΎΫΨ§Ω Ψ¨Ψ―ΩΩΨ―)

β¦οΈtexts `on` or `off`
- ΩΨ­ΨͺΩΨ§ ΩΨ§Ϋ ΨΉΪ©Ψ³ Ω ... ΩΎΨ§Ϊ© ΩΫΨ΄ΩΨ― Ω Ϊ©Ψ§Ψ±Ψ¨Ψ±Ψ§Ω ΩΩΨ· ΩΨ§Ψ―Ψ± Ψ¨Ω Ψ§Ψ±Ψ³Ψ§Ω ΩΎΫΨ§Ω Ψ―Ψ± ΩΩΨΉ ΩΨͺΩ Ψ¨Ω Ψ΄ΩΨ§ ΩΫΨ¨Ψ§Ψ΄ΩΨ―

β¦οΈantilogin `on` or `off`
- Ψ¨ΨΉΨ― Ψ§Ψ² Ψ±ΩΨ΄Ω Ψ΄Ψ―Ω Ϊ©Ψ³Ϋ ΩΩΫΨͺΩΨ§ΩΨ― ΩΨ§Ψ±Ψ― Ψ§Ϊ©Ψ§ΩΨͺ Ψ΄ΩΨ§ Ψ¨Ψ΄ΩΨ― 

β¦οΈsafe `on` or `off`
- Ψ­Ψ§ΩΨͺ Ψ§ΩΩ : Ϊ©Ψ³Ψ§ΩΫ Ϊ©Ω Ψ¨Ψ§ Ψ΄ΩΨ§ ΩΎΫΩΫ ΩΨ―Ψ§Ψ±ΩΨ― ΫΨ§ Ϊ©ΩΨͺΨ± Ψ§Ψ² 200 ΩΎΫΨ§Ω Ψ¨Ω Ψ΄ΩΨ§ Ψ―Ψ§Ψ―Ω Ψ§ΩΨ― Ψ§Ψ±Ψ΄ΫΩ Ω ΩΫΩΨͺ ΩΫΨ΄ΩΩΨ― 

β¦οΈrandbio `on` or `off`
- Ψ¨ΫΩ Ψ±ΩΨ―ΩΩ Ω ΪΨ±Ψ?Ψ΄Ϋ Ψ·Ψ¨Ω Ψ¬ΩΩΩ ΩΨ§ΫΫ Ϊ©Ω Ψ§Ψ² ΩΎΫΨ΄ ΨͺΨΉΫΫΩ Ϊ©Ψ±Ψ―ΫΨ―

β¦οΈattack `on` or `off`
- Ψ­Ψ§ΩΨͺ Ψ­ΩΩΩ : Ϊ©Ψ³Ψ§ΩΫ Ϊ©Ω Ψ¨Ψ§ Ψ΄ΩΨ§ ΩΎΫΩΫ ΩΨ―Ψ§Ψ΄ΨͺΩΨ― ΫΨ§ Ϊ©ΩΨͺΨ± Ψ§Ψ² 75 ΩΎΫΨ§Ω Ψ¨Ω Ψ΄ΩΨ§ Ψ―Ψ§Ψ―ΩΨ― Ψ¨ΩΨ§Ϊ© ΩΫΨ΄ΩΩΨ― (Ψ¨Ψ§ Ψ§Ψ·ΩΨ§ΨΉ Ψ―Ψ§Ψ―Ω Ψ­Ψ§ΩΨͺ Ψ­ΩΩΩ Ψ¨Ω Ψ’Ω ΩΨ§)

π₯saving `on` or `off`
- Ψ°Ψ?ΫΨ±Ω Ϊ©Ψ±Ψ―Ω Ω Ψ¨Ϊ© Ψ§ΩΎ Ϊ―Ψ±ΩΨͺΩ ΨͺΩΨ§ΩΫ ΪΨͺ ΩΨ§ , Ψ­ΨͺΫ Ψ§Ϊ―Ψ± ΪΨͺ ΩΨ§ ΩΎΨ§Ϊ© Ψ΄ΩΩΨ― ΩΫΨ² ΩΨ§Ψ¨Ω Ψ―Ψ³ΨͺΨ±Ψ³ Ψ?ΩΨ§ΩΨ― Ψ¨ΩΨ― 
- Ψ―Ψ³ΨͺΩΨ± Ϊ―Ψ±ΩΨͺΩ ΪΨͺ ΩΩΨ±Ψ― ΩΨΈΨ± : see [reply] or [id] 

π₯spy `on` or `off`
- Ψ­Ψ§ΩΨͺ Ψ¬Ψ§Ψ³ΩΨ³Ϋ : Ϊ©ΩΩΨ§ΨͺΫ Ϊ©Ω ΨͺΨΉΫΫΩ Ϊ©Ψ±Ψ―ΫΨ― Ψ¬Ψ§Ψ³ΩΨ³Ϋ Ψ΄ΩΩΨ― Ψ§Ϊ―Ψ± Ψ―Ψ± ΩΎΫΨ§ΩΫ Ψ―ΫΨ―Ω Ψ¨Ψ΄ΩΩΨ― Ψ³Ψ±ΫΨΉΨ§ Ψ’Ω ΩΎΫΨ§Ω Ψ¨Ω Ψ―Ψ± Ϊ©Ψ§ΩΨ§Ω ΫΨ§ Ψ³ΫΩ ΩΨ³ΫΨ¬ΨͺΩΩ ΩΨ±ΩΨ§Ψ±Ψ― ΩΫΨ΄ΩΩΨ― 

π₯cleaning `on` or `off`
- ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΩΎΫΩΫ ΩΨ§ ΩΨ±Ψ±ΩΨ² (Ψ¨Ψ¬Ψ² ΩΎΫΩ Ψ΄Ψ―Ω ΩΨ§) 

β¦οΈgrouplock `on` or `off`
- ΩΩΩ Ψ΄Ψ―Ω Ψ§Ψ― Ψ―Ψ± Ϊ―Ψ±ΩΩ ΩΨ§Ϋ Ψ¬Ψ―ΫΨ― ( Ψ±Ψ¨Ψ§Ψͺ Ψ―Ψ±Ψ¬Ψ§ Ψ¨ΨΉΨ― Ψ§Ψ² Ψ§Ψ― Ψ΄Ψ―Ω ΩΩΨͺ ΩΫΨ―ΩΨ―)

β¦οΈprivatelock `on` or `off`
- Ψ¨ΩΨ§Ϊ© Ψ΄Ψ―Ω ΩΎΫΩΫ ΩΨ§Ϋ Ψ¬Ψ―ΫΨ― ΩΩΨ±Ψ§Ω Ψ¨Ψ§ Ψ§Ψ·ΩΨ§ΨΉ Ψ¨Ω Ψ’ΩΩΨ§ Ϊ©Ω Ψ§ΫΩ ΩΩΩ ΩΨΉΨ§Ω Ψ§Ψ³Ψͺ  

β¦οΈbot `on` or `off`
- Ψ±ΩΨ΄Ω ΫΨ§ Ψ?Ψ§ΩΩΨ΄ Ψ΄Ψ―Ω Ψ±Ψ¨Ψ§Ψͺ



βββββββββββββββββ
π± Ψ¨Ψ?Ψ΄ ΩΎΫΨ΄Ψ±ΩΨͺΩ π±
> ΩΎΨ§Ψ³Ψ? Ϊ―ΩΫΫ Ψ?ΩΨ―Ϊ©Ψ§Ψ± π 
β§ clearanswers : ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΨͺΩΨ§Ω Ψ¬ΩΨ§Ψ¨ ΩΨ§Ϋ Ψ?ΩΨ―Ϊ©Ψ§Ψ±
β§ delanswer : ΩΎΨ§Ϊ© Ϊ©Ψ±Ψ―Ω ΫΪ© Ψ¬ΩΨ§Ψ¨
β§ answerlist : ΩΨ΄Ψ§ΩΨ―Ω Ϋ ΨͺΩΨ§Ω Ϊ©ΩΫΨ― ΩΨ§ Ω Ψ¬ΩΨ§Ψ¨ ΩΨ§
β§ addanswer : Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω Ψ¬ΩΨ§Ψ¨ Ω Ϊ©ΩΫΨ―
β
> Ψ¬Ψ§Ψ³ΩΨ³Ϋ π
β§ clearspies ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΨͺΩΨ§Ω Ϊ©ΩΩΨ§Ψͺ ΨͺΨ­Ψͺ ΩΨΈΨ± Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω
β§ delspy ΩΎΨ§Ϊ© Ϊ©Ψ±Ψ―Ω ΫΪ© Ϊ©ΩΩΩ
β§ spylist ΩΨ΄Ψ§ΩΨ―Ω Ϋ ΨͺΩΨ§ΩΫ Ϊ©ΩΩΨ§Ψͺ Ω Ψ¬ΩΩΩ ΩΨ§Ϋ ΨͺΨ­Ψͺ ΩΨΈΨ±
β§ addspy Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω Ϊ©ΩΩΩ ΫΨ§ Ψ¬ΩΩΩ Ψ¬ΩΨͺ Ψ¬Ψ§Ψ³ΩΨ³Ϋ 
β
> Ψ―Ψ΄ΩΩ β οΈ
β§ delenemy Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω Ψ―Ψ΄ΩΩ
β§ clearenemies ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΨͺΩΨ§ΩΫ Ψ―Ψ΄ΩΩ ΩΨ§ 
β§ addenemy [reply][id] Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω Ψ―Ψ΄ΩΩ 
β§ enemylist ΩΨ΄Ψ§ΩΨ―Ω Ϋ ΨͺΩΨ§ΩΫ Ψ―Ψ΄ΩΩΨ§Ω
β
> Ψ¨ΫΩ ΩΨͺΨ­Ψ±Ϊ© βοΈ 
β§ biolist ΩΫΨ³Ψͺ Ψ¨ΫΩ ΩΨ§Ϋ ΪΨ±Ψ?Ψ΄Ϋ Ω ΩΨͺΨ­Ψ±Ϊ©
β§ clearbioes ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΨͺΩΨ§ΩΫ Ψ¨ΫΩ ΩΨ§Ϋ Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω
β§ delbio ΩΎΨ§Ϊ© Ϊ©Ψ±Ψ―Ω ΩΩΨ· ΫΪ© Ψ¨ΫΩ
β§ addbio Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω Ψ¨ΫΩ
β
> Ψ­Ψ§ΩΨͺ ΩΩΨ΄Ϋ π€΅πΌββοΈ  
> Ψ§Ϊ―Ψ± ΩΨ±Ψ―Ϋ ΩΎΫΨ§Ω Ψ―ΩΨ― ΩΩΪ―Ψ§ΩΫ Ϊ©Ω Ψ΄ΩΨ§ Ψ§ΩΩΨ§ΫΩ ΩΨ³ΨͺΫΨ― Ψ§ΫΩ ΩΨ§Ψ¨ΩΫΨͺ ΩΎΫΨ§ΩΫ Ϊ©Ω Ψ΄ΩΨ§ Ψ«Ψ¨Ψͺ Ϊ©Ψ±Ψ―ΫΨ― Ψ±Ψ§ Ψ¨Ψ±Ψ§Ϋ Ψ’Ω ΩΨ±Ψ― ΩΫΩΨ±Ψ³ΨͺΨ―   
β§ clerk 
β
β§ setmainbio Ψ¨ΫΩΫ Ψ§Ψ΅ΩΫ Ϊ©Ω ΩΩΪ―Ψ§Ω Ψ?Ψ§ΩΩΨ΄ Ϊ©Ψ±Ψ―Ω Ψ¨ΫΩ ΩΨͺΨ­Ψ±Ϊ© Ψ¨Ψ± Ψ±ΩΫ ΩΎΨ±ΩΩΨ§ΩΨͺΩΩ ΩΨ±Ψ§Ψ± ΩΫΪ―ΫΨ±Ψ―
β
> ΩΨ§Ψ¨ΩΫΨͺ ΩΨ±ΩΨ΄Ϊ―Ψ§ΩΫ πͺ
β§ setcard Ψ«Ψ¨Ψͺ Ψ΄ΩΨ§Ψ±Ω Ϊ©Ψ§Ψ±Ψͺ ΫΨ§ ΩΨ± ΩΨͺΩ Ψ―ΫΪ―Ψ±Ϋ    
β§ card ΩΩΨ§ΫΨ΄ Ψ΄ΩΨ§Ψ±Ω Ϊ©Ψ§Ψ±Ψͺ ΫΨ§ ΩΨͺΩ Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω Ψ¨Ω Ψ³Ψ±ΨΉΨͺ
β
> ΨΉΨ΄Ω β₯οΈ 
> Ψ³Ψ§ΨΉΨͺ ΩΨ§Ϋ Ψ³Ψͺ Ω ΩΫΨ΄ ΨͺΨ§ΫΩ ΩΨ§ Ψ±Ψ§ Ψ¨Ψ§ ΩΩΨ¨ Ψ¨Ψ±Ψ§Ϋ ΩΨ±Ψ― Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω ΩΫΩΨ±Ψ³ΨͺΨ―
β§ dellove [in chat] Ψ§ΨΆΨ§ΩΩ Ϊ©Ψ±Ψ―Ω ΨΉΨ΄Ω
β§ setlove [in chat] Ψ­Ψ°Ω Ϊ©Ψ±Ψ―Ω ΨΉΨ΄Ω
β
> Ψ²Ψ¨Ψ§Ω Ψ±Ψ¨Ψ§Ψͺ
β§ `lang` `en` or `fa`
β
> Ψ?ΩΨ΄ Ψ§ΩΨ―Ϊ―ΩΫΫ π
β§ setwel 
β
> Ψ±Ϋ Ψ§Ϊ©Ψ΄Ω Ψ?ΩΨ―Ϊ©Ψ§Ψ± π€ͺ
> ΨͺΩΨ§ΩΫ ΩΎΫΨ§Ω ΩΨ§Ϋ ΩΨ±Ψ³ΨͺΨ§Ψ―Ω Ψ΄Ψ―Ω Ψ―Ψ± ΩΎΫΩΫ Ψ―Ψ± ΩΩΨ§Ω ΩΨ­ΨΈΩ Ψ§ΫΩΩΨ¬Ϋ Ψ«Ψ¨Ψͺ Ψ΄Ψ―Ω Ψ±Ψ§ Ψ±Ϋ Ψ§Ϊ©Ψͺ ΩΫΪ©ΩΩΨ― 
β§ reaction
β
> ΩΨΆΨΉΫΨͺ Ψ΄ΩΨ§ π’π―
> ΩΨΆΨΉΫΨͺΫ Ϊ©Ω Ψ¨Ψ§ΩΨ§Ϋ Ψ΅ΩΨ­Ω Ψ¨Ω ΩΩΨ§ΫΨ΄ Ψ―Ψ± ΩΫ Ψ’ΫΨ― (Ψ―Ψ±Ψ­Ψ§Ω ΩΩΨ΄ΨͺΩ . ...)
β§ status
β
> Ψ­Ψ§ΩΨͺ ΨͺΨ§ΫΩΎ π 
β§ typemodel
β
> Ψ―ΫΨ―Ω ΪΨͺ ΩΨ§Ϋ Ψ§Ψ±Ψ΄ΫΩ Ψ΄Ψ―Ω 
> Ψ¨Ψ±Ψ§Ϋ Ψ§Ψ³ΨͺΩΨ§Ψ―Ω Ω Ψ«Ψ¨Ψͺ ΪΨͺ ΩΨ§ Ψ§ΩΩ Ψ°Ψ?ΫΨ±Ω Ϋ ΩΎΫΨ§Ω ΩΨ§ Ψ±Ψ§ Ψ±ΩΨ΄Ω Ϊ©ΩΫΨ―
β§ see [reply][in chat][id] ΩΨ±Ψ³ΨͺΨ§Ψ―Ω ΩΨ§ΫΩ ΪΨͺ Ψ¨Ψ§ Ψ§ΩΩ ΩΨ±Ψ―
β§ allchats ΩΨ±Ψ³ΨͺΨ§Ψ―Ω ΨͺΩΨ§ΩΫ ΩΨ§ΫΩ ΩΨ§Ϋ ΪΨͺ 
β
π€ͺ Ψ³Ψ±Ϊ―Ψ±ΩΫ π€ͺ 
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
`mydel` ΩΎΨ§Ϊ©Ψ³Ψ§Ψ²Ϋ ΨͺΩΨ§ΩΫ ΩΎΫΨ§Ω ΩΨ§Ϋ Ψ?ΩΨ―
πͺ© DEV : https://www.github.com/amiralirj 
πͺ© DEV : @amiralirj_official 
'''


# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 .

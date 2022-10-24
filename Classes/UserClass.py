from Database.selfdata import database
from random import choice

class User:
    DataBase=database
    def __init__(self) -> None:
        self.dataBase=database
        details=self.dataBase.see_all
        self.user_id = int(details[0])
        self.Text_Change = int(details[1])
        self.Contacts_Only = bool(details[2])
        self.Text_Only = bool(details[3])
        self.Anti_Login = bool(details[4])
        self.Chat_Status = int(details[5])
        self.Safe_Mode = bool(details[6])
        self.Del_Saver = bool(details[7])
        self.Save_Chats = bool(details[8])
        self.Random_Bio = bool(details[9])
        self.Attack_Mode = bool(details[10])
        self.Spy = bool(details[11])
        self.New_Group_Lock = bool(details[12])
        self.New_Pv_Lock = bool(details[13])
        self.Auto_WerWolf_Join =bool(details[14])
        self.Auto_WerWolf_Play =bool(details[15])
        self.Auto_Answering =bool(details[16])
        self.Auto_Clean = bool(details[17])
        self.Auto_Read = bool(details[18])
        self.Auto_Reaction = str(details[19])
        if str(details[19]).lower()=='none':self.Auto_Reaction=None
        self.Welcomer = int(details[20])
        self.Love = str(details[21])
        if str(details[21]).lower()=='none':self.Love=None
        else:self.Love=int(self.Love)
        self.Card_Number = str(details[22])
        if str(details[22]).lower()=='none':self.Card_Number=None
        self.Log_Channel = str(details[23])
        if str(details[23]).lower()=='none':self.Log_Channel=None
        else:self.Log_Channel=int(self.Log_Channel)
        self.Messages_Channel=str(details[24])
        if str(details[24]).lower()=='none':self.Messages_Channel=None
        else:self.Messages_Channel=int(self.Messages_Channel)
        self.Bio_Text = str(details[25])
        if str(details[25]).lower()=='none':self.Bio_Text=None
        self.Offline_Answering = int(details[26])
        self.Lang = bool(int(details[27]))
        self.Bot = bool(int(details[28]))
    # ---------------------------------------------------------------
    @property  
    def show_bios(self):
        return self.dataBase.show_bios
    @property  
    def show_enemies(self):
        return self.dataBase.show_enemys
    @property  
    def show_spyes(self):
        return self.dataBase.show_spies
    @property  
    def show_answers(self):
        return self.dataBase.show_answers
    #---------------------------------------------------------------
    def add_bio(self,bio:str):
        self.dataBase.add_bio(str(bio))
    def add_enemy(self,user_id:int):
        self.dataBase.add_enemy(user_id) 
    def add_spy(self,word:str):
        self.dataBase.add_spy(word)
    def add_answer(self,word:str,answer:str):
        self.dataBase.add_answers(word,answer)
    #---------------------------------------------------------------
    def rem_bio(self,bio:str):
        self.dataBase.rem_bio(str(bio))
    def rem_enemy(self,user_id:int):
        self.dataBase.rem_enemy(user_id) 
    def rem_spy(self,word:str):
        self.dataBase.rem_spy(word)
    def rem_answer(self,word:str):
        self.dataBase.rem_answers(word)
    #--------------------------------------------------------------------------
    #-------------------------------| #Opiran |--------------------------------
    #--------------------------------------------------------------------------
    def change_bot(self,amount:bool):
        self.dataBase.change('Bot',int(amount))
        
    def change_lang(self,lang):
        self.dataBase.change('Lang',int(lang))
        
    def change_love(self,user_id):
        if str(user_id).lower() == 'none':self.dataBase.change('Love','None')
        else:self.dataBase.change('Love',str(int(user_id)))
        
    def change_clean(self,type:int):
        self.dataBase.change('Auto_Clean',int(type))
        
    def change_text_type(self,type:int):
        self.dataBase.change('Text_Change',int(type))
        
    def change_only_contacts(self,amount:bool):
        self.dataBase.change('Contacts_Only',int(amount))
        
    def change_only_texts(self,amount:bool):
        self.dataBase.change('Text_Only',int(amount))

    def change_anti_login(self,amount:bool):
        self.dataBase.change('Anti_Login',int(amount))

    def change_chat_status(self,amount:int):
        self.dataBase.change('Chat_Status',int(amount))
    
    def change_safe_mode(self,amount:bool):
        self.dataBase.change('Safe_Mode',int(amount))

    def change_del_saver(self,amount:bool):
        self.dataBase.change('Del_Saver',int(amount))
    
    def change_chat_saver(self,amount:bool):
        self.dataBase.change('Save_Chats',int(amount))

    def change_random_bio(self,amount:bool):
        self.dataBase.change('Random_Bio',int(amount))
    
    def change_attack_mode(self,amount:bool):
        self.dataBase.change('Attack_Mode',int(amount))
    
    def change_spying(self,amount:bool):
        self.dataBase.change('Spy',int(amount))
    
    def change_group_lock(self,amount:bool):
        self.dataBase.change('New_Group_Lock',int(amount))
    
    def change_pv_lock(self,amount:bool):
        self.dataBase.change('New_Pv_Lock',int(amount))
        
    def change_werewolf_j(self,amount:bool):
        self.dataBase.change('Auto_WerWolf_Join',int(amount))
    
    def change_werewolf_p(self,amount:bool):
        self.dataBase.change('Auto_WerWolf_Play',int(amount))
    
    def change_answering(self,amount:bool):
        self.dataBase.change('Auto_Answering',int(amount))
    
    def change_cleaning(self,amount:bool):
        self.dataBase.change('Auto_Answering',int(amount))
        
    def change_reading(self,amount:bool):
        self.dataBase.change('Auto_Read',int(amount))
    
    def change_reacting(self,amount:str):
        self.dataBase.change('Auto_Reaction',str(amount))
        
    def change_welcomer(self,amount:int):
        self.dataBase.change('Welcomer',int(amount))

    def change_card_num(self,amount:str):
        self.dataBase.change('Card_Number',str(amount))

    def change_lchannel(self,amount:str):
        self.dataBase.change('Log_Channel',int(amount))
    
    def change_mchannel(self,amount:str):
        self.dataBase.change('Messages_Channel',int(amount))
    
    def change_main_bio(self,amount:str):
        self.dataBase.change('Bio_Text',str(amount))
        
    def change_offline_answering(self,amount:int):
        self.dataBase.change('Offline_Answering',int(amount))
        
    def find_deleted(self,m_id):
        return self.dataBase.find_deleted(m_id)

    def load_message(self,c_id,m_id,text):
        self.dataBase.load_message(c_id,m_id,text)
        
    def emoji(self,amount):
        if amount :return '🟢'
        else:return '🔴'
        
    def __int__(self):
        return int(self.user_id)
    
    
    
# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 .
import sqlite3 as db

class Data:
    def __init__(self):
        self.con = db.connect(r"Rj-self.db" , detect_types=db.PARSE_DECLTYPES, check_same_thread = False)
        self.c = self.con.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS User (
            user_id INT PRIMARY KEY ,
            Text_Change INT , 
            Contacts_Only INT , 
            Text_Only INT ,
            Anti_Login INT ,
            Chat_Status INT ,
            Safe_Mode INT , 
            Del_Saver INT , 
            Save_Chats INT ,
            Random_Bio INT ,
            Attack_Mode INT ,
            Spy INT ,
            New_Group_Lock INT ,
            New_Pv_Lock INT , 
            Auto_WerWolf_Join INT ,
            Auto_WerWolf_Play INT ,
            Auto_Answering INT ,
            Auto_Clean INT ,
            Auto_Read INT , 
            Auto_Reaction TEXT , 
            Welcomer INT , 
            Love TEXT ,
            Card_Number TEXT , 
            Log_Channel TEXT , 
            Messages_Channel TEXT ,
            Bio_Text TEXT ,
            Offline_Answering INT ,
            Lang INT ,
            Bot INT 
            )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Enemy ( user_id INT PRIMARY KEY )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Spy ( word TEXT PRIMARY KEY )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Bio ( biograpgy TEXT PRIMARY KEY )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Answers ( word TEXT PRIMARY KEY , answer TEXT )''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Messages ( chat_id INT  , message_id INT , message_text TEXT  )''')
        self.con.commit()
        
    def add(self,user_id):
        self.c.execute('''INSERT OR IGNORE INTO User (user_id,Text_Change,Contacts_Only,Text_Only,Anti_Login,Chat_Status,Safe_Mode,Del_Saver,Save_Chats,Random_Bio,Attack_Mode,Spy,New_Group_Lock,New_Pv_Lock,Auto_WerWolf_Join,Auto_WerWolf_Play,Auto_Answering,Auto_Clean,Auto_Read,Auto_Reaction,Welcomer,Love,Card_Number,Log_Channel,Messages_Channel,Bio_Text,Offline_Answering,Lang,Bot)
                       VALUES 
                       (:user_id,:Text_Change,:Contacts_Only,:Text_Only,:Anti_Login,:Chat_Status,:Safe_Mode,:Del_Saver,:Save_Chats,:Random_Bio,:Attack_Mode,:Spy,:New_Group_Lock,:New_Pv_Lock,:Auto_WerWolf_Join,:Auto_WerWolf_Play,:Auto_Answering,:Auto_Clean,:Auto_Read,:Auto_Reaction,:Welcomer,:Love,:Card_Number,:Log_Channel,:Messages_Channel,:Bio_Text,:Offline_Answering,:Lang,:Bot)''',
                       {'user_id':int(user_id),'Text_Change':0,'Contacts_Only':0,'Text_Only':0,'Anti_Login':0,
                        'Chat_Status':0,'Safe_Mode':0,'Del_Saver':0,'Save_Chats':0,'Random_Bio':0,
                        'Attack_Mode':0,'Spy':0,'New_Group_Lock':0,'New_Pv_Lock':0,'Auto_WerWolf_Join':0,
                        'Auto_WerWolf_Play':0,'Auto_Answering':0,'Auto_Clean':0,'Auto_Read':0,
                        'Auto_Reaction':'None','Welcomer':0,'Love':'None','Card_Number':'None',
                        'Log_Channel':'None','Messages_Channel':'None','Bio_Text':'None','Offline_Answering':0,'Lang':0,'Bot':1})
        self.con.commit()
        
    def change(self,attribute,amount):
        self.c.execute(f'UPDATE User SET {attribute}=:Amount ',{'Amount':amount})
        self.con.commit()
    
    @property
    def see_all(self):
        self.c.execute('SELECT * FROM User ')
        FT=(self.c.fetchall())[0]
        return FT
    
        # return {'user_id':FT[0],'Text_Change':FT[1],'Contacts_Only':FT[2],'Text_Only':FT[3],'Anti_Login':FT[4],
        #         'Chat_Status':FT[5],'Safe_Mode':FT[6],'Del_Saver':FT[7],'Save_Chats':FT[8],'Random_Bio':FT[9],
        #         'Attack_Mode':FT[10],'Spy':FT[11],'New_Group_Lock':FT[12],'New_Pv_Lock':FT[13],'Auto_WerWolf_Join':FT[14],
        #         'Auto_WerWolf_Play':FT[15],'Auto_Answering':FT[16],'Auto_Clean':FT[17],'Auto_Read':FT[18],
        #         'Auto_Reaction':FT[19],'Welcomer':FT[20],'Love':FT[21],'Card_Number':FT[22],
        #         'Log_Channel':FT[23],'Messages_Channel':FT[24],'Bio_Text':FT[25],'Offline_Answering':FT[26],'Lang':FT[27],'Bot':FT[28]}
        
    def see(self,attribute):
        self.c.execute(f'SELECT {attribute} FROM User ')
        return (self.c.fetchall())[0][0]
    #--------------------------------------------------------------------------------------------
    def add_answers(self,word,answer):
        self.c.execute('INSERT  INTO Answers (word,answer) VALUES (:word,:answer)',{'word':word,'answer':answer})
        self.con.commit()
        
    def rem_answers(self,word):
        self.c.execute('DELETE FROM Answers WHERE  word=:word',{'word':word})
        self.con.commit()
        
    @property
    def show_answers(self):
        self.c.execute(f'SELECT * FROM Answers ')
        return [i for i in (self.c.fetchall())]
    #--------------------------------------------------------------------------------------------
    def add_enemy(self,user_id):
        self.c.execute('INSERT  INTO Enemy (user_id) VALUES (:User_id)',{'User_id':user_id})
        self.con.commit()
        
    def rem_enemy(self,user_id):
        self.c.execute('DELETE FROM Enemy WHERE  user_id=:user_id',{'user_id':user_id})
        self.con.commit()
        
    @property
    def show_enemys(self):
        self.c.execute(f'SELECT * FROM Enemy ')
        return [i[0] for i in (self.c.fetchall())]
    #--------------------------------------------------------------------------------------------
    def add_bio(self,bio):
        self.c.execute('INSERT  INTO Bio (biograpgy) VALUES (:biograpgy)',{'biograpgy':bio})
        self.con.commit()
        
    def rem_bio(self,bio):
        self.c.execute('DELETE FROM Bio WHERE  biograpgy=:biograpgy',{'biograpgy':bio})
        self.con.commit()
        
    @property
    def show_bios(self):
        self.c.execute(f'SELECT * FROM Bio ')
        return [i[0] for i in (self.c.fetchall())]
    #--------------------------------------------------------------------------------------------
    def add_spy(self,word):
        self.c.execute('INSERT  INTO  Spy (word) VALUES (:word)',{'word':word})
        self.con.commit()
        
    def rem_spy(self,word):
        self.c.execute('DELETE FROM Spy WHERE  word=:word',{'word':word})
        self.con.commit()
        
    @property
    def show_spies(self):
        self.c.execute(f'SELECT * FROM Spy ')
        return [i[0] for i in (self.c.fetchall())]
    
    def find_deleted(self,m_id):
        self.c.execute(f'SELECT chat_id,message_text FROM Messages WHERE  message_id=:mid',{'mid':m_id})
        return (self.c.fetchall())[0]
    
    def load_message(self,c_id,m_id,text):
        self.c.execute('INSERT  INTO  Messages (chat_id,message_id,message_text) VALUES (:chat_id,:message_id,:message_text)',{'chat_id':c_id ,'message_id':m_id,'message_text':text})
        self.con.commit()
        
database = Data()

# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 .
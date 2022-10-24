#  Copyright (c) 2019-2022 Dan <https://github.com/delivrance>
#  Copyright (c) 2022  <https://github.com/amiralirj>

'''RUN THIS FILE |>----<| EDIT Config -> __init__.py'''

import os , sys
SCRIPT_DIR = str(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(-1,(SCRIPT_DIR))

#------------------------------------| This will make Chat saving folder
from os import makedirs            #-|
makedirs('Chats',exist_ok=True)    #-|
del makedirs                       #-|
#------------------------------------|   

del os
del sys

print('\n\n\n')
print('\x1b[6;30;42m','Github : www.github.com/amiralirj ', '\x1b[0m')
print('telegram : @amiralirj_official \n\n')


from Classes.CliClass import Rjself

if __name__ == "__main__":
        
    cli=Rjself() 
    
    with cli : 
        PEERID=(cli.get_me()).id
        cli.start_robot(PEERID)
        cli.create_log_channels()
    
    cli.OP_IRAN() # start schedular tasks every minutes 
    print('Trying to connect ...')
    cli.run() # start() , idle()
    print('Im offline now , bye bye :) ')
    
    
# @amiralirj_official  - https://www.github.com/amiralirj
# 2022 - 
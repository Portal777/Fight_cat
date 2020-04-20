import sys
from db_logic import *
from enter_logic import *
from main_menu_logic import *

lib1 = Engine('proj_lib1')
lib2 = Engine('proj_lib2')

print(lib1.find_user_name('Portal'))

lib1.print_all_user()



print(sys.modules)

print(login_user)

db_logic.lib1.__add_bot()

"""
Constant strings for cluster tools, mostly boilerplate for generating files
"""

DBMODULE_DISCOVERABLE_INIT = '''"""
AUTOGENERATED INIT FILE FOR DBMODULE
"""
from os.path import dirname, exists, join, split
from citrine import CitrineDB
DB_ID = split(dirname(__file__))[1]
DB_PATH = join(dirname(__file__), DB_ID)
db = lambda: CitrineDB(DB_PATH) if exists(DB_PATH) else CitrineDB.new(DB_PATH, database_name=DB_ID)
DISCOVERABLE = True
'''

DBMODULE_UNDISCOVERABLE_INIT = '''"""
AUTOGENERATED INIT FILE FOR DBMODULE
"""
from os.path import dirname, exists, join, split
from citrine import CitrineDB
DB_ID = split(dirname(__file__))[1]
DB_PATH = join(dirname(__file__), DB_ID)
db = lambda: CitrineDB(DB_PATH) if exists(DB_PATH) else CitrineDB.new(DB_PATH, database_name=DB_ID)
DISCOVERABLE = False
'''

# Shorthand, basically a default value
DBMODULE_INIT = DBMODULE_DISCOVERABLE_INIT

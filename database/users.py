from motor.motor_asyncio import *
from config import *
from domainers import *
client = AsyncIOMotorClient(DATABASE_URL)
db = client[DATABASE_NAME]
col = db["users"]


async def get_user(user_id):
    user_id = int(user_id)
    user = await col.find_one({"user_id": user_id})
    if not user:
        res = {
            "user_id": user_id,
            "method":"MdiskPro",
            "shortener_api": None,
            "mdisk_api": None,
            "header_text": "",
            "footer_text": "",
            "username": None,
            "base_site": "GreyMatterslinks.in",
            "banner_image": None,
            "is_banner_image": True,
            "is_username": True,
            "is_header_text": True,
            "is_footer_text": True,
            "include_domain": [],
            "exclude_domain": [],
            "banned": False
        }
        await col.insert_one(res)
        user = await col.find_one({"user_id": user_id})

    return user

async def update_user_info(user_id, value:dict, tag="$set"):
    user_id = int(user_id)
    myquery = {"user_id": user_id}
    newvalues = {tag : value }
    await col.update_one(myquery, newvalues)

async def filter_users(dict):
    return col.find(dict)

async def total_users_count():
    return await col.count_documents({})

async def get_all_users():
    return col.find({})

async def delete_user(user_id):
    await col.delete_one({'user_id': int(user_id)})

async def total_users_count():
    return await col.count_documents({})

async def is_user_exist(id):
    user = await col.find_one({'user_id':int(id)})
    return bool(user)
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""

import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5472143789:AAF5Wm1WZqGHnH_Uvmj0iVfWrNtsUadslGc')
API_ID =  os.environ.get('api_id','18641760')
API_HASH = os.environ.get('api_hash','b7b026ce9d1d36400c02dc21d8df53a3')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','adryes95').split(';')
#ACCES_USERS = ('tl_admin_user','adryes95','Dr_Stranger0_0')
#ACCES_USERS = os.environ.get(ACCES_USERS)
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc',''))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import datetime
import time
import webbrowser
import user_agent
from user_agent import generate_user_agent
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR KEY : "+id)
  try:
    httpCaht = requests.get("https://pastebin.com/P9gAMfFC").text
    if id in httpCaht:
      print("\033[92m تم تفعيل كودك بنجاح نشكرك على تواصلك معنا")
      msg = str(os.geteuid())
      
      pass
    else:
      print("\x1b[91m كودك غير مفعل قم بارسال الكود الى المطور ليتم تفعيله يوزر المطور @ESP_OMAR تواصل تلكرام فقط")
      
      sys.exit()
  except:
    sys.exit()
    chk()
   
chk()
   
chk()
na = webbrowser.open('https://t.me/ESP_OM')
try:
	import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ses = requests.Session()
F = '\033[2;32m'
Z = '\033[1;31m' 
L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('O M A R', colors=['red', 'white'], align='center')
print(output)
token=input(' TOKEN : ')
ID=input(' ID : ')
pretty.install()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

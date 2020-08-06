import subprocess
import re

# netsh wlan show profile
# netsh wlan show profile <Name> key=clear

class Saved_Wifi_Password:
    def __init__(self):
        self.usernm = []
        self.passwd = []
        self.Get_Username()
        self.Get_Password()
        self.Print_Credentials()

    def Get_Username(self):
        output = subprocess.run(["netsh", "wlan", 'show', 'profile'], shell=False, capture_output=True)
        cmd_output = output.stdout.decode('utf-8')

        pattern = r'Profile\s.+'
        profiles = re.findall(pattern, cmd_output)
        for profile in profiles:
            tmp = profile.split(': ')[1]
            self.usernm.append(tmp[0:-1])

    def Get_Password(self):
        for user in self.usernm:
            output = subprocess.run(["netsh", "wlan", 'show', 'profile', user, 'key=clear'], shell=False, capture_output=True)
            cmd_output = output.stdout.decode('utf-8')

            pattern = r'Key\sContent.+'
            regex = re.compile(pattern)
            tmp = regex.search(cmd_output)
            password = tmp.group().split(': ')[1]
            self.passwd.append(password)

##            pattern = r'Key\sContent.+'
##            tmp = re.findall(pattern, cmd_output)   # Return a list
##            password = tmp[0].split(': ')[1]        # Only 1 match ==> tmp[0]; Get the password ==> split(': ')[1]
##            print(password[0:-1])                   # Have \r at the end of strings

    def Print_Credentials(self):
        x = max(len(user) for user in self.usernm)
        for i in range(0, len(self.usernm)):
            print(self.usernm[i] + " "*(x-len(self.usernm[i])) + "    : " + self.passwd[i])

if __name__=='__main__':
    x = Saved_Wifi_Password()
    input()

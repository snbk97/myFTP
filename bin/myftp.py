import ftplib
import time
import getpass

_author_ = "Sayan Bhowmik"


# url = "speedtest.tele2.net"
# url = "ftp.cs.brown.edu"

def putURL():
    a = raw_input("Enter FTP location: ")
    return a


def getin():
    uname = raw_input("Enter your username: ")
    pword = getpass.getpass("Enter your password: ")

    try:
        ftp.login(uname, pword)
        print "\n[*] Logged In"

    except:
        print "\n[-]Login Failed \n Check login credentials again"
        print "\n"
        time.sleep(5)
        getin()

header = '''
   _    _    _    _    _  
  / \  / \  / \  / \  / \ 
 ( m )( y )( F )( T )( P )
  \_/  \_/  \_/  \_/  \_/ 
  '''
print header
print "\n\n [*] For help, use '?' command after LOGGING IN\n\n"
url = putURL()
ftp = ftplib.FTP(url)
getin()


def ls():
    curr = ftp.pwd()
    time.sleep(2)
    dir_list = ftp.nlst(curr)
    dir_list.sort()
    for i in dir_list:
        i.replace('/', '')
        if('.' in i):
            print ("\t- " + i[0:])

        else:
            print ("[+] " + i[0:])

dir = ""


def cd(dir):
    try:
        ftp.cwd(dir)

    except:
        print ("[-] Error Occured. Please check Directory Lisiting again" +
               "\n\t" + "[*]HELP: ls()\n\n")


def bye():
    ftp.quit()
    print "Good Bye !"


def setTransferMode(MODE):
    if (MODE == "binary"):
        ftp.sendcmd("TYPE i")

    if (MODE == "ascii"):
        ftp.sendcmd("TYPE A")


def download(item):
    try:
        ftp.retrbinary('RETR ' + item, open(item, 'wb').write)
    except:
        print "[!] File Name Error"


def upload(item):
    ftp.sendcmd("TYPE i")
    filename = item
    ext = filename.split('.')[1]
    if ext in ("txt", "html", "htm"):
        ftp.sendcmd("TYPE i")
        myfile = open(filename)
        ftp.storlines("STOR " + filename, myfile)
        print "\t\t [test] no rb"
        ftp.sendcmd("TYPE A")

    else:
        ftp.sendcmd("TYPE i")
        myfile = open(filename, 'rb')
        ftp.storlines("STOR " + filename, myfile, 1024)
        print "\t\t [test] with rb"
        ftp.sendcmd("TYPE A")


def myhelp():
    a = '''
-------------------------
myFTP HELP
-------------------------


Here are all the available commands:
    
    [*] ? - see all available commands

    [*] help - see all available commands

    [*] ls - to list the names of the files in the current remote directory

    [*] cd <dir>  - to change directory on the remote machine

    [*] get <filename> - to copy one file from the remote machine to the local machine

    [*] put <filename> -t o copy one file from the local machine to the remote machine

    [*] set MODE <binry/ascii> - set transfer mode <binary/ascii>

    [*] bye - quits the current ftp connect and closes appliation

        '''
    print a

caret = ">> "
cmd = str(raw_input(caret))
while(cmd != "bye"):
    chk = cmd.split(" ")
    if (chk[0] == "ls"):
        ls()
        cmd = raw_input(caret)
    elif (chk[0] == "cd"):
        cd(chk[1])
        cmd = raw_input(caret)
    elif (chk[0] == "get"):
        download(chk[1])
        cmd = raw_input(caret)
    elif (chk[0] == "help" or chk[0] == "?"):
        myhelp()
        cmd = raw_input(caret)
    elif (chk[0] == "put"):
        upload(chk[1])
        cmd = raw_input(caret)
    elif (chk[0] == "set" and chk[1] == "MODE" and chk[2] == "binary"):
        setTransferMode("binary")
        print "Transfer MODE set to Binary"
        cmd = raw_input(caret)

    elif (chk[0] == "set" and chk[1] == "MODE" and chk[2] == "ascii"):
        setTransferMode("ascii")
        print "Transfer MODE set to Ascii"
        cmd = raw_input(caret)
    else:
        print "Unrecognized command given"
        cmd = raw_input(caret)


print "\n\t[-] Quitting..."
bye()
time.sleep(3)

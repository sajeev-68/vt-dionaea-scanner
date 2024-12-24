
import utils.getfiles as getfiles
import utils.setup as setup
import utils.send_bins as sendbins
import os
import datetime

def vt_call():
    now = datetime.datetime.now()
    file = "master.log"


    if os.path.exists(file):
        f = open(file, "a")
        f.write("\n[+] Updating master log file\n" )
    else:
        setup.set_cron_prompt()
        setup.create_logfiles()
        setup.set_vt_api()
    

    new_binaries = getfiles.getnewfiles_as_list()
    f1 = open("api_key.txt", "r")

    if not new_binaries == False:
        key = f1.read()
        sendbins.getreports(new_binaries, key)

    else:
        f.write(str(now))
        f.write("\n[-] No new binaries found as of now!\n")


if __name__ == "__main__":
    vt_call()
    

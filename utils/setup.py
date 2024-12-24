import datetime

now = str(datetime.datetime.now())

def set_cron_prompt():
    print(now, "\nSetup cronjob for your desired time")
    input("\nPress Enter to continue")
    return True

def create_logfiles():
    try:
        f = open("master.log", 'x')
        f1= open("file.log", 'x')
    
    except OSError:
        print('cannot create/open file')
        SystemExit
    f.write(now)
    f.write('\n[+]: Master Log file created! \n')
    f1.write(now)
    f1.write('\n[+]: File Log created! \n')
    f.close()
    f1.close()

    print("\n[+] Created log files!")
    return True

def set_vt_api():
    try:
        f = open("api_key.txt", "r")
    except OSError:
        print("\nVT-API key file error")
        SystemExit

    if not f.read(1):
        print("\nNo API key provided")
        return True

import vt
import datetime
import os

now = datetime.datetime.now()


def getreports(bins, api_key):

    for i in bins:

        f = open("file.log", 'a')
        f2 = open("master.log", "a")
        f3 = open("files.txt","a")
        f2.write(str(now))
        f2.write("\n[i]  New file found Hash, getting reports!\n")

        with vt.Client(api_key) as client:
            safe_path = i.replace('\n', '').replace('\r', '').strip()
            data = "/files/" + safe_path
            response = client.get_object(data)
            meaningful_name = response.get('meaningful_name')
            label = response.get('popular_threat_classification', {}).get('suggested_threat_label')
            reputation = response.get('reputation')
            sandbox_verdicts=response.get('sandbox_verdicts'),
            total_votes=response.get('total_votes')

        new_name = "/home/<ur_directory_here>/tpotce/data/dionaea/binaries/"+meaningful_name + ".details"  #change directory name to reflect your system
        
        f1 = open(new_name, "x")
        data = str(str(now) +"\n" +meaningful_name+"\n"+label+"\n"+str(reputation)+"\n"+"-------------------------------\n")
        f.write(data)
        data1 = str("\n" +str(now) + "\n"+label+"\n"+str(reputation)+"\n"+str(sandbox_verdicts)+"\n"+str(total_votes)+"\n")
        f1.write(data1)
        data3 = meaningful_name + ".details" + "\n" + meaningful_name + "\n"
        f3.write(data3)

        old_file = "/home/<ur_directory_here>/tpotce/data/dionaea/binaries/" + i  #change directory name to reflect your system

        new_meaningful_name = "/home/<ur_directory_here>/tpotce/data/dionaea/binaries/" + meaningful_name  #change directory name to reflect your system    
        os.rename(old_file, new_meaningful_name)
        f1.close()
        f.close()
        f2.close()
        f3.close()


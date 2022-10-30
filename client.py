import subprocess
import api
import time


machine_name = api.create_machine()
print("machine created!")

while True:
    print("wait for server!")
    machine = api.get_machine(machine_name)
    if machine.get("stop") == "n":
        if machine.get("status") == "ready":
            api.update_machine_status(machine_name,"downloading")
            subprocess.run("wget http://185.242.163.237/"+machine_name+".zip", shell=True)
            api.update_machine_status(machine_name, "unziping")
            subprocess.run("unzip " + machine_name + ".zip", shell=True)

            api.update_machine_status(machine_name, "runing")
            subprocess.run("puredns resolve -r resolvers.txt input.txt --write valid_output.txt", shell=True)
            with open("valid_output.txt","r") as readFile:
               for sub in readFile.readlines():
                   api.add_subdomain_to_db(machine.get("focus"),sub)

            subprocess.run("rm input.txt", shell=True)
            subprocess.run("rm "+machine_name+".zip", shell=True)
            api.update_machine_status(machine_name, "waiting")
        else:
           print("Timeout 10s")
           time.sleep(10)

    else:
        print("Makine durduruldu.")
        time.sleep(10)



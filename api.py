import requests
import json
import time



token = input("Token:")
telegram_api_key = input("Telegram Api Key:")
API = "http://185.242.163.237:5000/hardfox/api/v1"

def create_machine():
    name = input("machine name:")
    machinies = {"name": name,"token":token}
    while True:
        try:
            req = requests.post(API+"/machines",json=machinies)
            print(req.content)
            req.close()
            break
        except:
            print("Sunucuya ulasilamadi 10s timeout")
            time.sleep(10)

    json_object = json.dumps(machinies, indent=4)
    with open("config.json", "w") as outfile:
       outfile.write(json_object)

    return name



def get_machine(name):
    while True:
        try:
            req = requests.get(API+"/machines?name="+name)
            response_json = json.loads(req.text)
            req.close()
            return response_json

        except:
            print("Sunucuya ulasilamadi 10s timeout")
            time.sleep(10)




def update_machine_status(machine_name,status):
    data = {"name":machine_name,"status":status,"token":token}
    while True:
        try:
            req = requests.post(API+"/machines/status", json=data)
            print(req.content)
            req.close()
            break
        except:
            print("Sunucuya ulasilamadi 10s timeout")
            time.sleep(10)


def add_subdomain_to_db(domain,subdomain):
    while True:
        try:
            telegram_req = requests.get("https://api.telegram.org/bot"+telegram_api_key+"/sendMessage?chat_id=-880327745&text="+str(subdomain))
            telegram_req.close()
            break
        except:
            print("Telegram botuna ulasilamadi 10s timeout")
            time.sleep(10)
            

    data = {"domain": domain, "subdomain": subdomain,"token":token}
    while True:
        try:
            req = requests.post(API+"/subdomains",json=data)
            print(req.content)
            req.close()
            break
        except:
            print("Sunucuya ulasilamadi 10s timeout")
            time.sleep(10)



import requests
import json




token = input("Token:")
telegram_api_key = input("Telegram Api Key:")
API = "http://185.242.163.237:5000/hardfox/api/v1"

def create_machine():
    name = input("machine name:")
    machinies = {"name": name,"token":token}
    req = requests.post(API+"/machines",json=machinies)
    print(req.content)
    req.close()

    json_object = json.dumps(machinies, indent=4)
    with open("config.json", "w") as outfile:
       outfile.write(json_object)

    return name



def get_machine(name):
    req = requests.get(API+"/machines?name="+name)
    response_json = json.loads(req.text)
    return response_json



def update_machine_status(machine_name,status):
    data = {"name":machine_name,"status":status,"token":token}
    req = requests.post(API+"/machines/status", json=data)
    print(req.content)
    req.close()


def add_subdomain_to_db(domain,subdomain):
    telegram_req = requests.get("https://api.telegram.org/bot+"+telegram_api_key+"/sendMessage?chat_id=-880327745&text="+str(subdomain))
    data = {"domain": domain, "subdomain": subdomain,"token":token}
    req = requests.post(API+"/subdomains",json=data)
    print(req.content)
    req.close()



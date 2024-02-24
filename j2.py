from json import *

file_path = "C:/Users/Home/Desktop/PyLab4/json/sample-data.json"

try:
    with open(file_path) as f:
        data = load(f)
        print("Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")
        for x in data["imdata"]:
            dn = x["l1PhysIf"]["attributes"]["dn"]
            while len(dn) < 48:
                dn += " "
            descr = x["l1PhysIf"]["attributes"]["descr"]
            while len(descr) < 22:
                descr += " "
            speed = x["l1PhysIf"]["attributes"]["speed"]
            while len(speed) < 9:
                speed += " "
            mtu = x["l1PhysIf"]["attributes"]["mtu"]
            print(dn, descr, speed, mtu)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

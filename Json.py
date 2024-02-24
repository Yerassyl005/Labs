from json import *

j = open('sample-data.json')
data = load(j)
print('Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------')
for x in data['imdata']:
    dn = x['l1PhysIf']['attributes']['dn']
    while len(dn)<48: dn+=' '
    descr = x['l1PhysIf']['attributes']['descr']
    while len(descr)<22: descr+=' '
    speed = x['l1PhysIf']['attributes']['speed']
    while len(speed)<9: speed+=' '
    mtu = x['l1PhysIf']['attributes']['mtu']
    print(dn, descr, speed, mtu)
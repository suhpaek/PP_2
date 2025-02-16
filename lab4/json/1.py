import json

with open("C:\\Users\\ASUS\\PP_2\\lab4\\json\\sample.json", "r") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface status")
print("================================================================================")
print("{:<55} {:<16} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
print("-------------------------------------------------- --------------------  ------  ------")

for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "-"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<55} {:<16} {:<8} {:<8}".format(dn, descr, speed, mtu))
interfaces = ["Gi0/0/1", "Gi0/0/2", "Gi0/1/1"]

for interface in interfaces:
    print(interface)

print("\n")

for i in range(5):
    print(i, end=",")

print("\n")

for vlan_id in range(10, 15):
    print(vlan_id, end=",")

print("\n")

for port in range(1, 10, 2):
    print(port, end=",")

print("\n")

for port in range(10, 0, -1):
    print(port, end=",")

print("\n")

switches = ["core-sw-01", "dist-sw-02", "access-sw-03"]

for switch in switches:
    print(f"Yapılandırma kontrol ediliyor: {switch}")

print("\n")

switches = ["core-sw-01", "dist-sw-02", "access-sw-03"]

for i, switch in enumerate(switches):  # range(len(switches)) yerine
    print(f"{i}: {switch}")

for i, switch in enumerate(switches, start=1):
    print(f"{i}. {switch}")

print("\n")

attempts = 0

while attempts < 3:
    print(f"Bağlantı denemesi: {attempts + 1}")
    attempts += 1

while True:
    komut = input("Komut gir (çıkmak için 'q'): ")
    if komut == "q":
        break
    print(f"Çalıştırılıyor: {komut}")

print("\n")

vlans = [10, 20, 30, 99, 40]

for vlan in vlans:
    if vlan == 99:
        print(f"VLAN:{vlan} bulundu, durduruluyor.")
        break
    print(f"VLAN {vlan} işleniyor")

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)

print("\n")

ports = [1, 2, 0, 4, -1, 6]

for port in ports:
    if port <= 0:
        continue
    print(f"Port {port} taranıyor")

i = 0
while i < 10:
    i += 1  # continue'dan önce
    if i % 2 == 0:
        continue
    print(i)

print("\n")

vlans = [1, 2, 3, 4, 5]

for vlan in vlans:
    if vlan == 1:
        pass   # TODO: default VLAN için ayrı bir şey ekleyeceğim gibi gibi
    else:
        print(f"VLAN {vlan} yapılandırılıyor")

print("\n")

switches = ["core-sw01", "dist-sw-02", "access-sw-03"]
aranan = "dist-sw-04"

for switch in switches:
    if switch == aranan:
        print(f"{aranan} bulundu.")
        break
else:
    print(f"{aranan} listede yok.")  # for..else devreye girdi

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Deneme {attempts + 1}")
    attempts += 1
    if attempts == 2:
        break
else:
    print("Tüm denemeler tükendi, break hiç olmadı.")  # while...else - break ile kestim çalışmadı

print("\n")

for i in range(3, 20, 3):
    print(i)

for i in range(1, 20):
    if i % 3 != 0:
        continue
    print(i)

interfaces = ["Gi0/0/1", "Gi0/0/2", "Gi0/1/1"]

for interface in interfaces:
    if interface == "Gi0/0/1":
        print("Buldum: ", interface)
        break
else:
    print("Bulamadım.")

while True:
    giris = int(input("VLAN ID gir: "))

    if giris == 1:
        break
    elif giris < 0:
        continue
    elif giris > 0:
        print(giris)
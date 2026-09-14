import time

#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

ip = "10.0.0.1"
port = 22

print(ip, port)
print("IP:", ip)

print("10.0.0.1", "Gi0/0/1", "up")

print("10.0.0.1", "Gi0/0/1", "up", sep=" | ")

print("192", "168", "10", "5", sep=".")

print("Bağlanıyor", end="... ")
print("bağlandı!")

rapor = open("audit.txt", "w", encoding="utf-8")

print("Cihaz: core-sw-01", file=rapor)
print("Durum: compliant", file=rapor)

rapor.close()

print("Rapor dosyaya yazıldı.")

# Linux Bash'de çalıştırmak lazım (benim için) --> flush.py
print("Yükleniyor", end="")
for i in range(3):
    print(".", end="")
    time.sleep(2)
print("\nTamamlandı!\n")

print("Yükleniyor", end="")
for i in range(3):
    print(".", end="", flush=True)  # flush=True
    time.sleep(2)
print("\nTamamlandı!")

hostname = "core-sw-01"
latency = 4.567
loss = 0.0

print(f"Host: {hostname} | Latency: {latency:.1f}ms | Loss: {loss:.2f}%")

cihazlar = [
    ("10.0.0.1", "core-sw-01", "up"),
    ("10.0.0.2", "core-sw-02", "down"),
]

print(f"{'IP':<15}{'HOSTNAME':<15}{'DURUM'}")
print("-" * 38)
for ip, isim, durum in cihazlar:
    print(f"{ip:<15}{isim:<15}{durum}")

isim = input("Switch ismini girin: ")
print(f"Seçilen cihaz: {isim}")

vlan = input("VLAN ID girin: ")  # her zaman string - 100 verdik diyelim

print(type(vlan))
#print(vlan + 50)
# TypeError: can only concatenate str (not "int") to str

vlan_str = input("VLAN ID girin: ")

try:
    vlan = int(vlan_str)
    print(f"VLAN {vlan + 10} oluşturuldu.")
except ValueError:
    print("HATA: Lütfen bir sayı girin!")

cevap = input("Durum (up/down): ")  # up - sonda boşluk

print(cevap == "up")  # "up " != "up"

cevap = input("Durum (up/down): ").strip().lower()

if cevap == "up":
    print("Interface active")
elif cevap == "down":
    print("Interface deactive")
else:
    print("Anlaşılamadı, 'up' veya 'down' yazın.")

while True:
    giris = input("VLAN ID (1-4094): ").strip()
    try:
        vlan = int(giris)
        if 1 <= vlan <= 4094:
            break
        print("VLAN 1-4094 arasında olmalı.")
    except ValueError:
        print("Sayı girmediniz, tekrar deneyin.")

print(f"VLAN {vlan} onaylandı.")

"""
Eğer CTRL + D ile sonlandırırsam:

VLAN ID (1-4094): Traceback (most recent call last):
  File "/home/berkay/Desktop/Python-All/Tutorial/Input-Output/inp_out.py", line 89, in <module>
    giris = input("VLAN ID (1-4094): ").strip()
            ~~~~~^^^^^^^^^^^^^^^^^^^^^^
EOFError
"""

try:
    ip = input("Cihaz IP'si: ").strip()
except EOFError:
    ip = ""
    print("\nGirdi iptal edildi.")

# CTRL + C
try:
    ip = input("Cihaz IP'si: ").strip()
except (EOFError, KeyboardInterrupt):
    ip = ""
    print("\nGirdi iptal edildi.")

print("\n")

while True:
    hostname = input("Switch hostname: ").strip()
    if hostname:
        break
    print("Hostname boş olamaz.")

while True:
    giris = input("VLAN ID (1-4094): ").strip()
    try:
        vlan_id = int(giris)
        if 1 <= vlan_id <= 4094:
            break
        print("Aralık dışı! 1-4094 arası girin.")
    except ValueError:
        print("Sayı değil! Tekrar deneyin.")

vlan_name = input("VLAN ismi (boş = otomatik): ").strip()
if not vlan_name:
    vlan_name = f"VLAN{vlan_id}"

print(f"hostname {hostname}")
print(f"vlan {vlan_id}")
print(f" name {vlan_name}")
print("-" * 20)

onay = input("Bu config'i onaylıyor musunuz? (e/h): ").strip().lower()

if onay == "e":
    print(f"{hostname} için VLAN {vlan_id} onaylandı.")
else:
    print("İşlem iptal edildi.")

while True:
    ip = input("ip adresi gir: ").strip().split(".")

    if len(ip) != 4:
        print("ip adresi gir: 192.168.1.1 gibi")
        continue

    try:
        oktetler = (int(p) for p in ip)

        if all(0 <= oktet <= 255 for oktet in oktetler):
            break
        print("Her oktet 0-255 arası olmalı.")
    except ValueError:
        print("ip adresi gir!")

hedef_ip = input("Hedef IP girin: ").strip()
deneme_sayisi = int(input("Deneme sayısı: "))

for i in range(1, deneme_sayisi + 1):
    print(f"Hedef {i}. deneme: başarılı", flush=True)
    time.sleep(0.5)

hostname = input("Hostname girin: ").strip()
interface = input("Interface girin (örn: eth0): ").strip()
durum = input("Durum girin (up/down): ").strip()

with open("rapor.txt", "a", encoding="utf-8") as dosya:
    print(f"{hostname:<15} {interface:<15} {durum:<15}", file=dosya)

print("rapor yazıldı")

while True:
    ip = input("IP adresi girin: ").strip()
    print(f"Girdiğiniz IP: {ip}")

    onay = input("Bu IP doğru mu? (e/h): ").strip().lower()

    if onay == "e":
        print("İşlem onaylandı, program sonlandırılıyor.")
        break
    elif onay == "h":
        print("Tekrar deneyin.\n")
    else:
        print("Geçersiz seçim! Lütfen 'e' veya 'h' yazın.\n")
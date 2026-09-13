hostname = "core-sw-01"

hostname.upper()
print(hostname)  # Immutable

hostname = hostname.upper()
print(hostname)

a = "merhaba"
b = 'merhaba'
print(a == b)

mesaj = 'Switch "core-sw-01" yeniden başlatıldı'
print(mesaj)

#mesaj = 'Switch 'core-sw-01' yeniden başlatıldı'
#print(mesaj)
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

bos = ""
print(len(bos))

hostname = "sw-01"
print(len(hostname))

config = """interface Gi0/0/1
description Uplink
no shutdown"""

print(config)

print("birinci\nikinci")
print("sütun1\tsütun2")
print("tırnak: \"merhaba\"")   # \"
print('tek tırnak: \'a\'')     # \'
print("ters slash: \\")

#print("tırnak: "merhaba"")   # \" olmadan
#print('tek tırnak: 'a'')     # \' olmadan
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("\\\\")

print("Yükleme: %10\rTamamlandı!")
print("Yükleme: \r%10 Tamamlandı!")

print("C:\new\test")
print(r"C:\new\test")

satir = "Gi0/0/1  10.0.0.1  up"

print(satir.split())  # boşlukları hedef aldı

ip = "192.168.10.5"
print(ip.split("."))  # burada noktalar

mac = "AA:BB:CC:DD:EE:FF"
print(mac.split(":"))  # burada iki nokta üst üste

parcalar = ip.split(".")

print(parcalar[0])
print(parcalar[-1])

string = "10" + "20"
print(string)

string = int("10") + int("20")
print(string)

satir = "10.0.0.1  up  manual  1000Mbps"
print(satir.split(" ", 1))  # ilk boşlukta bölsün

octetler = ["192", "168", "10", "5"]

ip = ".".join(octetler)
print(ip)

config_satirlari = ["interface Gi0/0/1", "description Uplink", "no shutdown"]
config = "\n".join(config_satirlari)
print(config)

config_satirlari = ["interface Gi0/0/1", "description Uplink", "no shutdown"]

result = " ".join(x for x in config_satirlari)
print(result)

ham = "   interface Gi0/0/1   "

print(f"[{ham}]")

print(f"[{ham.strip()}]")
print(f"[{ham.lstrip()}]")
print(f"[{ham.rstrip()}]")

print(";;Gi0/0/1;;".strip(";"))

template = "hostname HOSTNAME\nip address IPADDRESS"

config = template.replace("HOSTNAME", "core-sw-01")
config = config.replace("IPADDRESS", "10.0.0.1")
print(config)

print("\n")

template = ("hostname HOSTNAME\nip address IPADDRESS \n"
            "----- \n hostname HOSTNAME\nip address IPADDRESS")

# Sadece 1 eşleşme ile sınırladım
config = template.replace("HOSTNAME", "core-sw-01", 1)
config = config.replace("IPADDRESS", "10.0.0.1", 1)
print(config)

satir = "interface Gi0/0/1"
print(satir.startswith("interface"))  # True
print(satir.startswith("Interface"))  # False

log = "Jul 12 08:15:01 %LINK-3-UPDOWN: Interface Gi0/0/1 changed state to up"
print(log.endswith("up"))

output = """Building configuration...
interface Gi0/0/1
 description Uplink
interface Gi0/0/2
 description Downlink
Current configuration : 1521 bytes"""

for satir in output.splitlines():  # satır satır bölmek için
    if satir.startswith("interface"):
        print("Bulunan:", satir.strip())

for satir in output.splitlines():
    if satir.endswith("bytes"):
        print("Bulunan:", satir.strip(": Current configuration"))

log = "Gi0/0/1 state changed to down"

print(log.find("down"))
print(log.find("ERROR"))  # -1 — yok
print(log.find("state"))

log = "Gi0/0/1 state changed to down"

if log.find("ERROR") != -1:
    print("Log'da hata var.")

# Daha temiz
if "ERROR" in log:
    print("Log'da hata var.")

#if log.index("ERROR") != -1:
#    print("Log'da hata var.")
# ValueError: substring not found
# index()'de aynı işlev ama hata döndürür

cevap = "UP"

print(cevap.lower())
print("merhaba".upper())

durum = input("Interface durumu (up/down): ")

if durum.lower() == "up":
    print("Interface active")
else:
    print("Interface deactive")

# if durum.casefold() == "up":
# uluslararası karşılaştırmalarda - almanca ß gibi - normalize etmelerde

hostname = "core-sw-01"
vlan = 100

print(f"hostname {hostname}")
print(f"interface Vlan{vlan}")
print(f"{hostname} üzerinde VLAN {vlan} yapılandırıldı")

a = 5
b = 3

print(f"{a} + {b} = {a + b}")
print(f"Karesi: {a ** 2}")

durum = "up"
print(f"{'ACTIVE' if durum == 'up' else 'DEACTIVE'}")

oran = 2.45678

print(f"{oran:.2f}")
print(f"{oran:.0f}")

buyuk_sayi = 1234567
print(f"{buyuk_sayi:,}")  # , - ayraç

ip = "10.0.0.1"
hostname = "core-sw-01"

print(f"{'IP':<15}{'HOSTNAME':<15}")
print("-" * 30)
print(f"{ip:<15}{hostname:<15}") # :<15 sol, :>15 sağ, :^15 orta

print(f"VLAN {{100}} config'i") # VLAN {100} - {} için

mac = "aa:bb:cc:dd:ee:ff"
mac_upper = mac.upper()
print(mac_upper.replace(":", "-"))

mac = "AA:BB:CC:DD:EE:FF"
mac_oui = ":".join(mac.split(":")[:3])

print("Vendor: ", mac_oui)
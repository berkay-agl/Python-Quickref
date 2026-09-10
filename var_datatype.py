from os.path import split

hostname = "core-sw-01"

x = 10
print(x)

x = 20
print(x)

vlan_id = 20
ip_address = "10.0.0.1"
is_reachable = True

#2vlan = 20
# SyntaxError: invalid decimal literal
#vlan-id = 20
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?

vlan_id = 100
port = 22
mtu = 1500

print(vlan_id)
print(port + mtu)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 8)     # subnetting'de

bandwidth = 10_000_000_000
print(bandwidth)              # 10000000000

latency_ms = 12.5
packet_loss = 0.02

print(latency_ms)
print(packet_loss)

latency_ms = 12,5
print(latency_ms) # (12, 5) anladı mesela: , ile

print(0.1 + 0.2) # 0.30000000000000004
print(0.1 + 0.2 == 0.3)
print(0.1 + 0.2 == 0.30000000000000004)

fark = abs(0.1 + 0.2 - 0.3)     # abs = mutlak değer
print(fark < 0.000001)

oran = 0.1 + 0.2
print(f"{oran:.2f}")

a = "merhaba"
b = 'merhaba'
c = """merhaba
dünya"""

print(a)
print(b)
print(c)

mesaj = 'Interface "Gi0/0/1" kapalı'
print(mesaj)

print("birinci satır\nikinci satır")
print("sekme\tyapar")
print("tırnak: \"merhaba\"")             # \"
print('gerçekten \"hayır olmaz\" dedi.')

hostname = "sw-01"
domain = ".sirket.local"

fqdn = hostname + domain
print(fqdn)

print("-" * 30)

log = "  Interface Gi0/0/1 state changed to DOWN  "

print(log.strip())
print(log.upper())
print(log.lower())
print(log.replace("DOWN", "UP"))
print("DOWN" in log)
print(len(log))

satir = "Gi0/0/1  10.0.0.1  up"
print(satir)

parcalar = satir.split()
print(parcalar)
print(len(parcalar))
print(parcalar[0])
print(f"interface: {parcalar[0]}, ip: {parcalar[1]}, state: {parcalar[2]}")

ip = "10.0.0.1"

print(ip[0])
print(ip[1])
print(ip[-1])    # -1 end

mac = "AA:BB:CC:DD:EE:FF"

print(mac[0:5])     # C'ye kadar
print(mac[:5])      # baştan C'ye kadar
print(mac[-5:])     # sondan D kısmından

is_up = True
is_connected = False

print(5 > 3)
print(5 == 5)
print(5 != 5)
print(10 <= 9)

print(bool("False"))
print(bool("0"))
print(bool(""))
print(bool(0))

print(type(42))
print(type(3.14))
print(type("10.0.0.1"))
print(type(True)) # bool -> int'in alt türü aslında

vlan_str = "100"
vlan_int = int(vlan_str)
print(vlan_int + 50)

oran_str = "2.5"
oran_float = float(oran_str)
print(oran_float * 2)

port = 22
mesaj = str(port)
print(mesaj)
print(type(mesaj))
mesaj = "Port: " + str(port)
print(mesaj)
print(type(mesaj))

print(int("42"))
#print(int("merhaba"))
# ValueError: invalid literal for int() with base 10: 'merhaba'

raw_deger = "N/A"

try:
    vlan = int(raw_deger)
except ValueError:
    vlan = -1
    print(f"'{raw_deger}' bir sayı değil, -1 atandı.")

print(vlan)

print(int(9.9))

#print(int("42.0"))
# ValueError: invalid literal for int() with base 10: '42.0'
print(int(float("42.0")))

print(int("  42  "))
#print(int(""))
# ValueError: invalid literal for int() with base 10: ''

cevap = "false"

if bool(cevap):            # True: istenen değil
    print("Açık!")

if cevap.lower() == "false":   # bu istenen
    print("Kapalı")
else:
    print("Açık")

isim = input("Switch ismi: ")
vlan_girdi = input("VLAN ID (sayı girin): ")

try:
    vlan_id = int(vlan_girdi)
except ValueError:
    print("VLAN ID bir sayı olmalıydı!")
    vlan_id = None

if vlan_id is not None:
    print(f"{isim} üzerinde VLAN {vlan_id} yapılandırılacak.")
    print(f"View: interface Vlan{vlan_id}")
else:
    print("İşlem iptal edildi.")

ip = "192.168.10.5".split('.')
ip_sum = int(ip[0]) + int(ip[1]) + int(ip[2]) + int(ip[3])
print(ip_sum)

latency = input("Latency değeri gir: ")

try:
    latency = float(latency)
except ValueError:
    latency = None
    print("Yanlış karakter.")

if latency is not None:
    if latency > 10:
        print("Sakiinn")
    else:
        print("İyisinn")

string_deger = " Gi0/0/1|up|1000Mbps ".strip(" ").split("|")
interface = string_deger[0].upper()
print(interface)

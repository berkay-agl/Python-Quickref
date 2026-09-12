print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

print(10 / 4)
print(10 // 4)
print(9 / 3)  # float 3.0
print(9 // 3)  # float değil

toplam_ip = 256  # /24
subnet_basina = 4  # /30 - 4 adet IP adresi

subnet_sayisi = toplam_ip // subnet_basina
print(f"Çıkarılabilecek /30 sayısı: {subnet_sayisi}")

print(10 % 3)
print(12 % 4)
print(7 % 2)

vlan = 20

if vlan % 2 == 0:
    print(f"VLAN {vlan} çift sayı")
else:
    print(f"VLAN {vlan} tek sayı")

dns_sunuculari = ["10.0.0.53", "10.0.0.54"]

for i in range(5):
    secilen = dns_sunuculari[i % 2]  # 0-1-0-1 | 0 % 2 = [0] | 1 % 2 = [1]
    print(f"İstemci {i}: DNS {secilen}")

print(2 ** 8)  # 256
print(2 ** 10)  # 1024
print(2 ** 16)  # 65536

prefix = 24
ip_sayisi = 2 ** (32 - prefix)  #  2^(32-24) = 2^8 = 256
print(f"/{prefix} bir blokta {ip_sayisi} IP vardır")

kullanilabilir = ip_sayisi - 2  # Ağ ve Broadcast adresleri olmadan işte
print(f"Kullanılabilir host: {kullanilabilir}")

print(5 + 2.0)
print(10 / 2)

print(5 == 5)
print(5 != 5)
print(5 > 3)
print(5 < 3)
print(5 >= 5)
print(5 <= 4)

mtu = 1500

if mtu >= 1500:
    print("MTU standart boyutta veya jumbo")

#if mtu = 1500:
    # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

durum = "up"

print(durum == "up")
print(durum == "UP")

durum = "UP"

if durum == "up":
    print("Interface çalışıyor")
else:
    print("Hata")

durum = "UP"

if durum.lower() == "up":
    print("Interface çalışıyor")
else:
    print("Hata")

latency = 45.5  # ms
kritik_esik = 50.0

if latency >= kritik_esik:
    print(f"ALARM: Latency {latency}ms eşiğini aştı")
else:
    print(f"Latency normal: {latency}ms")

print(True and True)  # and - true
print(True and False)
print(False and True)
print(False and False)

fiziksel_durum = "up"
line_protocol = "up"

if fiziksel_durum == "up" and line_protocol == "up":
    print("Interface tamamen çalışıyor")
else:
    print("Interface'de sorun var")

print(True or True)  # or - tek true
print(True or False)
print(False or True)
print(False or False)

isis_komsu = True
ospf_komsu = False

if isis_komsu or ospf_komsu:
    print("En az bir IGP komşuluğu var")
else:
    print("Hiç komşuluk yok")

print(not True)      # False
print(not False)     # True

bakim_modu = False

if not bakim_modu:
    print("Cihaz bakımda değil")

cihaz_erisilebilir = True
yeterli_yetki = True
bakimda = False

if cihaz_erisilebilir and yeterli_yetki and not bakimda:
    print("Config gönderilebilir")
else:
    print("Config gönderilemez")

sayac = 0
print(sayac)

sayac = 10

sayac += 5
print(sayac)  # 15

sayac -= 3
print(sayac)  # 12

sayac *= 2
print(sayac)  # 24

sayac /= 4
print(sayac)  # 6.0

sayac //= 2
print(sayac)  # 3.0

sayac **= 2
print(sayac)  # 9.0

sayac %= 2
print(sayac)  # 1.0

basarisiz_ping = 0

for deneme in [True, False, True, False, True]:
    if not deneme:
        basarisiz_ping += 1

print(f"Toplam başarısız deneme: {basarisiz_ping}")    # 2 - false

sayac = 5
#sayac++
# SyntaxError: invalid syntax
sayac += 1

"""
Öncelikli kurallar matematik dersindeki gibi

1. ()        parantez — en yüksek öncelik
2. **        üs alma
3. *, /, //, %   çarpma ve bölmeler, soldan sağa
4. +, -      toplama ve çıkarma
"""

print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20 — parantez
print(2 ** 3 * 2)

prefix = 26
host_sayisi = (2 ** (32 - prefix)) - 2  # 2^(32-prefix) - 2
print(f"/{prefix} için kullanılabilir host: {host_sayisi}")

log = "%LINK-3-UPDOWN: Interface Gi0/0/1, changed state to up"

print("UPDOWN" in log)         # "updown" log içinde var mı - true
print("ERROR" not in log)      # "error" log içinde yok mu - true

packet = 1000  # byte
bit = 8  # bit

print(packet * bit)  # 8000 bit

packet = 8000
bit = 8

print(packet * bit)  # 64.000 bit

toplam_gun_dk = 1440
cihaz_dk = 1437

yuzde = float((cihaz_dk / toplam_gun_dk) * 100)

print(f"Yüzdesi: {yuzde:.2f}%")

vlan_id = 110

if vlan_id % 5 == 0 and vlan_id > 100:
    print("Bu VLAN hem büyük hem 5'in katı")
else:
    print("Hata.")

prefix = 27
ip_sayisi = (2 ** (32 - prefix))
host_sayisi = ip_sayisi - 2
print(f"ip sayısı: {ip_sayisi}, host sayısı: {host_sayisi}")
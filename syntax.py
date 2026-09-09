import time

# Okunmaz bu satır

vlan_id = 10  # Bu da yorum: kod çalışır sonrası görünmez

print(vlan_id)

# Örnek şöyle kullanım olabilir: Switch'lerin yönetim IP'leri Burada Değiştirme
switch_1 = "10.0.0.1"
switch_2 = "10.0.0.2"

print(switch_1)
print(switch_2)

# Kötü yorum: kod zaten bunu söylüyor:
sayi = 1
sayi = sayi + 1  # sayıyı 1 arttırır: zaten bilinen bi' şey

# İyi yorum: kodun söylemediğini söylüyor:
timeout = 30  # X admin önerdiği için 10 yerine 30sn kullandım

"""
Bu dosya: switch listesini ekrana basar.
Yazan: Berkay
Tarih: 2026
"""

mesaj = """Bu uzun bir 
metin oldu, üç tırnak
ile yazılabilir."""

print(mesaj)

# TODO: Mesela X sunucusu çalışmazsa yedek giriş yöntemi ekle
# FIXME: Mesela bu da: hesaplama bazen yanlış sonuç veriyor, araştır
timeout_2 = 30

interface_state = "down"

if interface_state == "down":
    print("Interface kapalı.")
    print("Lütfen kontrol edin.")
print("Program bitti.")

interface_state = "up"

if interface_state == "down":
    print("Interface kapalı.")
    print("Lütfen kontrol edin.")
print("Program bitti.")

if True:
    print("4 boşluk.")
    if True:
        print("8 boşluk (4 + 4)")

if True:
  print("Tab diyelim buraya kadar girinti sağladı: yanlış")

# Şimdi indentation hatalarına bakalım

vlan_id = 10

if vlan_id > 5:
    ...
#print("VLAN 5'den büyük.")
#  ... sil ve # sil alt alta dene --> IndentationError: expected an indented block after 'if' statement on line 63

vlan_id = 10

if vlan_id > 5:
    print("4 girinti")
        #print("8 girinti")
        # IndentationError: unexpected indent

  #print("Gereksiz girinti: 2 boşluk.")
# IndentationError: unindent does not match any outer indentation level

interfaces = [
    "Gi0/0/0",
    "Gi0/0/1",
    "Gi0/0/2",
]

print(interfaces)

toplam = 1000 + 1000 + \
    3000 + 2000 + \
         - 1000
print(toplam)

print("Merhaba!")
print(42)
print("IP:", "10.0.0.1")

vlan_id = 10
#print("VLAN numarası: " + vlan_id)
# TypeError: can only concatenate str (not "int") to str

vlan_id = 10

# int'i str'ye
print("VLAN numarası: " + str(vlan_id))
# virgülle
print("VLAN numarası:", vlan_id)
# f-string
print(f"VLAN numarası: {vlan_id}")

hostname = "core-sw-01"
ip = "10.0.0.1"
state = "up"

print(f"Cihaz: {hostname} ({ip}) durumu: {state}")

packet_loss_percent = 5.4567213
print(f"Packet loss oranı: {packet_loss_percent:.2f}%")

print("10.0.0.1", "Gi0/0/1", "up")
print("10.0.0.1", "Gi0/0/1", "up", sep=" * ")

print("Yükleniyor", end="...")
print(" tamamlandı")

isim = input("ismini gir: ")
print(f"Merhaba {isim}, hoş geldin..")

for i in range(1, 4):
    print(f"Adım {i} ", end="", flush=False)
    time.sleep(2)
print("\nBitti.")

for i in range(1, 4):
    print(f"Adım {i} ", end="", flush=True)
    time.sleep(2)
print("\nBitti.")
interfaces = ["Gi0/0/1", "Gi0/0/2", "Gi0/1/1"]
vlan_ids = [10, 20, 30, 99]
karisik = ["core-sw-01", 10, True, 3.14]
bos_liste = []

interfaces = ["Gi0/0/1", "Gi0/0/2", "Gi0/1/1"]

print(interfaces[0])
print(interfaces[1])
print(interfaces[-1])
print(interfaces[-2])

#print(interfaces[10]
# IndexError: list index out of range

vlans = [10, 20, 30, 40, 50, 60]

print(vlans[1:4])
print(vlans[:3])
print(vlans[3:])
print(vlans[:])
print(vlans[::2])
print(vlans[::-1])

switches = ["core-sw-01"]
switches.append("dist-sw-02")
print(switches)

switches = ["core-sw-01"]
yeni_switchler = ["dist-sw-02", "access-sw-03"]

switches.extend(yeni_switchler)
print(switches)

liste1 = [1, 2, 3]
liste2 = [1, 2, 3]

liste1.append([4, 5])  # tek eleman olarak
liste2.extend([4, 5])  # her biri ayrı olarak
print(liste1)
print(liste2)

switches = ["core-sw-01", "access-sw-03"]
switches.insert(1, "dist-sw-02")  # index 1
print(switches)

print("\n")

switches = ["core-sw-01", "access-sw-03"]
switches.insert(len(switches), "dist-sw-04")  # append(x) ile aynı
print(switches)

frameworks = ["Django", "Flask", "Pyramid", "Flask"]
frameworks.remove("Flask")
print(frameworks)

switches = ["core-sw-01", "dist-sw-02", "access-sw-03"]
silinen = switches.pop(1)
print(silinen)
print(switches)

son = switches.pop()  # sonuncu index
print(son)

liste = [10, 20, 30, 40, 50]

del liste[0]
print(liste)

del liste[1:3]
print(liste)

del liste

#print(liste)
# NameError: name 'liste' is not defined. Did you mean: 'liste1'?

liste = [1, 2, 3]
liste.clear()
print(liste)

cpu_degerleri = [45, 90, 12, 78]
cpu_degerleri.sort()  # Sıralanmış
print(cpu_degerleri)

sonuc = cpu_degerleri.sort()
print(sonuc)  # None - geri dönüş değeri vermiyor

cpu_degerleri = [45, 90, 12, 78]
sonuc = sorted(cpu_degerleri)
print(sonuc)           #
print(cpu_degerleri)  # orijinal DEĞİŞMEDİ

cpu_degerleri = [45, 90, 12, 78]
print(sorted(cpu_degerleri, reverse=True))

cihazlar = [("core-sw-01", 90), ("dist-sw-02", 45), ("access-sw-03", 78)]
cpu_gore_sirali = sorted(cihazlar, key=lambda cihaz: cihaz[1])
print(cpu_gore_sirali)
# key=lambda cihaz: cihaz[1]:
# her elemanın sıralama kriteri olarak onun 1. index'ini kullanmak için yani tuple'da 90, 45, 78

switches = ["core-sw-01", "dist-sw-02", "access-sw-03"]
print(switches.index("dist-sw-02"))  # ilk pozisyon

#print(switches.index("dist-sw-04"))
# ValueError: 'dist-sw-04' is not in list

# Bu yüzden kontrol edilir yoksa hata basmaz
if "dist-sw-04" in switches:
    print(switches.index("dist-sw-04"))

if "dist-sw-01" in switches:
    print(switches.index("dist-sw-01"))

statuslar = ["up", "down", "up", "up", "down"]
print(statuslar.count("up"))  # listede kaç tane geçmiş

liste1 = [1, 2, 3]
liste2 = liste1  # aynı listeye işaret

liste2.append(4)
print(liste1)   # liste1 etkilendi

# Bu yüzden
liste3 = [1, 2, 3]

liste4 = liste3.copy()
liste4.append(4)
print(liste4)
print(liste3)

liste5 = liste3[:]  # bu da slice ile

koordinat = (10.5, 20.3)
switch_bilgisi = ("core-sw-01", "10.0.0.1", "up")

#koordinat[0] = 99
# TypeError: 'tuple' object does not support item assignment

liste = [1, 2, 3]
tp = tuple(liste)

tp2 = ("a", "b", "c")
liste2 = list(tp2)

yanlis = (5)
dogru = (5,)  # , lazım

print(type(yanlis))  # int
print(type(dogru))  # tuple

switch_bilgisi = ("core-sw-01", "10.0.0.1", "up")
hostname, ip, durum = switch_bilgisi

print(hostname)
print(ip)
print(durum)

degerler = (1, 2, 3, 4, 5)
ilk, *orta, son = degerler  # * ile esneklik ilk ve son al ama ortayı listele

print(ilk)
print(orta)
print(son)

a = 5
b = 10
a, b = b, a  # tuple oluşturulur sonra unpack edilir
print(a, b)

switchler = [("core-sw-01", "up"), ("dist-sw-02", "down")]

for hostname, durum in switchler:  # enumurate() gibi o da unpacking
    print(f"{hostname}: {durum}")

vlan_ids = {10, 20, 30, 20, 10}
print(vlan_ids)  # SET tekrarsız

ip_listesi = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.3", "10.0.0.2"]
tekil_ipler = list(set(ip_listesi))  # listedeki tekrarları çıkarmak
print(tekil_ipler)

bos_set = set()
yanlis = {}  # boş dict

vlanlar = {10, 20, 30}

vlanlar.add(40)
print(vlanlar)

vlanlar.add(20)
print(vlanlar)

vlanlar.remove(10)
print(vlanlar)

#vlanlar.remove(999)
#print(vlanlar)
# KeyError: 999

vlanlar.discard(999)  # Hata döndürmez
print(vlanlar)

switch_a_vlanlari = {10, 20, 30, 40}
switch_b_vlanlari = {30, 40, 50, 60}

# Kesişim
print(switch_a_vlanlari & switch_b_vlanlari)
print(switch_a_vlanlari.intersection(switch_b_vlanlari))

# Birleşim
print(switch_a_vlanlari | switch_b_vlanlari)
print(switch_a_vlanlari.union(switch_b_vlanlari))

# Fark — sadece A'da olup B'de olmayan elemanlar
print(switch_a_vlanlari - switch_b_vlanlari)
print(switch_a_vlanlari.difference(switch_b_vlanlari))

# Simetrik Fark — sadece birinde olanlar
print(switch_a_vlanlari ^ switch_b_vlanlari)

kucuk_set = {10, 20}
buyuk_set = {10, 20, 30, 40}

print(kucuk_set.issubset(buyuk_set))  # kucuk_set <= buyuk_set
print(buyuk_set.issuperset(kucuk_set))  # buyuk_set >= kucuk_set

gecerli = {1, "a", (10, 20)}  # immutable
#gecersiz = {1, [10, 20]}
# TypeError: unhashable type: 'list' çünkü mutable

switch = {
    "hostname": "core-sw-01",
    "ip": "10.0.0.1",
    "durum": "up",
    "port_sayisi": 48
}

print(switch["hostname"])
print(switch["port_sayisi"])

switch["seri_no"] = "FDO12345"
switch["durum"] = "down"

print(switch)

switch = {"hostname": "core-sw-01", "ip": "10.0.0.1", "durum": "up"}

del switch["durum"]
print(switch)

silinen_deger = switch.pop("ip")  # list.pop gibi
print(silinen_deger)

switch.clear()
print(switch)

switch = {"hostname": "core-sw-01", "ip": "10.0.0.1", "durum": "up"}

print(switch.keys())
print(switch.values())
print(switch.items())

# items() ile hem key hem value
for key, value in switch.items():
    print(f"{key}: {value}")

#print(switch["hostnam"])
# KeyError: 'hostnam'

print(switch.get("hostnam"))  # None
print(switch.get("hostnam", "N/A"))  # ikinci argüman: varsayılan değer

switch = {"hostname": "core-sw-01", "ip": "10.0.0.1"}
yeni_bilgiler = {"durum": "up", "ip": "10.0.0.2"}

switch.update(yeni_bilgiler)  # ip bilgisini üstüne yazıyor
print(switch)

# SET mantığı - hash table
gecerli = {("10.0.0.1", 22): "SSH bağlantısı"}
#gecersiz = {["10.0.0.1"]: "veri"}
# TypeError: unhashable type: 'list'

# Nested
switchler = [
    {"hostname": "core-sw-01", "ip": "10.0.0.1", "vlanlar": [10, 20, 30]},
    {"hostname": "dist-sw-02", "ip": "10.0.0.2", "vlanlar": [10, 40]},
]

for switch in switchler:
    print(f"{switch['hostname']} ({switch['ip']}) — VLAN'lar: {switch['vlanlar']}")

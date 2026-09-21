from time import sleep

def selamlama():
    print("Network of Networks.")

selamlama()

#ping_cihaz()
# NameError: name 'ping_cihaz' is not defined
# Bu yüzden önce def sonra çağırma

def ping_cihaz():
    print("Ping gönderiliyor...")

ping_cihaz()

def configure_interface(interface_name, vlan_id):  # parametre
    print(f"{interface_name} portuna VLAN {vlan_id} atandı.")

configure_interface("Gi0/1", 10)  # argüman

# keywordlü
def configure_interface(interface_name="Gi0/1", vlan_id=10):
    print(f"{interface_name} portuna VLAN {vlan_id} atandı.")

configure_interface()

def ssh_baglan(ip_adresi, port=22, timeout=5):
    print(f"{ip_adresi}:{port} adresine bağlanılıyor (Timeout: {timeout}s)...")

ssh_baglan("10.0.0.1")  # diğerleri varsayılan

ssh_baglan("10.0.0.2", port=2222, timeout=10)  # diğerleri ezildi

#def hatali_fonksiyon(port=22, ip_adresi):
#    pass
# SyntaxError: parameter without a default follows parameter with a default

def dogru_fonksiyon(ip_adresi, port=22):  # Varsayılan değeri olmayan başta
    pass

# fonksiyone kaç tane argüman gelecek bilmiyorsam *args
def vlan_ekle(switch_name, *vlanlar):
    print(f"Hedef Switch: {switch_name}")
    print(f"Gelen VLAN paketi tipi: {type(vlanlar)}")
    for vlan in vlanlar:
        print(f" -> VLAN {vlan} yapılandırılıyor...")
    print(repr(vlanlar))  # tuple

vlan_ekle("core-sw-01", 10, 20, 30, 40)

# **kwargs ile fonksiyone gönderilen fazladan keyword argümanlarını bir dictionary içinde
def cihaz_kaydi(hostname, **detaylar):
    print(f"Cihaz: {hostname}")
    print(f"Detay sözlüğü: {detaylar}")
    for ozellik, deger in detaylar.items():
        print(f"  - {ozellik}: {deger}")
    print(repr(detaylar))

cihaz_kaydi("dist-sw-01", ip="10.0.1.1", model="Catalyst 9300", vendor="Cisco")

# def func(positional, *args, default_param=val, **kwargs):

def parse_ip(tam_ip):
    ip_adresi = tam_ip.split("/")[0]
    return ip_adresi

temiz_ip = parse_ip("192.168.1.1/24")
print(f"İşlenecek IP: {temiz_ip}")

def parse_ip(tam_ip):
    ip_adresi = tam_ip.split("/")[0]

temiz_ip = parse_ip("192.168.1.1/24")
print(f"İşlenecek IP: {temiz_ip}")  # None olur çünkü return yok

def switch_ozet(hostname, port_sayisi, aktif_port):
    bos_port = port_sayisi - aktif_port
    kullanim_orani = (aktif_port / port_sayisi) * 100
    return bos_port, kullanim_orani

# Tuple unpacking mantığı
kalan, oran = switch_ozet("access-sw-01", 48, 36)
print(f"Boş Port: {kalan}, Doluluk: %{oran:.1f}")

# Docstring
def ip_ping(ip, count=3):
    """
    Belirtilen IP adresine ICMP ping paketi gönderir.

    Parametreler:
        ip (str): Hedef IP adresi (örn. '192.168.1.1')
        count (int): Gönderilecek paket sayısı (varsayılan: 3)

    Döndürür:
        bool: Cihaz ayaktaysa True, ulaşılamıyorsa False
    """
    return True

# Docstring'e erişim
print(ip_ping.__doc__)

global_dns = "8.8.8.8"  # Global

def ag_kurulum():
    local_gateway = "192.168.1.254"  # Local
    print(f"İçeriden okuma - DNS: {global_dns}, GW: {local_gateway}")

ag_kurulum()
print(global_dns)
#print(local_gateway)
# NameError: name 'local_gateway' is not defined

hata_sayisi = 0

def log_hatasi():
    global hata_sayisi  # Global hata_sayisi'nı kullanacağımı belirttim
    hata_sayisi += 1
    # Global silseydim: UnboundLocalError: cannot access local variable 'hata_sayisi' where it is not associated with a value

log_hatasi()
log_hatasi()
print(f"Toplam Hata: {hata_sayisi}")

# Klasik
def topla(a, b):
    return a + b

print(topla(3, 4))

# Lambda
topla_lambda = lambda a, b: a + b
print(topla_lambda(5, 10))

cihazlar = [
    {"host": "core-sw-01", "cpu": 88},
    {"host": "dist-sw-01", "cpu": 34},
    {"host": "edge-rt-01", "cpu": 95}
]

sirali = sorted(cihazlar, key=lambda c: c["cpu"])
print(sirali)

# Yanlışı port_listesi=[]
def port_ekle(port, port_listesi=[]):
    port_listesi.append(port)
    return port_listesi

print(port_ekle("Gi0/1"))  # ['Gi0/1']
print(port_ekle("Gi0/2"))  # ['Gi0/1', 'Gi0/2']

# Pythonic
def port_ekle_dogru(port, port_listesi=None):
    if port_listesi is None:
        port_listesi = []
    port_listesi.append(port)
    return port_listesi

print(port_ekle_dogru("Gi0/1"))  # ['Gi0/1']
print(port_ekle_dogru("Gi0/2"))  # ['Gi0/2']
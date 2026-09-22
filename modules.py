import math
from math import sqrt, pi
import datetime as dt
from math import sqrt as sq
import os
import sys
import random
from datetime import datetime, timedelta

sonuc = math.sqrt(25)  # karekök fonksiyonu
print(sonuc)
print(math.pi)

print(sqrt(64))
print(pi)

now = dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

print(sq(25))  # tek bir fonksiyon

# Basitçe modül x.py olsun bu
VLAN_POOL = [10, 20, 30, 40, 50]

def subnet_mask_bul(cidr):
    maskeler = {24: "255.255.255.0", 16: "255.255.0.0", 8: "255.0.0.0"}
    return maskeler.get(cidr, "Bilinmeyen Mask")

def host_ayristir(ip_str):
    return ip_str.split("/")[0]

# sonra y.py dosyasında

#import x as net

#ip = "192.168.1.50/24"

#temiz_ip = net.host_ayristir(ip)
#mask = net.subnet_mask_bul(24)

#print(f"Cihaz IP: {temiz_ip}, Mask: {mask}")
#print(f"Kullanılabilir VLAN'lar: {net.VLAN_POOL}")

def ping(ip):
    return f"{ip} erişilebilir."

# Başka dosya import x.py'yi yaparsa burası çalışmaz
if __name__ == "__main__":
    print("Modül doğrudan test ediliyor...")
    print(ping("10.0.0.1"))

mevcut_dizin = os.getcwd()  # Current Working Directory
print(f"Dizin: {mevcut_dizin}")

kullanici = os.getenv("USER") or os.getenv("USERNAME")  # Environment Variable okuma
print(f"Aktif Kullanıcı: {kullanici}")

if not os.path.exists("network"):
    os.mkdir("network")
    print("Yedek klasörü oluşturuldu.")

tam_yol = os.path.join("network", "core_sw_config.txt")
print(tam_yol)

print(f"Python Sürümü: {sys.version.split()[0]}")

# Script'i sonlandırma
# sys.exit(1)  # 0: başarıyla bitti, 1: hata ile bitti

# python x.py 10.0.0.1 Gi0/1
print(f"Script adı: {sys.argv[0]}")
if len(sys.argv) > 1:
    hedef_ip = sys.argv[1]
    print(f"Hedeflenen IP: {hedef_ip}")

print(math.ceil(4.2))  # Yukarı yuvarlar
print(math.floor(4.9))  # Aşağı yuvarlar
print(math.pow(2, 8))  # 2 üzeri 8
print(math.log2(256))  # 2 tabanında logaritma
print(math.gcd(48, 36))  # EBOB

rastgele_vlan = random.randint(10, 99)
print(f"Oluşturulan VLAN: {rastgele_vlan}")

cihazlar = ["core-sw-01", "dist-sw-01", "edge-rt-01", "access-sw-02"]
secilen = random.choice(cihazlar)
print(f"Yedeklenecek cihaz: {secilen}")

orneklem = random.sample(cihazlar, 2)  # N adetS
print(f"Seçilen 2 cihaz: {orneklem}")

random.shuffle(cihazlar)  # karıştırma
print(f"Karıştırılmış liste: {cihazlar}")

simdi = datetime.now()
print(f"Şu an: {simdi}")

# %Y: yıl, %m: ay, %d: gün, %H: saat, %M: dakika, %S: saniye
formatli_tarih = simdi.strftime("%Y-%m-%d_%H-%M-%S")
backup_dosya_adi = f"config_backup_{formatli_tarih}.txt"
print(f"Dosya adı: {backup_dosya_adi}")

tarih_metni = "2026-09-22 14:30:00"
tarih_objesi = datetime.strptime(tarih_metni, "%Y-%m-%d %H:%M:%S")

yedi_gun_once = simdi - timedelta(days=7)
print(f"1 hafta önceki tarih: {yedi_gun_once.strftime('%d.%m.%Y')}")

on_bes_gun_sonra = simdi + timedelta(days=15)
print(f"15 gün sonraki tarih: {on_bes_gun_sonra.strftime('%d.%m.%Y')}")


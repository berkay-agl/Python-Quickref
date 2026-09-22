import csv
import json

# dosya_nesnesi = open("dosya_yolu", "mod", encoding="utf-8")

f = open("sw_config.txt", "r", encoding="utf-8")
icerik = f.read()
print(icerik)
f.close()

f = open("sw_config.txt", "r", encoding="utf-8")
ilk_satir = f.readline()
ikinci_satir = f.readline()
print("\n")
print(ilk_satir)
print(ikinci_satir)
f.close()

f = open("sw_config.txt", "r", encoding="utf-8")
satirlar = f.readlines()  # her satır ayrı eleman - list
print(satirlar)
f.close()

"""
sw_config.txt

hostname core-sw-01
vlan 10
 name YONETIM
interface Gi0/1

    DENY
"""

# Daha memory dostu büyük dosyalarda
f = open("sw_config.txt", "r", encoding="utf-8")

for satir in f:
    if "DENY" in satir:
        print(satir.strip())
f.close()

f = open("sw_config.txt", "w", encoding="utf-8")
f.write("core-sw-01\n")  # oto alt satıra geçmiyo
f.write("dist-sw-01\n")
f.close()

# Manuel close() gerek yok
with open("sw_config.txt", "r", encoding="utf-8") as f:
    for satir in f:
        print(satir.strip())

print(f.closed)

f = open("sw_config.txt", "r", encoding="utf-8")

for satir in f:
    print(satir.strip())

#f.close()
print(f.closed)  # bu false oldu

# 'a' modu ekleme yapıyor
with open("sw_config.txt", "a", encoding="utf-8") as log_file:
    log_file.write("2026-09-22 10:00:00 - Switch.\n")

# List olarak
with open("devices.csv", "r", encoding="utf-8") as f:
    okuyucu = csv.reader(f)
    basliklar = next(okuyucu)  # İlk satırı ayrı almak
    print(f"Sütunlar: {basliklar}")

    for satir in okuyucu:
        hostname = satir[0]
        ip = satir[1]
        print(f"Cihaz: {hostname} -> IP: {ip}")

# Dict olarak
with open("devices.csv", "r", encoding="utf-8") as f:
    okuyucu = csv.DictReader(f)
    for row in okuyucu:
        print(f"Hostname: {row['hostname']}, Üretici: {row['vendor']}")
        print(repr(row))

veriler = [
    ["hostname", "ip", "status"],
    ["access-sw-01", "10.0.2.1", "up"],
    ["access-sw-02", "10.0.2.2", "down"]
]

# newline="" Windows'ta fazladan boş satır oluşmasını engellemek için
with open("cikis.csv", "w", newline="", encoding="utf-8") as f:
    yazici = csv.writer(f)
    yazici.writerows(veriler)

cihaz_verisi = {
    "hostname": "core-sw-01",
    "mgmt_ip": "10.0.0.1",
    "vlans": [10, 20, 30],
    "active": True
}

# dump - dosyaya json
with open("device_data.json", "w", encoding="utf-8") as f:
    json.dump(cihaz_verisi, f, indent=4)  # girintili

# load - dosyadan JSON okuma
with open("device_data.json", "r", encoding="utf-8") as f:
    yuklenen_veri = json.load(f)
    print(yuklenen_veri["mgmt_ip"])
    print(yuklenen_veri["vlans"][0])

raw_api_response = '{"status": "success", "interfaces": ["Gi0/1", "Gi0/2"]}'

# loads - string -> python dict
parsed_data = json.loads(raw_api_response)
print(parsed_data["interfaces"])

# dumps - python dict -> string
api_payload = {"command": "show version", "format": "json"}
json_string_payload = json.dumps(api_payload)
print(type(json_string_payload))
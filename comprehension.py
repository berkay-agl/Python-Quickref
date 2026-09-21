raw_ports = ["gi0/0/1", "gi0/0/2", "gi0/0/3"]
clean_ports = []

for port in raw_ports:
    clean_ports.append(port.upper())

print(clean_ports)

# işte list comprehension
raw_ports = ["gi0/0/1", "gi0/0/2", "gi0/0/3"]

clean_ports = [port.upper() for port in raw_ports]

print(clean_ports)

interfaces = [
    {"name": "Gi0/1", "status": "up"},
    {"name": "Gi0/2", "status": "down"},
    {"name": "Gi0/3", "status": "up"},
    {"name": "Gi0/4", "status": "admin_down"}
]

up_ports = [port["name"] for port in interfaces if port["status"] == "up"]
print(up_ports)

# klasikte şöyle olur
interfaces = [
    {"name": "Gi0/1", "status": "up"},
    {"name": "Gi0/2", "status": "down"},
    {"name": "Gi0/3", "status": "up"},
    {"name": "Gi0/4", "status": "admin_down"}
]

up_ports = []

for port in interfaces:
    if port["status"] == "up":
        up_ports.append(port["name"])

print(up_ports)

# if-else ise value dönüşümü için
cpu_values = [35, 88, 12, 95, 60]

cpu_status = ["CRITICAL" if cpu > 80 else "OK" for cpu in cpu_values]
print(cpu_status)

# ikisi bir arada
cpu_values = [45, -1, 92, 70, -5]

durumlar = [
    "HIGH" if cpu >= 80 else "NORMAL"
    for cpu in cpu_values
    if cpu >= 0  # geçerli ölçümler
]
print(durumlar)

# Bu da aynısı
cpu_values = [45, -1, 92, 70, -5]

cpu_status = ["HIGH" if cpu >= 80 else "NORMAL" for cpu in cpu_values if cpu >= 0]
print(cpu_status)

# Nested list
switch_vlans = [
    [10, 20, 30],
    [40, 50],
    [10, 60]
]

# Düz list hale getirmek için
tum_vlanlar = [vlan for sw in switch_vlans for vlan in sw]
print(tum_vlanlar)

# Açık hali
tum_vlanlar = []

for sw in switch_vlans:
    for vlan in sw:
        tum_vlanlar.append(vlan)

print(tum_vlanlar)

# fark için
tum_vlanlar = []

for sw in switch_vlans:
    tum_vlanlar.append(sw)

print(tum_vlanlar)

# dict comp ve zip()
hostnames = ["core-sw-01", "dist-sw-01", "access-sw-01"]
ip_addresses = ["10.0.0.1", "10.0.1.1", "10.0.2.1"]

# zip iki ayrı list'den dict üretmek için
cihaz_haritasi = {host: ip for host, ip in zip(hostnames, ip_addresses)}

print(cihaz_haritasi)

# dict dönüşüm
interfaces_mbps = {"Gi0/1": 1000, "Fa0/1": 100, "Te0/1": 10000}

interfaces_gbps = {port: speed / 1000 for port, speed in interfaces_mbps.items()}

print(interfaces_gbps)

switches = {
    "core-sw-01": "up",
    "access-sw-01": "down",
    "access-sw-02": "up",
    "dist-sw-01": "unreachable"
}

sorunlu_cihazlar = {sw: durum for sw, durum in switches.items() if durum != "up"}

print(sorunlu_cihazlar)

vlan_isimleri = {10: "Yonetim", 20: "Muhasebe", 30: "Misafir"}

# reverse
vlan_idleri = {isim: vlan_id for vlan_id, isim in vlan_isimleri.items()}

print(vlan_idleri)

# SET - dict gibi : yok
devices = [
    {"name": "sw-01", "vendor": "Cisco"},
    {"name": "sw-02", "vendor": "Arista"},
    {"name": "sw-03", "vendor": "Cisco"},
    {"name": "rt-01", "vendor": "Juniper"},
]

vendors = {d["vendor"] for d in devices}
print(vendors)  # tekrar da yok SET yapısı gereği
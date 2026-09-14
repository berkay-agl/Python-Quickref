interface_status = "down"

if interface_status == "down":
    print("UYARI: Interface kapalı!")

cpu_usage = 45

if cpu_usage > 80:
    print("Kritik! CPU yüksek.")
else:
    print("Normal seviyede.")

cpu_usage = 65

if cpu_usage > 90:
    print("Kritik seviye!")
elif cpu_usage > 70:
    print("Yüksek seviye, izlemeye devam et.")
elif cpu_usage > 50:
    print("Orta seviye.")
else:
    print("Normal.")

cpu_usage = 85
mem_usage = 90

if cpu_usage > 80 and mem_usage > 80:
    print("Cihaz aşırı yüklenmiş, hem CPU hem RAM kritik.")

interface_state = "err-disabled"

if interface_state == "down" or interface_state == "err-disabled":
    print("Interface'e müdahale gerekiyor.")

interface_status = "up"
duplex_mismatch = True

if interface_status == "up":
    print("Interface aktif.")
    if duplex_mismatch:  # True?
        print("Ama duplex mismatch var, kontrol et.")
    else:
        print("Duplex ayarları uyumlu.")
else:
    print("Interface kapalı, duplex kontrolüne gerek yok.")

# pyramid of doom
if interface_status == "up":
    if duplex_mismatch:
        print("Sorun var")

# and, or vs.
if interface_status == "up" and duplex_mismatch:
    print("Sorun var")

cpu_usage = 92

if cpu_usage > 90:
    status = "kritik"
else:
    status = "normal"

# Ternary Operator
status = "kritik" if cpu_usage > 90 else "normal"

print(status)

port_count = 22
print(f"Bu switch'te {port_count} port var" if port_count > 0 else "Port bilgisi yok")

cpu = 10
# çalışır ama tercih değil
sonuc = "kritik" if cpu > 90 else "yüksek" if cpu > 70 else "normal"
print(sonuc)

cpu = 95
if cpu > 90:
    print("kritik")
if cpu > 50:  # bu da ayrıca kontrolden geçer
    print("orta")

packet_loss = float(6.0)
print(f"{packet_loss}% : ", "Mükemmel" if packet_loss == 0.0 else "İyi" if 1 <= packet_loss <= 4 else "Kötü")
# ne kadar fazla ternary o kadar karışık

interface_status = "down"
cable_connected = True

if cable_connected:
    if interface_status == "down":
        print("Sorun var.")
else:
    print("Kablo yok.")

latency = 110
print(f"{latency}ms : ", "Yüksek gecikme" if latency > 100 else "Normal")
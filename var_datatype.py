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


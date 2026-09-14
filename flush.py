import time

print("Yükleniyor", end="")
for i in range(3):
    print(".", end="")
    time.sleep(2)
print("\nTamamlandı!\n")

print("Yükleniyor", end="")
for i in range(3):
    print(".", end="", flush=True)  # flush=True
    time.sleep(2)
print("\nTamamlandı!")

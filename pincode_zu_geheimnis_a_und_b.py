import random
pincode = int(input("Gib den Pincode ein: "))
geheimnis_a = random.randint(0, 999999)
geheimnis_b = pincode ^ geheimnis_a
print(f"Geheimnis A: {geheimnis_a}")
print(f"Geheimnis B: {geheimnis_b}")
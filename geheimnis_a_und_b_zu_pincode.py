geheimnis_a = int(input("Gib Geheimnis A ein: "))
geheimnis_b = int(input("Gib Geheimnis B ein: "))
pincode = geheimnis_a ^ geheimnis_b
print(f"Pincode: {pincode}")
from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15 Pro", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79345678901"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79456789012"))
catalog.append(Smartphone("Google", "Pixel 8", "+79567890123"))

print("Каталог смартфонов:")
for phone in catalog:
    print(phone)

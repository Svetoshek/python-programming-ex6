mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for item in mac:
    result.append(item.replace(":","."))
print(result)
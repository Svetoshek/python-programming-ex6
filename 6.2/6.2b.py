flag = False

while flag == False:
    ip = input("Enter ip: ")
    flag = True
    index = ip.split(".")
    if len(index) == 4:
        for octet in index:
            if not (octet.isdigit() and int(octet) >= 0 and int(octet) <= 255):
                flag = False
                break
    else:
        flag = False
    if not flag:
        print('Вы ввели неккоректный ip адрес')




f_ip = int(index[0])
if f_ip <= 223 and f_ip > 0:
    print("unicast")
elif f_ip <=239 and f_ip >= 224:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")

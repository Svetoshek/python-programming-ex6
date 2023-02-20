ip = input("Enter ip: ")
first_index = ip.split(".")[0]
if int(first_index) <= 223 and int(first_index) > 0:
    print("unicast")
elif int(first_index) <=239 and int(first_index) >= 224:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")

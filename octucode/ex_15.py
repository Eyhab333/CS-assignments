area = input("Choose an area: (Cairo), (Alexandria) or (Tanta) ")
if area.lower() == "cairo" or area.upper() == "ALEXANDRIA" or area.lower() == "tanta":
    print(f"{area} is on our list.")           
else:
    print(f"Sorry, {area} is not on our list.")           
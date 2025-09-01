nums = []

print("         Agrega tu lista y escribe 'ya' cuando acabes\n")
started = True
while started:
    num = input("ingrese valor: ")
    if num.lower() == "ya":
        break
    nums.append(int(num))
print(f"Tu lista, {nums} \n¿Desea duplicarla?")
action = input("(SI/NO): ").lower()
if action != "no":
    nums = nums + nums
    print(f"Tu lista, {nums} ")
else:
    print("\nHasta la proxima")
    started = False
    
def suma(*nums):
    res=0
    for num in nums:
        res+=num
    return res

numeros=[]
while True:
    num = (input("ingresa los numeros que deseas ingresar o enter para realizar la suma "))
    if num=="":
        break
    numeros.append(float(num))


print(*numeros)
with open("/home/ricardo/Descargas/tcopp.bin", "rb") as f:
    data = f.read()
print(len(data))
print(data)

for x in data:
    print(x, end="")
print()
for x in range(1,len(data)):
    print('divido por: ',x,'da: ',(len(data)-1)/x)
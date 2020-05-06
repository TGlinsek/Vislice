# eratostenovo sito

števila_do_200 = [i + 1 for i in range(200)]
števila_do_200.remove(1)  # ne rabmo enke
števec = 0
while True:
    if števec >= len(števila_do_200):
        break
    prašt = števila_do_200[števec]
    print(prašt)
    števila_do_200 = list(map(lambda x: "prazno" if (x % prašt == 0 and x != prašt) else x, števila_do_200))  # zamenjaj tiste, za katere vemo da niso praštevila, s "prazno"
    for i in range(števila_do_200.count("prazno")):  # odstrani vse elemente, ki so bili zamenjani s "prazno"
        števila_do_200.remove("prazno")
    števec += 1
# print(števila_do_200)  # števila_do_200 zdaj vsebujejo le še vsa praštevila do 200
print("\n🔴 1 - Sinal Vermelho\n")
print("\n🟡 2 - Sinal Amarelo\n")
print("\n🟢 3 - Sinal Verde\n")

sinal = int(input("Qual a cor do semáforo? "))

if sinal == 1:
    print("PARE!")
elif sinal == 2:
    print("ATENÇÃO!")
else:
    print("PROSSIGA!")


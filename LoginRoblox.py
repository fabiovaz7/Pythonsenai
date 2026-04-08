
import webbrowser     

nome = input("Digite seu nome: ")
idade = int(input("Digite seu idade: "))

if idade >= 18:
    print("Acesso Liberado!")
    webbrowser.open("https://roblox.com")
else:
    print(f"{nome}você precisar ser maior de idade!")


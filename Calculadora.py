print("Calculadora")

num1 = input(float("Informe o primeiro número:"))
operador = input("Digite o caracter quer realizar a operacao:.\n"
      f"( SOMA = +)"
      f"( SUBTRACAO = - )"
      f"( MULTIPLICACAO = * )"
      f"( DIVISAO = / )")
num2 = input(float("Informe o segundo número:"))

if operador == "+" : 
    num1+num2 = float(resultado)
elif operador == "-" : 
    num1-num2 =  float(resultado)
elif operador == "*" : 
    num1*num2 =  float(resultado)
elif operador == "/" : 
    num1/num2 =  float(resultado)

print(f"O resultado da operacao é {resultado}")

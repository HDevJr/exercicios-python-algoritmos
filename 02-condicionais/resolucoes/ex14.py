# Enunciado 15:
# # Verificar se três lados formam triângulo (desigualdade).

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Forma um triângulo.")
else:
    print("Não forma um triângulo.")

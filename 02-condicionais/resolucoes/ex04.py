# Enunciado 04:
# Leia as coordenadas (x, y) de um ponto no plano cartesiano e informe:
# - Primeiro Quadrante (x > 0 e y > 0)
# - Segundo Quadrante (x < 0 e y > 0)
# - Terceiro Quadrante (x < 0 e y < 0)
# - Quarto Quadrante (x > 0 e y < 0)
# - Eixo X (y = 0 e x ≠ 0)
# - Eixo Y (x = 0 e y ≠ 0)
# - Origem (x = 0 e y = 0)

coord_x = float(input('Informe a coordenada x: '))
coord_y = float(input('Informe a coordenada y: '))

if coord_x == 0 and coord_y == 0:
    print('Ponto na origem')
elif coord_x == 0:
    print('Eixo Y')
elif coord_y == 0:
    print('Eixo X')
elif coord_x > 0 and coord_y > 0:
    print('Primeiro quadrante')
elif coord_x < 0 and coord_y > 0:
    print('Segundo quadrante')
elif coord_x < 0 and coord_y < 0:
    print('Terceiro quadrante')
else:
    print('Quarto quadrante')

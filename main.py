equip = [ 'Jugador 1', 'Jugador 2', 'Jugador 3', 'Jugador 4', 'Jugador 5']

equip[0] = 'Marc'
equip[1] = 'Juan'
equip[2] = 'Pepe'
equip[3] = 'Raul'
equip[4] = 'Eric'

print(equip)
num=1
for jugador in equip:
  print(f'El jugador {num} es {jugador}')
  num+=1

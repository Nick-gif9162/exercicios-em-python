dias = float(input("Digite a quantidade de dias que não acontecem acidentes :"))
meses = dias / 30
if dias > 30 or dias == 30 :
  print("A quantidade de meses é :", meses)
else:
  if dias > 365 or dias == 365 :
    anos = dias / 360
    print("A quantidade de anos sem acidentes é :", anos)
  else: 
    print("A quantidade de dias sem acidente é :", dias) 
  


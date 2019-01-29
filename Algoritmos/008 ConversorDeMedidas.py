valor = float(input('Digite um valor em metros:  '))

km = valor * 0.001 #quilômetro
hm = valor * 0.01 #hectômetro
dam = valor * 0.1 #decâmetro
dm = valor * 10 #decímetro
cm = valor * 100 #centímetro
mm = valor * 1000 #milímetro

print('{} metros são equivalentes a: \n {}km\n {}hm\n {:.1f}dam\n {:.0f}dm\n {:.0f}cm\n {:.0f}mm\n '.format(valor,km,hm,dam,dm,cm,mm))
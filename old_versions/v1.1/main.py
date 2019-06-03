#coding: utf-8
import numpy as np
import funcs



arq_dpd = open('termos_dpd.txt', 'r')
arq_idpd = open('termos_idpd.txt', 'r')
matriz = tuple(funcs.read_Matriz(arq_dpd.readlines()))
vct_idpd = funcs.read_Matriz(arq_idpd.readlines())


print("\nMatriz Original:	")
funcs.show_Matriz(matriz)
print("\nVetor Independente: ")
funcs.show_Matriz(vct_idpd)

determs = funcs.determ_Matriz(matriz, vct_idpd, True)
if determs[0] != 0:
	vlr_vars = funcs.Cramer(determs, 1)
else:
	print("\nDeterminate da Matriz igual a ZERO!!\n")
	exit(0)
# print("\nValor dos Determinantes: ")
# print(determs)
print("\n\nResultado por Cramer:\n")
for i in range(len(vlr_vars)):
	print("Valor da variável D_{%d}: %f\n" %((i+1), vlr_vars[i]))

res_Gauss = funcs.Gauss(matriz, vct_idpd, 1)
print("\n\nResultado por Gauss:\n")
for i in range(len(res_Gauss)):
	print("Valor da variável D_{%d}: %f\n" %(i+1, res_Gauss[i]))

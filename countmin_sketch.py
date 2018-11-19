# C:\Users\ggalv\Google Drive\Respaldo\Magister\Big Data\Tarea 1			python countmin_sketch.py
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import heapq as hq
import math as mt
import operator
import time
import sys
import hashlib as hl
import random as rd
import xlsxwriter

def ParametrosHash(d):
	hashes=[]
	for i in range(d*2):
		hashes.append(int(float(rd.random())*float(10000)/float(rd.random()) + 1))
	return(hashes)

def Hashing(item,i):
	hashval = (hashes[i]*item+hashes[i+1])%w;
	return(hashval)

def Countminsketch(line):
	for i in range(len(line)):
		item=int(line[i])
		lista_item.add(item)
		for j in range(d):
			hashval=Hashing(item,j)
			sketch[j][hashval]+=1
	return(sketch,lista_item)

def RecuentoCountminsketch(lista_item,recuento):
	lista_item=list(lista_item)
	for i in range(len(lista_item)):
		recuento_temp=[]
		for j in range(d):
			hashval=Hashing(lista_item[i],j)
			recuento_temp.append(sketch[j][hashval])
		recuento_temp=min(recuento_temp)
		recuento[lista_item[i]]=recuento_temp
	return(recuento)		

				

#MAIN
start=time.time()

#Constructor de hash------------------------------------------------------------
eps = 0.002;
gamma = 0.2;
w = mt.ceil(mt.exp(1)/eps);
d = mt.ceil(mt.log(1/gamma));
print("w,d= ",w,d)
hashes=ParametrosHash(d)

#Inicializo lista de sketch y set de items y diccionario de recuento----------------------------------------------------- 
sketch=np.zeros((d,w), dtype=int)
lista_item=set()
recuento={}

#Leo datos y lleno Sketch-------------------------------------------------------
i=0
dataset='eu-2005-adj.txt'
for line in open(dataset):
	line=line.split()
	del line[0]
	sketch,lista_item=Countminsketch(line)




	#Llevo contrl para detener la wea
	# i+=1
	# if i==30:
	# 	break

#Genero el recuento de los items
recuento=RecuentoCountminsketch(lista_item,recuento)
# print(recuento)

#Transformo la salida a un excel
workbook = xlsxwriter.Workbook('Frecuencia Countmin Sketch.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for key in recuento.keys():
    row += 1
    worksheet.write(row, col, key)
    item=recuento[key]
    worksheet.write(row, col + 1, item)

workbook.close()


end=time.time()
print("Tiempo de ejeución= ",end-start)

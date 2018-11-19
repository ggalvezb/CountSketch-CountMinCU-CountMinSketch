datos_reales={}
for i in range(862665):
	datos_reales[i]=0

dataset='eu-2005-adj.txt'
for line in open(dataset):
	line=line.split()
	del line[0]
	for i in range(len(line)):
		item=int(line[i])
		datos_reales[item]+=1
print(datos_reales)		
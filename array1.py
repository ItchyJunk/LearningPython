matrix1 = [['m11','m12','m13'],['m21','m22','m23']]
matrix2 = [['n11','n12'],['n21','n22'],['n31','n32']]
mm = ''
swap = []



for i in range(len(matrix2[0])):
	swap.append([matrix2[j][i] for j in range(len(matrix1[0]))])
	
for list_1, list_2 in matrix1,swap:
	for element_1, element_2 in zip(list_1, list_2):
		mm += element_1 + element_2 + ' ' 

print(mm)
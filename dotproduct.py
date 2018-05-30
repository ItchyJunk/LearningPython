v = [1,2]
u = [2,-1]
dotproduct = 0

for v_element, u_element in zip(v,u):
	dotproduct += (v_element * u_element)

print(dotproduct)
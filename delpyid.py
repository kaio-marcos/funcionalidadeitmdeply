# -*- coding: utf-8 -*-
filename = 'planta rodolfo.svg'

f = open(filename, encoding="utf8")

a = open('rodolfo.svg', 'w')

n = 0
count_id = 0
for x in f:
	n = n+1
	count_id = count_id + x.count('id=" "')
	
	print(count_id)

	y = x.replace('id=" "','id="' + str(count_id) + '"')
	a.write(y)

	print(x)
	

f.close()

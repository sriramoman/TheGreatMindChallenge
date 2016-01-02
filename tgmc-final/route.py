import sys
source = int(sys.argv[1])
dest = int(sys.argv[2])
graph=[[0,5,10,-1,-1],[5,0,3,11,-1],[10,3,0,2,-1],[-1,11,2,0,1],[-1,-1,-1,1,0]]
confirmed=[[source,0,source]]
tentative=[]
map={}
map[0]='a'
map[1]='b'
map[2]='c'
map[3]='d'
map[4]='e'
countDown = len(graph)
if source == dest:
	print "Error!! Why do you want to use public transit to suthify and reach ur own place? Thats not what we've coded for!!"
	exit()
while tentative !=[] or countDown >= 0:
	countDown = countDown - 1
	next=confirmed[len(confirmed)-1][0]
	lsp=[]
	ctrL = 0;
	for j in graph[next]:
		if j != -1 and j != 0:
			lsp.append([ctrL,j])
		ctrL = ctrL+1
	for neighbour in lsp:
		costC = confirmed[len(confirmed)-1][1]
		costT = graph[neighbour[0]][next]
		new_cost = costC + costT
		flag1,flag2=False,False
		flagC,flagT=False,False
		for k in confirmed:
			if k[0] == neighbour[0]:
				flagC = True
		if tentative != []:
			for k in tentative:
				#print '(' + map[k[0]] + ',' + str(k[1]) + ',' + map[k[2]] + ')'
				if k[0] == neighbour[0]:
					flagT = True
					costT = k[1]
		if flagC == False and flagT == False:
			tentative.append([neighbour[0],new_cost,next])
		if flagT == True and new_cost < costT:
			for k in tentative:
				if k[0] == neighbour[0]:
					k[1] = new_cost
					k[2] = confirmed[len(confirmed)-1][0]
	if tentative != []:
		min = tentative[0][1]
		position = 0
		counter = 0
		for t in tentative:
			if t[1] <= min:
				position = counter
				min = t[1]
			counter = counter + 1
		confirmed.append(tentative[position])
		tentative.pop(position)
		if confirmed[len(confirmed)-1][0] == dest:
			break
confirmed.reverse()
print "The Final RIP Boils down to:"
for c in confirmed:
	print '(' + map[c[0]] + ',' + str(c[1]) + ',' + map[c[2]] + ')'
route=[]
route.append(confirmed[0][0])
route.append(confirmed[0][2])
adjoin = route[len(route)-1]
for c in range(1,len(confirmed)):
	if(confirmed[c][0] == adjoin):
		adjoin = confirmed[c][2]
		route.append(adjoin)
route.reverse()
route.pop(0)
routestring=''
for i in route:
	routestring = routestring + "--" + map[i] + "--"
print '''\nYour Route String is :-\n''' + routestring

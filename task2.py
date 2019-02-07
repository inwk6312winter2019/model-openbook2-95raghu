def accessible(data,data1):
	a=0
	for line in data1:
		if line[10]=="ARTERIAL":
			#print(True)
			fdmid=line[23]
			#print(objectid)
			for line1 in data:
				if line1[9]==fdmid:
					#print(True)
					if line1[7]=="Accessible":
						 a=a+1
	return a

def nonstandard(data,data1):
	b=0
	for line in data1:
		if line[10]=="LOCAL STREET":
                        #print(True)
			fdmid=line[23]
                        #print(objectid)
			for line1 in data:
				if line1[9]==fdmid:
                                        #print(True)
					if line1[7]=="Non-Standard":
						b=b+1
	
	return b

def inaccessible(data,data1):
	c=0
	for line in data1:
		if line[10]=="MINOR COLLECTOR":
                        #print(True)
			fdmid=line[23]
                        #print(objectid)
			for line1 in data:
				if line1[9]==fdmid:
                                        #print(True)
					if line1[7]=="Inaccessible":
						c=c+1
        
	return c



data1=[]
data=[]
#opening first file
fout1=open("Bus_Stops.csv")
for line in fout1:
        line=line.split(",")
        data.append(line)
#print(data)
#opening second file
fout2=open("Street_Centrelines.csv")
for line in fout2:
	line=line.split(",")
	data1.append(line)
#print(data1)


print(accessible(data,data1))
print(nonstandard(data,data1))
print(inaccessible(data,data1))


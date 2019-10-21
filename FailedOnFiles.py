import subprocess
i=0
j=0
fill = []
fsuccess=open('SuccessfullyOpenedDataFiles.txt','r')
for lin in fsuccess:
    j+=1
    #print lin
    y1 = lin.split()
    x1 = y1[6].split("/")
    z1 = x1[14]
    a1 = z1.split("_")
    b1 = a1[1].split(".")
    #print z1
    #if(j<3):
    #print z1
    fill.append(b1[0])
    #print "***************************************************************************************"

#print fill



fall=open('AllDataFiles.txt','r')

#for line in fall:
for line in fall:
    #print line
    y = line.split()
    x = y[2].split("\"")
    z = x[1].split("/")
    a = z[11].split("_")
    b = a[1].split(".")
    i+=1
    #print lineOB
    #if(i<3):
    #print line
    #print y
    #print x
    #print z[-1]
    #print z[11]
    if (b[0] not in fill):
        #print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        #print b[0]
        print y[2]
print i, j
print "end"
        

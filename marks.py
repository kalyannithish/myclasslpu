print("Welcome,")
Name = input("Enter Subject Code: " )
print("Your Subject Code is : ",Name,"\n\n")
print("Enter Your  CA Marks")
M1 = (int(input("Enter CA-1 Marks : ")))
M2 = (int(input("Enter CA-2 Marks : ")))
M3 = (int(input("Enter CA-3 Marks : ")))
Att= int(input("Enter Your Attendence %: "))
Mid = int(input("Enter Your Mid Marks(Out of 20): "))
#Finding First Best Of Two CAS
if(M1 > M3 and M1>M2):
        N1 = M1;
elif(M2>M1 and M2>M3):
        N1 = M2;
else:
        N1 = M3;
#Finding second Best of Two CAs
list1 = [M1,M2,M3]
mx=max(list1[0],list1[1])
N2=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>mx:
		N2=mx
		mx=list1[i]
	elif list1[i]>N2 and \
		mx != list1[i]:
		N2=list1[i]
print("Your First Best CA is :" ,N1)
print("Your Second Best CA is :" ,N2,"\n\n\n")
#Finding Average of two CA's
Avg =  ((N1+N2)/2)
print("Average of Best Two CA's is : ",Avg,"Out of 30")
Avg25 = int((Avg*25)/30)
print("Average of Best Two CA's is : ",Avg25,"Out of 25(WEIGHTAGE)","\n\n")
#Attendence :
if(Att>=92):
    A1 = 5;
elif(Att>=85):
    A1 = 4;
elif(Att>=80):
    A1 = 3;
elif(Att>=75):
    A1 = 2;
else:
    A1 = 0;
    print('"YOU HAVE TO GIVE  A REAPPEAR"')
print("For ",Att,"% you have got ",A1,"Marks","\n \n \n")
print("Mid =",Mid,"\n","Attendence marks =",A1,"\n","Avg25 =",Avg25,"\n \n \n")
print("out of 50 marks you got : ",Avg25+Mid+A1)
print("Rest of the Marks You have to Score in End Term :)")

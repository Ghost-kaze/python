print"1.maximum"
print"2.minimum"
car=raw_input("enter:")
def csme():
    if int(car)==1 or int(car)==2:
        var= raw_input("1.enter no. :")
        sar= raw_input("2. enter no. :")
        cra= raw_input("3. enter no. :") 
    else:
        return sam(car)
def sam(car):
    if int(car)==1:
        x=int(csme())
        print max(int(var),int(sar),int(cra))
    elif int(car)==2:
        c=csme()
        print min(int(var),int(sar),int(cra))
    else :
        print"choose one :"
       
sam(car)
csme()

#main.py
'''
fp=open("data.txt","w")
#print(fp)
#print(type(fp))

#d="hello all"
#d="good evening"
#fp.write(d)
fp=open("data.txt","a")
d="good night"
fp.write(d)

fp.close()
'''
# contact directory project
def searchbymobile():
    smob=input("enter the number to be searched")
    fp=open("data.txt","r")
    data=fp.readlines()
    #print(data)
    for x in data:
        t=x.split(":")
        if smob+"\n"==t[1]:
                print("name",t[0])
                print("mobile no",t[1])
                break
    else:
                print("CONTACT NOT FOUND!!!")
#delete record

def delete_record():
    smob=input("enter the no. to be deleted")
    fp=open("data.txt","r")
    data=fp.readlines()
    for x in data:
            print(x)
            rec=x.split(":")
            if smob+"/n"==rec[1]:
                print("found:",+x)
            else:
                print("contact not found,please create it")
            data.remove(x)
            fp1=open("data.txt","w")
            newdata="".join(data)
            print(newdata)
            fp1.write(newdata)
            fp1.close()

#update record
def update_record():
    smob=input("enter the mobile number")
    fp=open("data.txt","r")
    data=fp.readlines()
    for x in data:
            print(x)
            rec=x.split(":")
            if smob+"/n"==rec[1]:
                print("1.upadte mobile number")
                print("2.update name")
                ch=input("enter your choice:")
                if ch=='1':
                    newmob=input("enter the new number")
                    rec[1]=newmob+'\n'
                    data.remove(x)
                    temp=':'.join(rec)
                    data.append(temp)
                    fdata=''.join(data)
                    fp1=open("data.txt","w")
                    fp1.write(fdata)
                    fp1.close()
                    print("record updated successfully")
                elif ch=='2':
                    print("update name")
                else:
                    print("please enter valid choice")
                    break
    else:
        print("no record found")
while True:
    print()
    print("1.ADD CONTACT")
    print("2.VIEW CONTACT")
    print("3.UPDATE CONTACT")
    print("4.DELETE CONTACT")
    print("5.SEARCH BY MOBILE NUMBER")
    print("6.SEARCH BY NAME")
    print("7.EXIT")
    ch=input("Enter Your Choice: ")

    if ch=='1':
        fp=open("data.txt","a")
        n=input("enter your name")
        mob=input("enter your mobile number")
        d=n+":"+mob +"\n"
        fp.write(d)
        fp.close()
    elif ch=='2':
        fp=open("data.txt","r")
        cdata=fp.read()
        print("CONTACT DIRECTORY")
        print("===============================")
        print(cdata)
        fp.close()
        pass
    elif ch=='3':
         update_record()
    elif ch=='4':
         delete_record()
         pass
    elif ch=='5':
        searchbymobile()
    elif ch=='6':
        pass
    elif ch=='7':
        print("THANKS FOR USING THIS APPLICATION !!!")
        break
    else:
        print("PLEASE ENTER A VALID CHOICE")




    












         


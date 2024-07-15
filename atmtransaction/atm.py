acc={'name':'yadhav','balance':1000}
print (acc)
while True:
    print("1.deposit")
    print("2.Withdraw")
    print("3.Exit")
    ch=input("enter your choice:")
    if ch=="1":
        am=int(input("Enter Amount: "))
        acc["balance"]=acc["balance"]+am
        print(acc)
    elif ch=="2":
        am=int(input("Enter Amount: "))
        if am>acc["balance"]:
            print("insuffiicient fund")
        else:
            acc["balance"]=acc["balance"]-am
            print(acc)
            break
     
        
        
        
    
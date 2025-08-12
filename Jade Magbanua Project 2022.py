#PList=[]
def MainMenu(Main):
    print("Welcome to Shop Domain online.")
    print ("1. Add Product\n2. Search Product\n3. Update Product\n4. Buy Product\n5. Exit")
    Operation=str(input("Please select one of the following options: "))
    if Operation=="1":
        print("Welcome to add product option")
        def AddProduct(PID):
            if PID in ID:
                return True
            else:
                return False
        def CheckProduct(PID):
            if (AddProduct(PID)==True):
                print("That product code is existing in the system, please enter a new one.")
                PID=int(input("Please enter new product code: "))
                CheckProduct(PID)
            if (AddProduct(PID)==False):
                print("Please enter properties")
                Category=str(input("Product category: "))
                Name=str(input("Enter product name: "))
                Model=(input("Enter product model: "))
                Price=float(input("Enter Product price: $"))
                Quantity=int(input("Enter quantity: "))
                while (Quantity<10 or Quantity>50):
                    if Quantity<10 or Quantity>50:
                        print("Please choose a quantity between 10 to 50")
                        Quantity=int(input("Enter quantity: "))
                        
                Add_More=str(input("Do you want to add more products? Enter yes or no: "))
                if Add_More=="no":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                elif Add_More=="No":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                elif Add_More=="NO":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                    
                elif Add_More=="yes":
                    PID=int(input("Please enter new product code: "))
                    CheckProduct(PID)
                elif Add_More=="Yes":
                    PID=int(input("Please enter new product code: "))
                    CheckProduct(PID)
                elif Add_More=="YES":
                    PID=int(input("Please enter new product code: "))
                    CheckProduct(PID)
        ID=[101,102,103]
        PID=int(input("Please enter new product code: "))
        CheckProduct(PID)
        
    if Operation=="2":
        print ("Welcome to search product option.")
        #PID=int(input("Please enter product code:"))
        def CheckProduct_2(SID):
            if SID in ID:
                return True
            else:
                return False
        def SearchProduct(SID):
            if (CheckProduct_2(SID)==True):
                if SID==101:
                    Index_No=ID.index(SID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                if SID==102:
                    Index_No=ID.index(SID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                if SID==103:
                    Index_No=ID.index(SID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                SMore=str(input("Do you want to search other products? Enter yes or no: "))
                if SMore=="no":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                elif SMore=="No":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                elif SMore=="NO":
                    print("Thank you, Goodbye.")
                    print("")
                    MainMenu(Operation)
                elif SMore=="yes":
                    SID=int(input("Please enter product code: "))
                    SearchProduct(SID)
                elif SMore=="Yes":
                    SID=int(input("Please enter product code: "))
                    SearchProduct(SID)
                if SMore=="YES":
                    SID=int(input("Please enter product code: "))
                    SearchProduct(SID)   
            if (CheckProduct_2(SID)==False):
                print("The code is not in the system.")
                SID=int(input("Please enter product code: "))
                SearchProduct(SID)
        Properties=["Category","Name","Model","Price","Quantity"]
        Category=["Mobile","Computer","Watch"]
        Name=["Eye-Phone","Racer G17","Mango Watch"]
        Model=[2022,"G2003",2021]
        Price=["$1,200","$5,000","$612"]
        Quantity=[40,46,35]
        ID=[101,102,103]
        SID=int(input("Please enter product code: "))
        SearchProduct(SID)
        
    if Operation=="3":
        print("Welcome to update product option.")
        def CheckProduct_3(UID):
            if UID in ID:
                return True
            else:
                return False
        def UpdateProduct(UID):
            if (CheckProduct_3(UID)==False):
                print("Sorry ID cannot be found.")
                UID=int(input("Please enter the product code you want to update: "))
                UpdateProduct(UID)
            if (CheckProduct_3(UID)==True):
                if UID==101:
                    Index_No=ID.index(UID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                if UID==102:
                    Index_No=ID.index(UID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                if UID==103:
                    Index_No=ID.index(UID)
                    print("Product details:")
                    print("Category:",Category[Index_No],"\nName:",Name[Index_No],"\nModel:",Model[Index_No],"\nPrice",Price[Index_No],"\nQuantity:",Quantity[Index_No])
                IndexNo=ID.index(UID)
                FQ=str(input("Do you want to update the category? Please enter yes or no: "))
                if FQ=="yes":
                    NewCategory=input("Enter new Category: ")
                    Category[IndexNo]=NewCategory
                if FQ=="Yes":
                    NewCategory=input("Enter new Category: ")
                    Category[IndexNo]=NewCategory
                if FQ=="YES":
                    NewCategory=input("Enter new Category: ")
                    Category[IndexNo]=NewCategory
                    
                SQ=str(input("Do you want to update the Name? Please enter yes or no: "))
                if SQ=="yes":
                    NewName=input("Enter new Name: ")
                    Name[IndexNo]=NewName
                if SQ=="Yes":
                    NewName=input("Enter new Name: ")
                    Name[IndexNo]=NewName
                if SQ=="YES":
                    NewName=input("Enter new Name: ")
                    Name[IndexNo]=NewName
                    
                    
                TQ=str(input("Do you want to update the Model? Please enter yes or no: "))
                if TQ=="yes":
                    NewModel=input("Enter new Model: ")
                    Model[IndexNo]=NewModel
                if TQ=="Yes":
                    NewModel=input("Enter new Model: ")
                    Model[IndexNo]=NewModel
                if TQ=="YES":
                    NewModel=input("Enter new Model: ")
                    Model[IndexNo]=NewModel
                    
                    
                FOQ=str(input("Do you want to update the price? Please enter yes or no: "))
                if FOQ=="yes":
                    NewPrice=float(input("Enter new price: $"))
                    Price[IndexNo]=NewPrice
                if FOQ=="Yes":
                    NewPrice=float(input("Enter new price: $"))
                    Price[IndexNo]=NewPrice
                if FOQ=="YES":
                    NewPrice=float(input("Enter new price: $"))
                    Price[IndexNo]=NewPrice
                    
                FIQ=str(input("Do you want to update the quantity? Please enter yes or no: "))
                if FIQ=="yes":
                    NewQuantity=int(input("Enter new quantity: "))
                    Quantity[IndexNo]=NewQuantity
                if FIQ=="Yes":
                    NewQuantity=int(input("Enter new quantity: "))
                    Quantity[IndexNo]=NewQuantity
                if FIQ=="YES":
                    NewQuantity=int(input("Enter new quantity: "))
                    Quantity[IndexNo]=NewQuantity
                print("The updated informations are:","\nCategory:",Category[IndexNo],"\nName:",Name[IndexNo],"\nModel:",Model[IndexNo],"\nPrice: $",Price[IndexNo],"\nQuantity:",Quantity[IndexNo])
                print("")
                MainMenu(Operation)
                
        Properties=["Category","Name","Model","Price","Quantity"]
        Category=["Mobile","Computer","Watch"]
        Name=["Eye-Phone","Racer G17","Mango Watch"]
        Model=[2022,"G2003",2021]
        Price=["$1,200","$5,000","$612"]
        Quantity=[40,46,35]
        ID=[101,102,103]
        UID=int(input("Please enter the product code you want to update: "))
        UpdateProduct(UID)

    if Operation=="4":
        print("Welcome to buy product option.")
        def CheckProduct_4(BID):
            if BID in ID:
                return True
            else:
                return False
        def BuyProduct(BID):
            if (CheckProduct_4(BID)==False):
                print ("The code is not in the system.")
                BID=int(input("Please enter product code: "))
                BuyProduct(BID)
            if (CheckProduct_4(BID)==True):
                if BID==101:
                    IndexNo=ID.index(BID)
                    #ProPrice_1=1200
                    print("Item details:","\nCategory:",Category[IndexNo],"\nName:",Name[IndexNo],"\nModel:",Model[IndexNo],"\nPrice:",Price[IndexNo])
                    PQ=int(input("Please enter quantity:"))
                    if (PQ>40):
                        print("There are only 40 'Eye-phones' in stock available.")
                        AProduct=str(input("Do you want to change the quantity? please enter yes or no: "))
                        if AProduct=="yes":
                            BuyProduct(BID)
                        if AProduct=="Yes":
                            BuyProduct(BID)
                        if AProduct=="YES":
                            BuyProduct(BID)
                        else:
                            print("Thank you, Goodbye")
                            MainMenu(Operation)
                    elif (PQ>10 and PQ<20):
                        DisProduct=PQ * 1200
                        PDiscount=DisProduct * 0.1
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>20 and PQ<30):
                        DisProduct=PQ * 1200
                        PDiscount=DisProduct * 0.2
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>30):
                        DisProduct=PQ * 1200
                        PDiscount=DisProduct * 0.3
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    else:
                        DisProduct=PQ * 1200
                        print("The total price is: $",DisProduct)
                        print("")
                        MainMenu(Operation)
                
                if BID==102:
                    IndexNo=ID.index(BID)
                    #ProPrice_1=1200
                    print("Item details:","\nCategory:",Category[IndexNo],"\nName:",Name[IndexNo],"\nModel:",Model[IndexNo],"\nPrice:",Price[IndexNo])
                    PQ=int(input("Please enter quantity:"))
                    if (PQ>46):
                        print("There are only 46 'Racer G17' in stock available.")
                        AProduct=str(input("Do you want to change the quantity? please enter yes or no: "))
                        if AProduct=="yes":
                            BuyProduct(BID)
                        if AProduct=="Yes":
                            BuyProduct(BID)
                        if AProduct=="YES":
                            BuyProduct(BID)
                        else:
                            print("Thank you, Goodbye")
                            MainMenu(Operation)
                    elif (PQ>10 and PQ<20):
                        DisProduct=PQ * 5000
                        PDiscount=DisProduct * 0.1
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>20 and PQ<30):
                        DisProduct=PQ * 5000
                        PDiscount=DisProduct * 0.2
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>30):
                        DisProduct=PQ * 5000
                        PDiscount=DisProduct * 0.3
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    else:
                        DisProduct=PQ * 5000
                        print("The total price is: $",DisProduct)
                        print("")
                        MainMenu(Operation)
                
                if BID==103:
                    IndexNo=ID.index(BID)
                    #ProPrice_1=1200
                    print("Item details:","\nCategory:",Category[IndexNo],"\nName:",Name[IndexNo],"\nModel:",Model[IndexNo],"\nPrice:",Price[IndexNo])
                    PQ=int(input("Please enter quantity:"))
                    if (PQ>35):
                        print("There are only 35 'Mango watch' in stock available.")
                        AProduct=str(input("Do you want to change the quantity? please enter yes or no: "))
                        if AProduct=="yes":
                            BuyProduct(BID)
                        if AProduct=="Yes":
                            BuyProduct(BID)
                        if AProduct=="YES":
                            BuyProduct(BID)
                        else:
                            print("Thank you, Goodbye")
                            print("")
                            MainMenu(Operation)
                    elif (PQ>10 and PQ<20):
                        DisProduct=PQ * 612
                        PDiscount=DisProduct * 0.1
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>20 and PQ<30):
                        DisProduct=PQ * 612
                        PDiscount=DisProduct * 0.2
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    elif (PQ>30):
                        DisProduct=PQ * 612
                        PDiscount=DisProduct * 0.3
                        ProductSum=DisProduct-PDiscount
                        print("The total price is: $",ProductSum)
                        print("")
                        MainMenu(Operation)
                    else:
                        DisProduct=PQ * 612
                        print("The total price is: $",DisProduct)
                        print("")
                        MainMenu(Operation)
                        
                        
        Properties=["Category","Name","Model","Price","Quantity"]
        Category=["Mobile","Computer","Watch"]
        Name=["Eye-Phone","Racer G17","Mango Watch"]
        Model=[2022,"G2003",2021]
        Price=["$1,200","$5,000","$612"]
        Quantity=[40,46,35]
        ID=[101,102,103]
        BID=int(input("Please enter the product code you want to buy: "))
        BuyProduct(BID)
    if Operation=="5":
        print("Thank you, Goodbye")
        exit()
Main="yes"
MainMenu(Main)


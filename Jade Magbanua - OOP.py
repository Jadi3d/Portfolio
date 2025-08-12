class Product:
    Product_Code=0
    Product_Name=0
    Product_Price=0
    Product_Quantity=0
    def __init__(self,Code,Name,Price,Quantity):
        self.Product_Code = Code
        self.Product_Name = Name
        self.Product_Price = Price
        self.Product_Quantity = Quantity
    def DisplayDetail(self):
        print("Product Code:",self.Product_Code)
        print("Product Name: ",self.Product_Name)
        print("Product Price: $",self.Product_Price)
        print("Product Quantity: ",self.Product_Quantity)
    def ApplyDiscount(self):
        TPrice=self.Product_Price*self.Product_Quantity
        DisPrice=TPrice-self.Product_Price*0.1
        return DisPrice
        
    
Product01=Product(101,"Eye-phone",1200,40)
Product01.DisplayDetail()
Product02=Product(102,"Racer G17",5000,46)
Product02.DisplayDetail()
Product03=Product(103,"Mango watch",612,35)
Product03.DisplayDetail()
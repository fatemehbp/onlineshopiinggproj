
class User:
    def __init__(self,name=None,password=None,phonenumber=None):
         self.name=name
         self.password=password
         self.phonenumber=phonenumber
         self.addresses=[]
         self.orders=[]
         self.is_login=False
         self.is_admin=False

    def add_addresses(self,addresses):
         self.addresses.append(addresses)
         return self.add_addresses
    
    def login(self,password,phonenumber):
         if self.password==password and self.phonenumber==phonenumber:
              self.is_login=True
              print(f"welcome {self.name} with { self.phonenumber}")
         else:
              print("try agin")

    def add_order(self,order):
         if self.is_login==True :
              self.orders.append(order)
         else:
              print("user doesnot login")

class Product:
     def __init__(self,name=None,price=None,explian=None,mogodi=None):
          self.name=name
          self.price=price
          self.explian=explian
          self.mogodi=mogodi

     def __str__(self):
          return f"{self.name}:{self.explian} with{self.price}$"
     
     def sort_products(self,products=None,sort_by=None):
          self.products=products
          self.sort_by=sort_by

          if sort_by=="price":
               return sorted(products, key=lambda x: x.price)
          elif sort_by=="mogodi":
               return sorted(products, key=lambda x: x.mogodi)
          else:
               print("choose how to sort")
        

     def is_mogodi(self,measure):
         if self.mogodi>=measure:
              return self.mogodi>=measure
         else:
              print("mogodi less than your measure")
    
     def update_mogodi(self,measure):
          self.mogodi=self.mogodi-measure
          
    

class Shopping_cart:
     def __init__(self):
          self.products=[]
          self.measures=[]

     def add_item(self,product,measure):
           if self.is_login==True :
                if product.is_mogodi(measure):
                       self.products.append(product)
                       self.measures.append(measure)
                       product.update_mogodi(measure)
                       print(f"{product.name} added")
                else:
                     print("not enough mogodi")
           else:
                print("user doesnot login")

     def payment(self):
          total=0
          for i in range(len(self.products)):
               total=total+self.products[i]*self.measures[i]
          return total
     
     
class Core:
    def __init__(self):
        self.users=[]
        self.products=[]
        self.orders=[]
        
    def register (self,name,password,phonenumber):
        user=User(name,password,phonenumber,is_admin=False)
        self.users.append(user)
        print(f"user{name} with{phonenumber} register")
        
    def add_product(self,admin,name,price,mogodi,explian):
        if admin.is_admin:
            product=product(name,price,mogodi,explian)
            self.products.append(product)
            print(f"product{name} with{price}$ with{mogodi} added")
        else:
            print("admins can add products")
        
    def edit_product(self,admin,product_name,new_name=None,new_price=None,new_explian=None,new_mogodi=None ):
         if admin.is_admin:
              for product in  self.products:
                   if product.name==product_name:
                        if new_name:
                             product.name=new_name
                        if new_price:
                             product.price=new_price
                        if new_mogodi is not None:
                             product.mogodi=new_mogodi
                        if new_explian:
                             product.expian=new_explian
                        print(f"product{product_name} updated")
                        return
                   else:
                          print(f"product {product_name} not found")
         else:
               print("admins can edit products")
               
    def delet_product(self,admin,product_name):
         if admin.is_admin:
              for product in self.products:
                   if product.name==product_name:
                        self.products.remove(product)
                        print(f"product{product_name} deleted")
                        return
                   else:
                        print(f"product{product_name} not found")
         else:
              print("admins can delet products")
     
    def seach_product(self,name=None):
     result=[]
     if name:
          for product in self.products:
               if name in product.name:
                    result.append(product)
               else:
                    print(f"{name} not found")
     return result
               
    def add_shopping_cart(self,user,product_name,measure):
         if user.is_login:
              for product in self.products :
                   if Product.name==product_name:
                        if product.is_mogodi(measure):
                             user.shopping_cart.add_item(product,measure)
                             print(f"{product_name} with{measure} added toyour shopping cart")
                             return
                        
                        else:
                            print("not enough mogodi")
                            return
                   else:
                        print(f"{product_name} not found")
         else:
              print("you need to login for this work")
              return
         
    def nahayi(self,user):
         if user.is_login:
              
               
                   
            
               
                
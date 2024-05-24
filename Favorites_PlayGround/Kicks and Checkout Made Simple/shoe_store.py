class Shoes:
    """
    A class that holds the information about a shoe.
    """
    def __init__(self,brand,category,name,price,stock):
        """
        Defines the necessary attributes to their corresponding values
        """
        self.brand = brand
        self.category = category
        self.name = name
        self.price = price
        self.stock = stock

    def get_info(self):
      """
      Returns a dictionary containing a shoe products information.

      Dictionary returns:
          - brand(str): The shoe brand
          - category(str): The type of shoe(ex.Running)
          - name(str): The name of the shoe
          - price(int): The price of the shoe
          - stock(int): Amount of shoes left in stock
      Returns:
        A dictionary containing shoe info
      """
      return {
          "brand": self.brand,
           "category":self.category,
           "name":self.name,
           "price":self.price,
           "stock":self.stock,
           "is_expensive":"Expensive" if self.price >= 250 else "Not Expensive",
      }
    
def Create_Shoe(brand,category,name,price,stock):
   """
   Returns a shoe object

   Args:
      - brand(str): The shoe brand
      - category(str): The type of shoe(ex.Running)
      - name(str): The name of the shoe
      - price(int): The price of the shoe
      - stock(int): Amount of shoes left in stock
    Return:
      return a shoe object
   """
   return Shoes(brand,category,name,price,stock)

#All shoes in the jordan category
jordan_shoes = {
   "Jordan 1":Create_Shoe("Jordan","Basketball","Jordan 1", 145, 30),
   "Jordan 11 Bred":Create_Shoe("Jordan","Basketball","Jordan 11 Bred",350,6)
}
#All shoes in New Balance category
new_balance_shoes = {
   "New Balance 990":Create_Shoe("New Balance","Running","New Balance 990",185,56),
   "New Balance 2002r Nite Tide":Create_Shoe("New Balance","Running","New Balance 2002r Nite Tide",145,26)
}
#All shoes in the Yeezy category
yeezy_shoes = {
   "Yeezy Boost 700":Create_Shoe("Adidas","Running","Yeezy Boost 700",350,10),
   "Yeezy Boost 350":Create_Shoe("Adidas","Running","Yeezy Boost 350",230,2)
}
#Shoe dictionary access each shoe based on brand
shoes = {
   "Jordans":jordan_shoes,
   "New Balance":new_balance_shoes,
   "Yeezys":yeezy_shoes
}
#DTLR inventory
DTLR = {
   "Inventory_Value":sum(shoe.price * shoe.stock for shoe_dict in shoes.values() for shoe in shoe_dict.values())
}

def main():
  """
  Introduces user to store and store owner and gets user budget then calls options function.

  Args:
    budget(int): user budget
  
  """
  print("Reggie: Welcome to DTLR! We have all the hottest fashion and clothes. However due to a time shortage we only have the hottest shoes at the moment.")
  while True:
    try:
      budget = int(input("Reggie: I'm Reggie may I know your budget for today valued customer?\nMe: currently I only have $500 in the bank so I will set my budget between 0-$400.\nMe:My budget is $ "))
      if budget < 0 or budget > 400:
        print("\nMe: That budget is not valid, I have to choose a budget between 0 and 400.")
      else:
        break
    except:
      print("Reggie:Make sure you entered a price.")
  options(budget,shoes)
  
   
def options(budget,all_shoes):
  """
  Gives the user a list of shoe options within the users price range. And calls checkout function.

  Args:
    budget(int): max price user is willing to pay
    all_shoes: shoe dictionary

  """
  affordable_shoes = []#stores shoes the user can afford
  for brand,shoe_dict in all_shoes.items():
    for shoe in shoe_dict.values():
      if budget >= shoe.price:
        affordable_shoes.append(shoe)
  if len(affordable_shoes) > 0:#checks if user can afford anything in the store
    print("\nReggie:Uhhh based on your budget I think you can get...")
    for shoes in affordable_shoes:
        shoe_info = shoes.get_info()
        print(f"{shoe_info['name']} for ${shoe_info['price']} {shoe_info['is_expensive']}")
  else:
    print("\nReggie: You cannot buy anything in our store we have nothing that cheap.")
    return main()
  CheckOut(budget,all_shoes)

def CheckOut(budget,all_shoes):
  """
  User is prompted to select a shoe brand and shoe they would like to purchase. Additionally, we see how much user saved by budgeting. Finally we return the inventory value of the shoe store after the purchase.

  Args:
    budget(int): max price user is willing to pay
    all_shoes: shoe dictionary
  
  Return: 
    DTLR(Dictionary): Dictionary containing inventory value 
  """

  print("\nReggie:So what item would you like to purchase?\n \nTip:Use the keyword to answer Reggie.\n\nKeywords:")
  for brand,shoe_dict in all_shoes.items():
    for shoe in shoe_dict.values():
      print(f"brand:{brand} | shoe name:{shoe.name}")
      break
  brand_input = input("\nReggie: First Select a brand.\nEnter the shoe brand: ")
  shoe_input = input("\nReggie: Splendid! Now tell me the name of shoe.\nEnter the shoe name: ")

  selected_shoe_dict = shoes.get(brand_input)
  if selected_shoe_dict:
    selected_shoe = selected_shoe_dict.get(shoe_input)
    if selected_shoe:
      cost = selected_shoe.price
      if cost <= budget:
        wallet = budget - cost
        selected_shoe.stock -= 1
        inventory = (DTLR["Inventory_Value"]-cost)
        print(f"\nMe: Welp I managed to save ${wallet+100} in my wallet\n\nReggie: Thanks for your purchase! Our store now has an inventory value of ${inventory}\n\nReggie:...Uhh I don't know why I told you that hehe.")
            
      elif cost > budget:
        print("\nMe: I can't afford this without going over my budget")
    else:
      print("\nReggie: That shoe may not exist orr you spelled something wrong.")

    return DTLR
  else:
    print(f"\nReggie: Wait a minute I am not sure what brand {brand_input} is please try again using the key words.")
    return CheckOut(budget,all_shoes)
main()


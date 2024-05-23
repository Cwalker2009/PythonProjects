class Shoes:
  def __init__(self, brand, category, name, price,stock):# Defines the constructor for the Shoes class
    self.brand = brand
    self.category = category
    self.price = price
    self.name = name
    self.stock = stock
  def get_info(self): 
    return {
            "brand": self.brand,
            "category": self.category,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "is_expensive": "Expensive" if self.price >= 250 else "Not Expensive",
        }

def Create_Shoe(brand, category, name, price,stock):
  return Shoes(brand, category, name, price,stock)
      
jordan_shoes = {
  "Jordan 1":Create_Shoe("Jordan", "Basketball", "Jordan 1", 145, 30)
}
new_balance_shoes = {
  "New Balance 990": Create_Shoe("New Balance", "Running", "New Balance 990", 185, 56)
}
yeezy_shoes = {
  "Yeezy Boost 700":Create_Shoe("Adidas", "Running", "Yeezy Boost 700", 350, 10)
}

shoes = {
  "Jordans":jordan_shoes,
  "New Balance":new_balance_shoes,
  "Yeezys":yeezy_shoes
}

DTLR = {
  "Inventory_Value":sum(shoe.price * shoe.stock for shoe_dict in shoes.values() for shoe in shoe_dict.values())
}


def main():
  print("Welcome to DTLR! We have all the hottest fashion and clothes. However due to a time shortage we only have the hottest shoes at the moment.")
  while True:
    budget = int(input("Reggie: I'm Reggie may I know your budget for today valued customer?\n \nme: currently I only have $500 in the bank my budget can be between 0-$400.\n \nmy budget is $ "))
    if budget < 0 or budget > 400:
      print("Me: That budget is not valid, I have to choose a budget between 0 and 400.")
    else:
      break
      
  options(budget,shoes)



def options(budget, all_shoes):
  affordable_shoes = []
  for brand,shoe_dict in all_shoes.items():
    for shoe in shoe_dict.values():
      if budget >= shoe.price:
        affordable_shoes.append(shoe)
  if len(affordable_shoes) > 0:
    print("Reggie:Uhhh based on your budget I think you can get..." )
    for shoes in affordable_shoes:
        shoe_info = shoes.get_info()
        print(f"{shoe_info['name']} for ${shoe_info['price']} {shoe_info['is_expensive']}")
  else:
    print("Reggie: You cannot buy anything in our store we have nothing that cheap")
    return main()
  CheckOut(budget, all_shoes)


def CheckOut(budget, all_shoes):
  #first we need to know what shoe the user wants
  #Once we get the shoe we want to look through the shoe dictionary and figure out the price and then subtract that price from the total amount of inventory
  print("Reggie: so what item would you like to purchase?\nTip: Use the keyword to answer Reggie. \nKeywords:")
  for brand, shoe_dict in all_shoes.items():
    for shoe in shoe_dict.values():
      print(f"brand:{brand} | shoe name:{shoe.name}")
      break
  user_brand_selection = input("Reggie: First Select a brand.\nEnter the shoe brand: ")
  user_shoe_selection = input("Reggie: Splendid! Now tell me the name of the shoe.\nEnter the shoe name: ")

  selected_shoe_dict = shoes.get(user_brand_selection)
  if selected_shoe_dict:
    selected_shoe = selected_shoe_dict.get(user_shoe_selection)
    if selected_shoe:
      cost = selected_shoe.price
      wallet = budget - cost 
      selected_shoe.stock -= 1
      inventory = (DTLR["Inventory_Value"]) - cost
      print(f"Me: Welp I managed to save ${wallet} in my wallet")
      print(f"Reggie: Thanks for your purchase! Our store now has an inventory value of ${inventory} \nReggie:...Uhh I don't know why I told you that hehehe.")
    else:
       print("Reggie: That shoe may not exist orrr you spelled something wrong." )
    
    
    return DTLR
  else:
    print(f"Reggie: Wait a minute I am not sure what brand {user_brand_selection} is please try again using the key words" )
    return CheckOut(budget,all_shoes)
main()

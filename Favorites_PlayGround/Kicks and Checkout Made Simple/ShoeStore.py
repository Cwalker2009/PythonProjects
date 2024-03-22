class Shoes:
  def __init__(self, brand, category, name, price):# Defines the constructor for the Shoes class
    self.brand = brand
    self.category = category
    self.price = price
    self.name = name
  def getBrand(self):# Defines a method to return the brand of the shoe
    return "This is a {} shoe".format(self.brand)

  def getCategory(self):# Defines a method to return the category of the shoe
    return "This is a {} shoe".format(self.category)

  def getName(self): # Defines a method to return the name of the shoe
    return self.name

  def getPrice(self):# Defines a method to return the price of the shoe
    return "This shoe costs {}".format(self.price)
  def isExpensive(self):# Defines a method to check if the shoe is expensive
      if self.price >= 250:
        return "The {} {} are expensive".format(self.brand,self.name)

      elif self.price <= 250:
        return "The {} {} are not expensive".format(self.brand,self.name)

      
Jordan1 = {
  "name":"Jordan 1",
  "brand":"Jordan",
  "price":145,
  "stock":30,  
  "category":"Basketball"
}
NewBalance990 = {
  "name":"New Balance 990",
  "brand":"New Balance",
  "price":185,
  "stock":8,
  "category":"Running"
}
YeezyBoost700 = {
  "name":"Yeezy Boost 700",
  "brand":"Adidas",
  "price":350,
  "stock":10,
  "category":"Running"
}

DTLR = {
  "Yeezys":YeezyBoost700,
  "Jordans":Jordan1,
  "NB":NewBalance990,
  "Inventory_Value":sum(shoe["price"] * shoe["stock"] for shoe in [Jordan1,NewBalance990,YeezyBoost700])
}


def main():
  print("Welcome to DTLR! We have all the hottest fashion and clothes. However due to a time shortage we only have the hottest shoes at the moment.")
  while True:
    budget = int(input("Reggie: I'm Reggie may I know your budget for today valued customer?\n \nme: currently I only have $500 in the bank my budget can be between 0-$400.\n \nmy budget is $ "))
    if budget < 0 or budget > 400:
      print("Me: That budget is not valid, I have to choose a budget between 0 and 400.")
    else:
      break
      
  options(budget)



def options(budget):
  tempDict = {145:"Jordan 1s",
              185:"New Balance990s",
              350:"YeezyBoost700s"
             }
  
  if budget >= min(tempDict):
    print("Reggie:Uhhh based on your budget I think you can get..." )
  for i in tempDict:
    if i <= budget:
      shoes = Shoes("Shoes","Feet",tempDict[i],i)# Creates a shoe object with placeholders for brand and category (fix needed)
      print(tempDict[i], "for $", i, "\n",shoes.isExpensive())

    elif budget < min(tempDict) :
      print("Reggie: You cannot buy anything in our store we have nothing that cheap")
      return main()
  CheckOut(budget)


def CheckOut(budget):
  # Classify the shoe as expensive or not
  #first we need to know what shoe the user wants
  #Once we get the shoe we want to look through the shoe dictionary and figure out the price and then subtract that price from the total amount of inventory
  print("Reggie: so what item would you like to purchase?\nTip: Use the keyword to answer Reggie. \nKeywords: \n'Yeezys' = YeezyBoost700s' \n 'Jordans' = Jordan1s' \n 'NB' = 'NewBalance990s' ")
  checkout = input("Me: ")
  if checkout == "Yeezys":
    cost = DTLR[checkout]["price"]
    wallet = budget - cost 
    inventory = (DTLR["Inventory_Value"]) - cost
    print("Me: Welp I only have $", wallet, "left")
    print("Reggie: Thanks for your purchase! Our store now has an inventory value of $", inventory, "\nReggie:...Uhh I don't know why I told you that hehehe.")
  elif checkout == "Jordans":
    cost = DTLR[checkout]["price"]
    wallet = budget - cost 
    inventory = (DTLR["Inventory_Value"]) - cost
    print("Me: Welp I only have $", wallet, "left")
    print("Reggie: Thanks for your purchase! Our store now has an inventory value of $", inventory, "\nReggie:...Uhh I don't know why I told you that hehehe.")
  elif checkout == "NB":
    cost = DTLR[checkout]["price"]
    wallet = budget - cost 
    inventory = (DTLR["Inventory_Value"]) - cost
    print("Me: Welp now I only have $", wallet, "left")
    print("Reggie: Thanks for your purchase! Our store now has an inventory value of $", inventory, "\nReggie:...Uhh I don't know why I told you that hehehe.")
  
  
    
    
  
main()
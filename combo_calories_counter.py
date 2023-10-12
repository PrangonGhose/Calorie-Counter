from calorie_counter import calorie_counter

def combo_calories_counter(*args):
  combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
  }

  total = 0

  for arg in args:
    if arg in combos:
      for item in combos[arg]:
        total += calorie_counter(item)
    else:
      total += calorie_counter(arg)
  return total
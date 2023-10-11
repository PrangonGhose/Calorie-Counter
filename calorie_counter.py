def calorie_counter(*args):
  calories = {
    'Hamburger': 600,
    'Cheese Burger': 750,
    'Veggie Burger': 400,
    'Vegan Burger': 350,
    'Sweet Potatoes': 230,
    'Salad': 15,
    'Iced Tea': 70,
    'Lemonade': 90,
  }

  total = 0

  for arg in args:
    total += calories[arg] if arg in calories else 0
  return total
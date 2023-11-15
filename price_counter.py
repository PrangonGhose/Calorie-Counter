from load_data import load_data

all_meals = load_data("data/meals.json")
all_combos = load_data("data/combos.json")

def price_counter(orders):
  meals = all_meals['meals']
  combos = all_combos['combos']

  total = 0

  for order in orders:
    if 'combo' in order:
      for combo in combos:
        if order == combo['name']:
          total += combo['price']
    else:
      for meal in meals:
        if order == meal['name']:
          total += meal['price']
  return total
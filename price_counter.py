from load_data import load_data

def price_counter(orders):

  all_meals = load_data("data/meals.json")
  meals = all_meals['meals']

  all_combos = load_data("data/combos.json")
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
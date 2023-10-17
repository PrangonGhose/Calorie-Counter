from load_data import load_data

def calorie_counter(orders):
  from combo_calories_counter import combo_calories_counter

  all_meals = load_data("data/meals.json")
  meals = all_meals['meals']

  all_combos = load_data("data/combos.json")
  combos = all_combos['combos']

  total = 0

  for order in orders:
    if 'combo' in order:
      for combo in combos:
        if order == combo['name']:
          total += combo_calories_counter(order)
    else:
      for meal in meals:
        if order == meal['name'] or order == meal['id']:
          total += meal['calories']
  return total
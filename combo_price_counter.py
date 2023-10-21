from load_data import load_data

def combo_price_counter(orders):
  from price_counter import price_counter
  all_combos = load_data("data/combos.json")
  combos = all_combos['combos']

  for combo in combos:
    if orders == combo['name']:
      combo_meal_list = combo['meals']

  total = price_counter(combo_meal_list)

  return total
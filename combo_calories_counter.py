from load_data import load_data

def combo_calories_counter(orders):
  from calorie_counter import calorie_counter
  all_combos = load_data("data/combos.json")
  combos = all_combos['combos']

  for combo in combos:
    if orders == combo['name']:
      combo_meal_list = combo['meals']

  total = calorie_counter(combo_meal_list)

  return total
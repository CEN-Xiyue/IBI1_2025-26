#	create	a	new	Python	class	called	‘food_item’
class food_item:
    def __init__(self,food,calories,protein,carbohydrate,fat):
        self.food = food
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

# calculate and report total calories, protein,	carbohydrate and fat
def cal_daily(total_food, student = 'Student'):
    calories_mass = 0.0
    protein_mass = 0.0
    carbohydrate_mass = 0.0
    fat_mass = 0.0
    for item in total_food:
        calories_mass += item.calories
        protein_mass += item.protein
        carbohydrate_mass += item.carbohydrate
        fat_mass += item.fat
    print(f"----The nutrient report of {student}----")
    print(f"The total calories consumed over 24h:{calories_mass}cal ")
    print(f"The total protein consumed over 24h:{protein_mass}g ")
    print(f"The total carbohydrate consumed over 24h:{carbohydrate_mass}g ")
    print(f"The total fat consumed over 24h:{fat_mass}g ")
# warning if cal>2500 or fat>90
    if calories_mass>2500 or fat_mass>90:
        print(f"Waring! Pay attention to your diet! Too unhealthy!! ")
    return calories_mass, protein_mass, carbohydrate_mass,fat_mass

#example
class food_item:
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    banana = food_item("Banana", 105, 1.3, 27, 0.4)
    ziweidumplings = food_item("ziweidumplings", 165, 31, 0, 66)
    pizza = food_item("Pizza", 285, 12, 36, 10)
    heytea = food_item("Heytea", 520, 30, 40, 30)

   
# 1
    daily_food_1 = [apple, banana, ziweidumplings]
    cal_daily(daily_food_1, student = "Student A" )

#2
    daily_food_2 = [ziweidumplings, heytea]
    cal_daily(daily_food_2, student = 'Student B')
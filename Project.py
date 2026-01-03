import os.path

def prompt_filename():
    """
    Prompt the user for text file name until a valid file name is provided.

    Returns:
       path to valid text file
    """
    while not os.path.isfile(filename := input('give path to data file: ')):
        print(f'data file {filename} does not exist')

    return filename

class Food:
    def __init__(food, name, status, cuisine_style, meal_type,calorie_level, flavour):
        food.name = name
        food.status = status
        food.cuisine_style = cuisine_style
        food.meal_type = meal_type
        food.calorie_level = calorie_level
        food.flavour = flavour
    def __str__(food):
        return f'{food.name} {food.status} {food.cuisine_style} {food.meal_type} {food.calorie_level} {food.flavour}'

def read_foods(filename):
    """
    Read foods from given text file.

    Args:
        filename: path to text file

    Returns:
        list of objects of type Food
    """
    foods = []
    with open(filename) as file:
        for line in file:
            words = line.split()
            status = words[-5]
            cuisine_style = words[-4]
            meal_type = words[-3]
            calorie_level = words[-2]
            flavour = words[-1]
            # name is everything from the first word to the collecting status ; these are joined into single string
            name = str.join(' ', words[-5:0:-1])
            foods.append(Food(name, status, cuisine_style, meal_type,calorie_level, flavour))

    return foods

def sort_collected_foods(foods):
    """
    Put collected foods into a list.

    Args:
        foods: list of objects of type Food

    Returns:
        list of collected foods
    """
    collected_foods = []
    for food in foods:
        if food.status == 'collected':
            collected_foods.append(food)

    return collected_foods

def count_all_the_foods(foods):
    """
    Count all the foods in the list.

    Args:
        foods: list of objects of type Food

    Returns:
        total number of foods
    """
    return len(foods)

def count_collected_foods(foods):
    """
    Count collected foods in the list.

    Args:
        foods: list of objects of type Food

    Returns:
        number of collected foods
    """
    count = 0
    for food in foods:
        if food.status == 'collected':
            count += 1

    return count

def sort_foods_by_meal_type(collected_foods):
    """
    Separate foods by meal type.

    Args:
        foods: list of objects of type Food

    Returns:
        three lists of foods: breakfast, lunch/dinner, dessert
    """
    breakfast = []
    lunch_dinner = []
    dessert = []

    for food in collected_foods:
        if food.meal_type == 'breakfast':
            breakfast.append(food)
        elif food.meal_type == 'lunch/dinner':
            lunch_dinner.append(food)
        elif food.meal_type == 'dessert':
            dessert.append(food)

    return breakfast, lunch_dinner, dessert

def analyze_most_common_cuisine_style(collected_foods):
    """
    Analyze favorite cuisine style from collected foods.

    Args:
        collected_foods: list of objects of type Food

    Returns:
        most frequent cuisine style among collected foods
    """
    American_count = 0
    Asian_count = 0
    European_count = 0
    for food in collected_foods:
        if food.cuisine_style == 'American':
            American_count += 1
        elif food.cuisine_style == 'Asian':
            Asian_count += 1
        elif food.cuisine_style == 'European':
            European_count += 1

    if American_count >= Asian_count and American_count >= European_count:
        return 'American'
    elif Asian_count >= European_count:
        return 'Asian'
    else:
        return 'European'
    
def analyze_most_common_calorie_level(collected_foods):
    """
    Analyze favorite calorie level from collected foods.

    Args:
        collected_foods: list of objects of type Food
    
    Returns:
        most frequent calorie level among collected foods
    """
    low_count = 0
    medium_count = 0
    high_count = 0
    for food in collected_foods:
        if food.calorie_level == 'low':
            low_count += 1
        elif food.calorie_level == 'medium':
            medium_count += 1
        elif food.calorie_level == 'high':
            high_count += 1

    if low_count >= medium_count and low_count >= high_count:
        return 'low'
    elif medium_count >= high_count:
        return 'medium'
    else:
        return 'high'

def analyze_most_common_flavour(collected_foods):
    """
    Analyze favorite flavour from collected foods.

    Args:
        collected_foods: list of objects of type Food

    Returns:
        most frequent flavour among collected foods
    """
    sweet_count = 0
    savory_count = 0
    umami_count = 0
    for food in collected_foods:
        if food.flavour == 'sweet':
            sweet_count += 1
        elif food.flavour == 'savory':
            savory_count += 1
        elif food.flavour == 'umami':
            umami_count += 1

    if sweet_count >= savory_count and sweet_count >= umami_count:
        return 'sweet'
    elif savory_count >= umami_count:
        return 'savory'
    else:
        return 'umami'
    
def print_analysis(foods):
    collected_foods = get_collected_foods(foods)
    print(f"Total number of foods: {count_all_the_foods(foods)}")
    print(f"Number of collected foods: {count_collected_foods(foods)}")
    breakfast, lunch_dinner, dessert = sort_foods_by_meal_type(collected_foods)
    print(f"Breakfast foods: {len(breakfast)}")
    print(f"Lunch/Dinner foods: {len(lunch_dinner)}")
    print(f"Dessert foods: {len(dessert)}")
    print(f"Favorite cuisine style: {analyze_most_common_cuisine_style(collected_foods)}")
    print(f"Favorite calorie level: {analyze_most_common_calorie_level(collected_foods)}")
    print(f"Favorite flavour: {analyze_most_common_flavour(collected_foods)}")

filename = prompt_filename()
foods = read_foods(filename)
print_analysis(foods)
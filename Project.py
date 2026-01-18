import os.path

def prompt_filename():
    """
    Prompt the user for text file name until a valid file name is provided.

    Returns:
       path to valid text file
    """
    while not os.path.isfile(filename := input('Give path to data file: ')):
        print(f'data file {filename} does not exist')

    return filename

class Food:
    """
    Class representing a food item.

    Returns: 
        food item with its attributes
    """
    def __init__(self, name, status, cuisine_style, meal_type, calorie_level, flavour):
        self.name = name
        self.status = status
        self.cuisine_style = cuisine_style
        self.meal_type = meal_type
        self.calorie_level = calorie_level
        self.flavour = flavour

    def __str__(self):
        return f'{self.name} {self.status} {self.cuisine_style} {self.meal_type} {self.calorie_level} {self.flavour}'

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
            line = line.strip()
            if not line:
                continue
            words = line.split()
            if len(words) < 6:
                continue
            name = words[0]
            status = words[1]
            cuisine_style = words[2]
            meal_type = words[3]
            calorie_level = words[4]
            flavour = words[5]
            foods.append(Food(name, status, cuisine_style, meal_type, calorie_level, flavour))

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
    collected_foods = sort_collected_foods(foods)

    return len(collected_foods)

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

    if not collected_foods:
        return 'N/A'

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

    if not collected_foods:
        return 'N/A'
    
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

     if not collected_foods:
        return 'N/A'
    
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
    
def print_breakfast(breakfast):
    """
    Print names of collected breakfast foods.

    Args:
        breakfast: list of breakfast food objects

    Returns:
        names of collected breakfast foods separated by commas
    """
    for food in breakfast:
        print(food.name, end='')
        if food.name != breakfast[-1].name:
            print(end=', ')

def print_lunch_dinner(lunch_dinner):
    """
    Print names of collected lunch/dinner foods.

    Args:
        lunch_dinner: list of lunch/dinner food objects

    Returns:
        names of collected lunch/dinner foods separated by commas
    """
    for food in lunch_dinner:
        print(food.name, end='')
        if food.name != lunch_dinner[-1].name:
            print(end=', ')

def print_dessert(dessert):
    """
    Print names of collected dessert foods.

    Args:
        dessert: list of dessert food objects

    Returns:
        names of collected dessert foods separated by commas
    """
    for food in dessert:
        print(food.name, end='')
        if food.name != dessert[-1].name:
            print(end=', ')

def print_analysis(foods):
    collected_foods = sort_collected_foods(foods)
    print(f"Total number of foods: {len(foods)}")
    print(f"Number of collected foods: {len(collected_foods)}")

    print("For the collected foods:",end='\n')

    breakfast, lunch_dinner, dessert = sort_foods_by_meal_type(collected_foods)
    print("Breakfast foods: ", end='')
    print_breakfast(breakfast)
    print()
    print("Lunch/Dinner foods: ", end='')
    print_lunch_dinner(lunch_dinner)
    print()
    print("Dessert foods: ", end='')
    print_dessert(dessert)
    print()

    print(f"Favorite cuisine style: {analyze_most_common_cuisine_style(collected_foods)}")
    print(f"Favorite calorie level: {analyze_most_common_calorie_level(collected_foods)}")
    print(f"Favorite flavour: {analyze_most_common_flavour(collected_foods)}")

filename = prompt_filename()
foods = read_foods(filename)
print_analysis(foods)

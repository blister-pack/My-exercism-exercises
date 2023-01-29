"""Functions for compiling dishes and ingredients for a catering company."""

#  sets don't keep duplicate entries, keep that in mind


from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)

import sets_categories_data


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """
    assistant_set = set(
        drink_ingredients
    )  #  a list isn't hashable, so I have to turn it into a set

    if assistant_set.isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"


print(
    check_drinks(
        "Amaretto Sour",
        [
            "almond liqueur",
            "bourbon",
            "cherries",
            "egg white",
            "lemon juice",
            "lemon twist",
            "simple syrup",
        ],
    )
)


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """

    # dicts work as key --> value
    diet_category = [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE]
    diet_category_names = ["VEGAN", "VEGETARIAN", "PALEO", "KETO", "OMNIVORE"]

    # apparently a set is immediatly unpacked when it's used and not its name
    for index, diets in enumerate(diet_category):
        if dish_ingredients.issubset(diets):
            return f"{str(dish_name)}: {diet_category_names[index]}"


print(
    categorize_dish(
        "Sticky Lemon Tofu",
        {
            "tofu",
            "soy sauce",
            "salt",
            "black pepper",
            "cornstarch",
            "vegetable oil",
            "garlic",
            "ginger",
            "water",
            "vegetable stock",
            "lemon juice",
            "lemon zest",
            "sugar",
        },
    )
)


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: tuple - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    (dish_name, dish_ingredients) = dish
    problem_ingredients = (set(dish_ingredients)).intersection(SPECIAL_INGREDIENTS)
    return (dish_name, problem_ingredients)


print(
    tag_special_ingredients(
        (
            "Ginger Glazed Tofu Cutlets",
            [
                "tofu",
                "soy sauce",
                "ginger",
                "corn starch",
                "garlic",
                "brown sugar",
                "sesame seeds",
                "lemon juice",
            ],
        )
    )
)


def compile_ingredients(dishes):
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    for ings in dishes:
        dishes[0] = dishes[0].union(ings)  #  the sets aren't joining
    return dishes[0]


#  don't forget to update this in exercism


print(
    compile_ingredients(
        dishes=[
            {
                "tofu",
                "soy sauce",
                "ginger",
                "corn starch",
                "garlic",
                "brown sugar",
                "sesame seeds",
                "lemon juice",
            },
            {
                "pork tenderloin",
                "arugula",
                "pears",
                "blue cheese",
                "pine nuts",
                "balsamic vinegar",
                "onions",
                "black pepper",
            },
            {
                "honeydew",
                "coconut water",
                "mint leaves",
                "lime juice",
                "salt",
                "english cucumber",
            },
        ]
    )
)


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    no_appis = set(dishes) - set(appetizers)
    return list(no_appis)


print(
    separate_appetizers(
        [
            "Avocado Deviled Eggs",
            "Flank Steak with Chimichurri and Asparagus",
            "Kingfish Lettuce Cups",
            "Grilled Flank Steak with Caesar Salad",
            "Vegetarian Khoresh Bademjan",
            "Avocado Deviled Eggs",
            "Barley Risotto",
            "Kingfish Lettuce Cups",
        ],
        [
            "Kingfish Lettuce Cups",
            "Avocado Deviled Eggs",
            "Satay Steak Skewers",
            "Dahi Puri with Black Chickpeas",
            "Avocado Deviled Eggs",
            "Asparagus Puffs",
            "Asparagus Puffs",
        ],
    )
)


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    #  this just turns the list of dishes into one big set of ingredients
    all_ings = set()
    for ings in dishes:
        all_ings = all_ings.union(ings)

    return all_ings.difference(intersection)


print(
    singleton_ingredients(
        sets_categories_data.example_dishes, sets_categories_data.EXAMPLE_INTERSECTION
    )
)

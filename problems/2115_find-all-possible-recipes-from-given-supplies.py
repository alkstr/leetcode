# 2115. Find All Possible Recipes from Given Supplies
#
# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The i_th recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
# Return a list of all the recipes that you can create. You may return the answer in any order.
# Note that two recipes may contain each other in their ingredients.

from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_to_i = {recipe: i for i, recipe in enumerate(recipes)}
        supplies_set = set(supplies)
        i_to_creatable = dict()
        visiting = set()

        def _check(i: int) -> bool:
            if i in visiting:
                return False
            if i in i_to_creatable:
                return i_to_creatable[i]

            visiting.add(i)
            for ingredient in ingredients[i]:
                if (ingredient in recipe_to_i and not _check(recipe_to_i[ingredient])) \
                        or (ingredient not in recipe_to_i and ingredient not in supplies_set):
                    visiting.remove(i)
                    i_to_creatable[i] = False
                    return False

            visiting.remove(i)
            i_to_creatable[i] = True
            return True

        result = []
        for i, recipe in enumerate(recipes):
            if _check(i):
                result.append(recipe)

        return result


assert Solution().findAllRecipes(
    ["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
    [
        ["d"],
        ["hveml", "f", "cpivl"],
        ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
        ["cpivl", "hveml", "zpmcz", "ju", "h"],
        ["h", "fzjnm", "e", "q", "x"],
        ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"],
        ["f", "hveml", "cpivl"]
    ],
    ["f", "hveml", "cpivl", "d"]
) == ["ju", "fzjnm", "q"]


assert Solution().findAllRecipes(
    ["bread"],
    [["yeast", "flour"]],
    ["yeast", "flour", "corn"]
) == ["bread"]

assert Solution().findAllRecipes(
    ["bread", "sandwich"],
    [["yeast", "flour"], ["bread", "meat"]],
    ["yeast", "flour", "meat"]
) == ["bread", "sandwich"]

assert Solution().findAllRecipes(
    ["bread", "sandwich", "burger"],
    [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
    ["yeast", "flour", "meat"]
) == ["bread", "sandwich", "burger"]

def buildCookBook():
    recipes = []
    recipes.append(["coffee", "coffee beans", "milk"])
    recipes.append(["peanut butter", "salt"])
    recipes.append(["honey", "honey"])
    recipes.append(["fries", "salt"])
    recipes.append(["yogurt", "pepper"])
    recipes.append(["apple", "apple"])
    recipes.append(["toast", "honey"])
    recipes.append(["eggs", "salt"])
    recipes.append(["ice cream", "milk"])
    #print("The recipes are: ",recipes)
    return recipes
def main():
    cookBook = buildCookBook()
    #ingredients = ["coffee beans", "milk", "peanuts", "honey", "sugar", "salt"]
    ingredients = []
    numIngredients = int(input("Enter how many ingredients you have: "))
    for i in range(numIngredients):
        ingredients.append(input("Enter ingredient: "))
    canMake = []
    #checks if all ingredients are in cookBook
    for index in range(len(cookBook)):
        temp = cookBook[index]
        temp2 = temp[1:]
        check = all(item in ingredients for item in temp2)
        if check:
            canMake.append(temp[0])
    print("You can make:",', '.join(canMake) )
main()

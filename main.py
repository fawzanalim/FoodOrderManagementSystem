def main():
    option = ""
    while option != "0": #sotto
        print("Welcome to SOFS\n")
        print("Which type of user are you: ")
        print("1. Login")
        print("2. Register")
        print("3. Browse Foods")
        print("0. Exit")
        
        option = input("Enter choice: ")
        if (option == "1"):
            login()
        elif (option == "2"):
            customerMenu(customerRegister())
        elif(option == "3"):
            guest()

def login():
    while True:
        print("\nPlease choose an option:\n")
        print("1. Customer Login")
        print("2. Admin Login")
        print("0. Go Back\n")
        option = input("Enter option: ")

        if option == "0":
            break

        if option == "1":
            email = input("Email: ")
            if email == "-1":
                break
            password = input("Password: ")

            try:
                file = open("customers.txt", "r")
                for line in file:
                    if line.strip().split("\t")[2] == email and line.strip().split("\t")[4] == password:
                        print("Welcome Back " + line.strip().split("\t")[1] + "!\n")
                        file.close()
                        customerMenu(line.strip().split("\t")[0])
                        return
                file.close()
                print("Login Failed. Try again or register.\n")
            except:
                print("Login failed. Try again or register.")
                

        elif option == "2":
            username = input("Username: ")
            if username == "-1":
                break
            password = input("Password: ")

            try:
                fileAdmin = open("admin.txt", "r")
                adminData = fileAdmin.readline().strip()
                fileAdmin.close()
                if (username == adminData.split("\t")[0] and password == adminData.split("\t")[1]):
                    print("Login successful admin!\n")
                    admin()
                    return

            except:
                if (username == "admin" and password == "1223334444"):
                    fileAdmin = open("admin.txt", "w")
                    
                    fileAdmin.write(username + "\t" + password)
                    fileAdmin.close()
                    print("Login successful admin!\n")
                    admin()
                    return

            print("Login failed. Try again")
        else:
            print("Invalid input. Try again\n")
         
def generateId(filename):
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        last_line = lines[-1]
        last_id = last_line.split('\t')[0]
        new_id = str(int(last_id) + 1).zfill(4)
    except FileNotFoundError:
        new_id = "0001"
    return new_id

def admin():
    
    while True:
        print("Admin Menu: ")
        print("\t1. Display Categories")
        print("\t2. Search Categories")
        print("\t3. Add Category")
        print("\t4. Edit Category")
        print("\t5. Delete Category")
        
        print("\t6. Display Foods")
        print("\t7. Search Foods")
        print("\t8. Add Food")
        print("\t9. Edit Food")
        print("\t10. Delete Food")
        
        print("\t11. Display Orders & Payments")
        print("\t12. Search Orders & Payments")

        print("\t13. Change Password")
        print("\t0. Logout\n")
        option = input("Choose an operation: ")
        print()
        
        if(option == "1"):
            displayCategories()
        elif(option == "2"):
            searchCategories()
        elif(option == "3"):
            addCategory()
        elif(option == "4"):
            editCategory()
        elif(option == "5"):
            deleteCatetgory()
        elif(option == "6"):
            displayFoods()
        elif(option == "7"):
            searchFoodsAdmin()
        elif(option == "8"):
            addFood()
        elif(option == "9"):
            editFood()
        elif(option == "10"):
            deleteFood()
        elif(option == "11"):
            displayOrders()
        elif(option == "12"):
            searchOrders()
        elif(option == "13"):
            changePassword()
        elif(option == "0"):
            return
        else:
            print("Invalid input. Try again.\n")

def displayCategories():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category.\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
    except:
        print("Error! There is no existing category.\n")
        return
    
def searchCategories():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category.\n")
            return

        searchKeyword = input("Enter a search keyword: ")
        matchingCategories = []
        for category in categories:
            if searchKeyword.lower() in category[1].lower():
                matchingCategories.append(category)
        
        if len(matchingCategories) == 0:
            print("No categories found")
            return
        
        
        print("\nCategory ID\tCategory Name")
        for category in matchingCategories:
            print(category[0] + "\t" + category[1], end="")
        print("\nTotal Categories Found:", len(matchingCategories))
        print()
        
    except:
        print("Error! There is no existing category.\n")
        return
       
def addCategory():
    catID = generateId("categories.txt")
    
    while True:
        catName = input("Category Name: ")
        if catName != "":
            break
    
    file = open("categories.txt", "a")
    file.write(catID + "\t" + catName + "\n")
    file.close()
    
    print("New category added successfully\n")

def editCategory():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category.\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        
        while True:
            print("Current Category Name: " + catName)
            newCatName = input("New Category Name: ")
            if newCatName == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        for category in categories:
            if catInput == category[0]:
                category[1] = newCatName
                break
        
        fileCat = open("categories.txt", "w")
        for category in categories:
            fileCat.write(category[0] + "\t" + category[1].strip() + "\n")
        fileCat.close()
        
        print("Category updated successfully\n")
    except:
        print("Error! There is no existing category.\n")
        return
    
    try:
        foods = []
        fileFood = open("foods.txt", "r")
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        
        fileFood = open("foods.txt", "w")
        
        for food in foods:
            if food[2] == catInput:
                food[3] = newCatName
            fileFood.write(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5].strip() + "\n")
        fileFood.close()
        
    except:
        return
    
def deleteCatetgory():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category.\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        
        confirmDelete = input("Are you sure you want to delete the category along with all the foods under it? [Y/N]: ")
        if confirmDelete.lower() not in ['yes', 'y', 'ya', 'yeah']:
            print("Deleting process cancelled\n")
            return
        fileCat = open("categories.txt", "w")
        for category in categories:
            if(category[0] != catInput and category[1].strip() != catName):
                fileCat.write(category[0] + "\t" + category[1].strip() + "\n")
        fileCat.close()
        
        
        print("Category successfully deleted\n")
    except:
        print("Error! There is no existing category.\n")
        return

    try:
        foods = []
        fileFood = open("foods.txt", "r")
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        
        fileFood = open("foods.txt", "w")
        
        for food in foods:
            if(food[2] != catInput and food[3].strip() != catName):
                fileFood.write(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5].strip() + "\n")
        fileFood.close()
    except:
        return

def displayFoods():
    print("1. Display all foods")
    print("2. Display Category-wise")
    option = input("Choose an option: ")
    
    if (option == "1"):
        try:
            fileFood = open("foods.txt", "r")
            foods = []
            for line in fileFood:
                foods.append(line.split("\t"))
            fileFood.close()
            if(len(foods) == 0):
                print("Error! There is no existing food.\n")
                return
            
            print("Food ID\tFood Name\tCategory ID\tCategory Name\tQty\tPrice")
            
            for food in foods:
                print(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5], end="")

        except:
            print("Error! There is no existing food.\n")
            return
    elif(option == "2"):
        try:
            fileCat = open("categories.txt", "r")
            categories = []
            for line in fileCat:
                categories.append(line.split("\t"))
            fileCat.close()
            if(len(categories) == 0):
                print("Error! There is no existing category.\n")
                return
            
            print("Category ID\tCategory Name")
            
            for category in categories:
                print(category[0] + "\t" + category[1], end="")
            
            print()
            while True:
                catInput = input("Choose a category ID: ")
                catName = ""
                for category in categories:
                    if catInput == category[0]:
                        catName = category[1]
                        break
                if(catName != ""):
                    break
                else:
                    print("Invalid input. Try again.\n")
            
        except:
            print("Error! There is no existing category.\n")
            return
        try:
            fileFood = open("foods.txt", "r")
            foods = []
            for line in fileFood:
                foods.append(line.split("\t"))
            fileFood.close()
            if(len(foods) == 0):
                print("Error! There is no existing food.\n")
                return
            
            print("Food ID\tFood Name\tCategory ID\tCategory Name\tQty\tPrice")
            
            for food in foods:
                if (food[2] == catInput and food[3].strip() == catName.strip()):
                    print(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5], end="")

        except:
            print("Error! There is no existing food.\n")
            return
    else:
        print("Invalid input\n")

def searchFoodsAdmin():
    try:
        fileFood = open("foods.txt", "r")
        foods = []
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        if(len(foods) == 0):
            print("Error! There is no existing food.\n")
            return

        search_keyword = input("Enter search keyword: ")
        search_results = []

        for food in foods:
            if search_keyword.lower() in food[1].lower():
                search_results.append(food)
        
        if len(search_results) == 0:
            print("No foods found with keyword", search_keyword)
        else:
            print("Food ID\tFood Name\tCategory ID\tCategory Name\tQty\tPrice")
            for result in search_results:
                print(result[0] + "\t" + result[1] + "\t" + result[2] + "\t" + result[3] + "\t" + result[4]+ "\t" + result[5], end="")
            print("\nTotal foods found:", len(search_results))
    except:
        print("Error! There is no existing food.\n")
        return

def addFood():
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Error! There is no existing category.\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")

        foodID = generateId("foods.txt")
            
        
        while True:
            foodName = input("Food Name: ")
            if foodName == "":
                print("Invalid input. Try again")
            else:
                break
        while True:
            try:
                foodQty = int(input("Food Quantity: "))
                if foodQty <= 0:
                    print("Invalid input. Try again")
                else:
                    break
            except:
                print("Invalid input. Try again")
        while True:
            try:
                foodPrice = float(input("Food Price: "))
                if foodPrice <= 0:
                    print("Invalid input. Try again")
                else:
                    break
            except:
                print("Invalid input. Try again")
        
        fileFood = open("foods.txt", "a")
        fileFood.write(foodID + "\t" + foodName + "\t" + catInput + "\t" + catName.strip() + "\t" + str(foodQty) + "\t" + str(foodPrice) +"\n")
        fileFood.close()
        
    except:
        print("Error! There is no existing category.\n")
        return
    
def editFood():
    try:
        fileFood = open("foods.txt", "r")
        foods = []
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        if(len(foods) == 0):
            print("Error! There is no existing food.\n")
            return
        
        print("Food ID\tFood Name\tCategory ID\tCategory Name\tQty\tPrice")
        
        for food in foods:
            print(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5], end="")
        
        print()
        while True:
            foodInput = input("Choose an food ID: ")
            foodName = ""
            for food in foods:
                if foodInput == food[0]:
                    foodName = food[1]
                    foodCat = food[2]
                    foodQty = food[4]
                    foodPrice = food[5]
                    break
            if(foodName != ""):
                break
            else:
                print("Invalid input. Try again.\n")

        while True:
            print("\nCurrent Food Name: ", foodName)
            newFoodName = input("New Food Name: ")
            if newFoodName == "":
                print("Invalid input. Try again.\n")
            else:
                break
            
        while True:
            print("\nCurrent Food Quantity: ", foodQty.strip())
            try:
                newFoodQty = int(input("New Food Quantity: "))
                if newFoodQty <= 0:
                    print("Invalid input. Try again")
                else:
                    newFoodQty = str(newFoodQty)
                    break
            except:
                print("Invalid input. Try again")
        
        while True:
            print("\nCurrent Food Price: ", foodPrice.strip())
            try:
                newFoodPrice = float(input("New Food Price: "))
                if newFoodPrice <= 0:
                    print("Invalid input. Try again")
                else:
                    newFoodPrice = str(newFoodPrice)
                    break
            except:
                print("Invalid input. Try again")
                
        print("\nCurrent Food Category: ", foodCat)
            
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()

        print("\nCategory ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            newFoodCat = input("Choose New category ID: ")

            newFoodCatName = ""
            for category in categories:
                if newFoodCat == category[0]:
                    newFoodCatName = category[1]
                    break
            if(newFoodCatName != ""):
                break
            else:
                print("Invalid input. Try again.\n")    

        for food in foods:
            if foodInput == food[0]:

                food[0] = foodInput

                food[1] = newFoodName

                food[2] = newFoodCat

                food[3] = newFoodCatName

                food[4] = newFoodQty
                
                food[5] = newFoodPrice
                
                break

        fileFood = open("foods.txt", "w")
        for food in foods:

            fileFood.write(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3].strip() + "\t" + food[4] + "\t" + food[5].strip() + "\n")

        fileFood.close()
        
        
    except:
        print("Error! There is no existing food.\n")
        return

def deleteFood():
    try:
        fileFood = open("foods.txt", "r")
        foods = []
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        if(len(foods) == 0):
            print("Error! There is no existing food.\n")
            return
        
        print("Food ID\tFood Name\tCategory ID\tCategory Name\tQty\tPrice")
        
        for food in foods:
            print(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3] + "\t" + food[4] + "\t" + food[5], end="")
        
        print()
        while True:
            foodInput = input("Choose an food ID: ")
            foodName = ""
            for food in foods:
                if foodInput == food[0]:
                    foodName = food[1]
                    break
            if(foodName != ""):
                break
            else:
                print("Invalid input. Try again.\n")

        confirmDelete = input("Are you sure you want to delete the food? [Y/N]: ")
        if confirmDelete.lower() not in ['yes', 'y', 'ya', 'yeah']:
            print("Deleting process cancelled\n")
            return
       
        fileFood = open("foods.txt", "w")

        for food in foods:
            if (food[0] != foodInput):
                fileFood.write(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3].strip() + "\t" + food[4].strip() + "\t" + food[5].strip() + "\n")

        fileFood.close()
        
        print("Food successfully deleted\n")
    except:
        print("Error! There is no existing food.\n")
        return

    
def displayOrders():
    print("Order ID\tCustomer ID\tStatus\tPayment Method\tAddress\tFood ID\tFood Name\tFoodQty\tFoodPrice\tTotal")
    try:
        fileOrders = open("orders.txt", "r")
        
        for line in fileOrders:
            line = line.strip().split("\t")
            
            for i in range(len(line)-1):
                print(line[i], end="\t")
            print(line[-1])
            
        
        fileOrders.close()
    except:
        print("There is no order in the system. Please wait for the customers to make an order.\n ")
        return
    
def searchOrders():
    try:
                
        fileOrder = open("orders.txt", "r")
        searchKey = input("Search Keyword: ")
        orders = []
        for line in fileOrder:
            orders.append(line.split("\t"))
        fileOrder.close()
        if(len(orders) == 0):
            print("Error! There is no existing order.\n")
            return
        
        print("Order ID\tCustomer ID\tStatus\tPayment Method\tAddress\tFood ID\tFood Name\tFoodQty\tFoodPrice\tTotal")
        
        for order in orders:
            for o in order:
                if searchKey.lower() in o.lower():
                    print(order[0] + "\t" + order[1] + "\t" + order[2] + "\t" + order[3] + "\t" + order[4] + "\t" + order[5] + "\t" + order[6] + "\t" + order[7] + "\t" + order[8] + "\t" + order[9], end="")
                    break

    except:
        print("Error! There is no existing food.\n")
        return  

def changePassword():
    fileAdmin = open("admin.txt", "r")
    
    username, currentPass = fileAdmin.readline().strip().split("\t")
    fileAdmin.close()
    
    while True:
        inputPass = input("Enter Current Password: ")
        if(currentPass == inputPass):
            break
    
    while True:
        newPass = input("Enter New Password: ").strip()
        if newPass != "":
            break
        else:
            print("Invalid input. Try again.\n")
    
    fileAdmin = open("admin.txt", "w")
    
    fileAdmin.write(username + "\t" + newPass)
    fileAdmin.close()

def guest():
    print("1. Browse through categories")
    print("2. Search food")
    option = input("Enter your choice: ")
    if(option == "1"):
        try:
            fileCat = open("categories.txt", "r")
            categories = []
            for line in fileCat:
                categories.append(line.split("\t"))
            fileCat.close()
            if(len(categories) == 0):
                print("Sorry! There is no existing category at the moment. We are working on it\n")
                return
            
            print("Category ID\tCategory Name")
            
            for category in categories:
                print(category[0] + "\t" + category[1], end="")
            
            print()
            while True:
                catInput = input("Choose a category ID: ")
                catName = ""
                for category in categories:
                    if catInput == category[0]:
                        catName = category[1]
                        break
                if(catName != ""):
                    break
                else:
                    print("Invalid input. Try again.\n")
            
            foods = []
            fileFood = open("foods.txt", "r")
            for line in fileFood:
                foods.append(line.split("\t"))
            fileFood.close()
            
            print("\nFood ID\tFoodName")
            for food in foods:
                
                if(food[2] == catInput and food[3].strip() == catName.strip()):
                    print(food[0] + "\t" + food[1])
            print("Please login as a customer to get more details about the foods. Thank you.\n")
        
            
        except:
            print("Sorry! There is no existing category at the moment. We are working on it\n")

            return
    elif(option == "2"):
        searchKey = input("Search Key: ")
        foods = []
        fileFood = open("foods.txt", "r")
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        
        print("\nFood ID\tFoodName")
        for food in foods:
            if searchKey.lower() in food[1].lower():
                print(food[0] + "\t" + food[1])
        print("Please login as a customer to get more details about the foods. Thank you.\n")
    else:
        print("Invalid input.\n")
   
def customerRegister():
    print("Welcome new user!")
    try:
        file = open("customers.txt", "r")
        for line in file:
            id = line.strip().split("\t")[0]
        id = int(id) + 1
        id = str(id).zfill(6)
    except:
        id = "000001"
    
    while True:
        name = input("Enter Name: ")
        if name == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        email = input("Enter Email: ")
        if email == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        phone = input("Enter Phone Number: ")
        if phone == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        password = input("Enter Password: ")
        if password == "":
            print("Invalid input. Try again.\n")
        else:
            break
    while True:
        address = input("Enter Address: ")
        if address == "":
            print("Invalid input. Try again.\n")
        else:
            break
        
    file = open("customers.txt", "a")
    file.write(id + "\t" + name + "\t" + email + "\t" + phone + "\t" + password + "\t" + address + "\n")
    file.close()
    return id

def customerMenu(customerID):
    if customerID == False:
        return
    while True:
        print("Customer Menu")
        print("1. Browse Foods")
        print("2. Search Food")
        print("3. Check Orders")
        print("0. Logout")
        
        option = input("Enter your choice: ")
        if (option == "1"):
            browseFoods(customerID)
        elif(option == "2"):
            searchFoods(customerID)
        elif(option == "3"):
            customerCheckOrders(customerID)
        elif(option == "0"):
            return
    
def browseFoods(customerID):
    try:
        fileCat = open("categories.txt", "r")
        categories = []
        for line in fileCat:
            categories.append(line.split("\t"))
        fileCat.close()
        if(len(categories) == 0):
            print("Sorry! There is no existing category at the moment. We are working on it\n")
            return
        
        print("Category ID\tCategory Name")
        
        for category in categories:
            print(category[0] + "\t" + category[1], end="")
        
        print()
        while True:
            catInput = input("Choose a category ID: ")
            catName = ""
            for category in categories:
                if catInput == category[0]:
                    catName = category[1]
                    break
            if(catName != ""):
                break
            else:
                print("Invalid input. Try again.\n")
        
        foods = []
        fileFood = open("foods.txt", "r")
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        
        print("\nFood ID\tFood Name\tQuantity\tPrice")
        for food in foods:
            
            if(food[2] == catInput and food[3].strip() == catName.strip()):
                print(food[0] + "\t" + food[1] + "\t" + food[4] + "\t" + food[5].strip())
        
        cartChoice = input("Anything of your interest? Want to add to cart? [Yes/No]: ")
        if(cartChoice.lower() not in ["yes", "y", "yeah", "yup", "ya"]):
            return
        while True:
            foodID = input("Enter Food ID: ")
            if (foodID == "-1"):
                return
            chosenFood = ""
            for food in foods:
                
                if food[0] == foodID:
                    
                    chosenFood = food
                    
                    break
            if chosenFood == "":
                print("Invalid input. Try again.")
                print("To go back, enter \'-1\'")
            else:
                break
        while True:
            try:
                foodQty = int(input("Enter Quantity: "))
                if foodQty > int(chosenFood[4]):
                    print("Not enough in stock.\n")
                    return
                elif foodQty < 0:
                    print("Invalid input. Try again.\n")
                else:
                    break
            except:
                print("Invalid input. Try again.\n")
        order(customerID, chosenFood, foodQty)
        
    except:
        print("Sorry! There is no existing category at the moment. We are working on it\n")

        return

def searchFoods(customerID):
    try:
        foods = []
        fileFood = open("foods.txt", "r")
        for line in fileFood:
            foods.append(line.split("\t"))
        fileFood.close()
        while True:
            searchKey = input("Search Key: ")
            if searchKey == "":
                print("Invalid input. Try again.\n")
            else:
                break
        
        print("\nFood ID\tFood Name\tQuantity\tPrice")
        for food in foods:
            for i in food[0:2]:
                if searchKey.lower() in i.lower():
                    print(food[0] + "\t" + food[1] + "\t" + food[4] + "\t" + food[5].strip())
                    break
        
        cartChoice = input("Anything of your interest? Want to add to cart? [Yes/No]: ")
        if(cartChoice.lower() not in ["yes", "y", "yeah", "yup", "ya"]):
            return
        while True:
            foodID = input("Enter Food ID: ")
            if (foodID == "-1"):
                return
            chosenFood = ""
            for food in foods:
                
                if food[0] == foodID:
                    
                    chosenFood = food
                    
                    break
            if chosenFood == "":
                print("Invalid input. Try again.")
                print("To go back, enter \'-1\'")
            else:
                break
        while True:
            try:
                foodQty = int(input("Enter Quantity: "))
                if foodQty > int(chosenFood[4]):
                    print("Not enough in stock.\n")
                elif foodQty < 0:
                    print("Invalid input. Try again.\n")
                else:
                    break
            except:
                print("Invalid input. Try again.\n")
        order(customerID, chosenFood, foodQty)
    except:
        print("We dont have any food at the moment. Please wait while we are updating our inventory. TQ\n")
        return

def order(customerID, food, qty):

    if qty == 0:
        return

    total = qty * int(food[5].strip())
    print("\nYour total is RM " + str(total))
    print("Pay by card")
    print("Cancel payment by entering \'-1\'")
    while True:
        cardNumber = input("Card Number: ")[-4:]
        if cardNumber == "-1":
            return
        if cardNumber == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    while True:
        cardExpiry = input("Expiry Date[MM/YY]: ")
        if cardExpiry == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    while True:
        cardCVV = input("CVV: ")
        if cardCVV == "":
            print("Invalid Input. Try again.\n")
        else:
            break
    
    
    fileFood = open("foods.txt", "r")
    foods = []
    for line in fileFood:
        foods.append(line.split("\t"))
    fileFood.close()
    
    
    for food in foods:
        if food[0] == food[0]:
            food[4] = str(int(food[4].strip()) - qty)
            break
        

    fileFood = open("foods.txt", "w")
    for food in foods:

        fileFood.write(food[0] + "\t" + food[1] + "\t" + food[2] + "\t" + food[3].strip() + "\t" + food[4] + "\t" + food[5].strip() + "\n")

    fileFood.close()
    
    try:
        file = open("orders.txt", "r")
        for line in file:
            orderID = line.strip().split("\t")[0]
        orderID = int(orderID) + 1
        orderID = str(orderID).zfill(6)
        file.close()
    except:
        orderID = "000001"
    
    fileCustomer = open("customers.txt", "r")
    for line in fileCustomer:
        if customerID == line.strip().split("\t")[0]:
            customerAdd = line.strip().split("\t")[5]
    fileCustomer.close()

    
    
    fileOrder = open("orders.txt", "a")
    fileOrder.write(orderID + "\t" + customerID + "\tPaid\tCard-" + cardNumber + "\t" + customerAdd + "\t" + food[0] + "\t" + food[1] + "\t" + str(qty) + "\t" + food[5].strip() + "\t" + str(total) + "\n")
    fileOrder.close()

def customerCheckOrders(customerID):
    
    print("Order ID\tStatus\tPayment Method\tAddress\tFood ID\tFood Name\tFoodQty\tFoodPrice\tTotal")
    try:
        fileOrders = open("orders.txt", "r")
        
        for line in fileOrders:
            line = line.strip().split("\t")
            print("")
            if(customerID == line[1]):
                print(line[0] + "\t" + line[2] + "\t" + line[3] + "\t" + line[4] + "\t" + line[5] + "\t" + line[6] + "\t" + line[7] + "\t" + line[8] + "\t" + line[9], end="")
        
        fileOrders.close()
    except:
        print("There is no order in the system.\n ")
        return


if __name__ == "__main__":
    main()
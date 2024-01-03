def interact_with_data():
    
    name = input("Enter your name: ")
    print("Hello, " + name + "!")

    age = int(input("Enter your age: "))
    next_year = age + 1
    print("Next year, you'll be", next_year,  "years_old.")

    favorite_fruits = input("Enter your favorite fruits separated by comas: ")
    fruits_list = favorite_fruits.split(',')
    print("You like the following fruits:", fruits_list)

if __name__ == "__main__":
    interact_with_data()
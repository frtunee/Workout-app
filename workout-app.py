#starting list of exercises
exercise_list = [
    {"name": "Skullcrushers", "weight": 25, "reps": 10, "sets": 3}
]

#adding new exercise
def get_valid_number(prompt, num_type):
    while True:
        try:
            user_input = input(prompt).replace(",", ".")
            value = num_type(user_input)

            if value >= 0:
                return value
            else:
                print("Numbers cannot be negative. Try again: ")
        except ValueError:
            print("That wasn't valid number.")
            
def create_exercise():
    name = input("Exercise name: ")
    weight = get_valid_number("Weight in kg: ", float)
    reps = get_valid_number("Number of reps: ", int)
    sets = get_valid_number("Number of sets: ", int)

    #creating a dictionary from the variables
    exercise_dict = {"name": name, "weight": weight, "reps": reps, "sets": sets}
    #sending the dictionary back to the function
    return exercise_dict

while True:
    print("1. View Exercises")
    print("2. Add Exercise")
    print("3. Exit")

    choice = input("Chose and option: ")
    if choice == "1": 
        print("Users exercises:") #printing the full list of exercises
        for exercise in exercise_list:
            print(exercise["name"], "-", exercise["weight"], "kg,", exercise["reps"], "reps,", exercise["sets"], "sets")
    elif choice == "2":
        print("Add new exercise: ") #adding new exercise/s if user types yes, appending new exercise in the exercise_list
        answer = "yes" #inicilize the loop if yes
        while answer == "yes": #keep looping if user types yes
            new_exercise = create_exercise()
            exercise_list.append(new_exercise)
            answer = input("Continue adding exercises? (yes/no):").lower()
    elif choice == "3":
        break
    else: 
        print("Invalid choice, please select 1, 2 or 3.")
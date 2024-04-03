#user_interface
def choosing_option():
    options = ["Performance Team","Mentors","Financial Dep","Mental Health Dep"]
    print("Hello there\nWelcome to WeThinkCode_")
    count = 0
    for option in options:
        count = count + 1
        print(f"{count}.{option}")
    while True:
        user_input = input("Select your option: ")
        # return user_input
        if user_input == "Performance Team":
            from Departments import performance_team
        elif user_input == "Mentors":
            from Departments import mentors
        elif user_input == "Financial Dep":
            from Departments import financial_dep
        elif user_input ==" Mental Health Dep":
            from Departments import mental_health_d
        else:
            print("Please enter a valid option")
            continue
        
choosing_option()
        
     
    


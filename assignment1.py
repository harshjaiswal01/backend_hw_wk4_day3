# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# # Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class

# Create a class BudgetCategory with private attributes for category name and allocated budget.
# Initialize these attributes in the constructor.
# Expected Outcome: A BudgetCategory class capable of storing category details securely.
# Task 2: Implement Getters and Setters

# Write getter and setter methods for both the category name and the allocated budget.
# Ensure that the setter methods include validation (e.g., budget should be a positive number).
# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.
# Task 3: Add Budget Functionality

# Add another attribute 'expense' to track how much you have spent towards a category
# Implement a method to add expenses.
# Validate the expense amount before adding it to the expense attribute.
# Expected Outcome: Ability to track expenses per category and update.
# Task 4: Display Budget Details

# Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses (budget - expenses).
# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
# Code Examples:

# class BudgetCategory:
#     # Constructor and private attributes
#     # ...

#     # Getters and setters for category name and budget
#     # ...

#     def add_expense(self, amount):
#         # Method to add an expense to the category
#         # ...

#     def display_category_summary(self):
#         # Method to display the budget category details
#         # ...

# # Example usage
# food_category = BudgetCategory("Food", 500)
# food_category.add_expense(100)
# food_category.display_category_summary()


class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = 0

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print("Budget should be a positive number.")

    def add_expense(self, amount):
        if amount > 0:
            check = self.__allocated_budget - self.__expense
            if amount <= check:
                self.__expense += amount
                print("Expense added successfully.")
            else:
                print("This amount is greater than available Budget.")
        else:
            print("Please enter a positive amount as expense!!!")

    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expense
        print("Category Name:", self.__category_name)
        print("Allocated Budget:", self.__allocated_budget)
        print("Expenses:", self.__expense)
        print("Remaining Budget:", remaining_budget)


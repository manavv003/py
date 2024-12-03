class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    def display(self):
        # This method shows the basic details of the person
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth}"
    
    def details(self):
        # This method can be overridden in the child class if needed
        return f"{self.name} is from {self.country} and was born on {self.date_of_birth}"

class Employee(Person):
    def __init__(self, name, country, date_of_birth, employee_id, position):
        # Call the parent class constructor using super()
        super().__init__(name, country, date_of_birth)
        self.employee_id = employee_id
        self.position = position
    
    def display(self):
        # Overriding the display method of the parent class
        person_details = super().display()  # Using the display method of the parent class
        return f"{person_details}, Employee ID: {self.employee_id}, Position: {self.position}"
    
    def details(self):
        # Overriding the details method to modify its behavior
        return f"{self.name}, with employee ID {self.employee_id}, holds the position of {self.position}."

# Example usage:
employee1 = Employee("Alice Smith", "USA", "1992-07-20", "E12345", "Software Engineer")

# Using the method from the parent class through the child class
print(employee1.display())  # Display person and employee details
print(employee1.details())  # Display overridden details
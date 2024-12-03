from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")  # Convert string to datetime

    def get_age(self):
        today = datetime.today()  # Get today's date
        age = today.year - self.date_of_birth.year  # Calculate age
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1  # Adjust age if birthday hasn't occurred yet this year
        return age

# Example usage:
person1 = Person("John Doe", "USA", "1990-05-15")
print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Age: {person1.get_age()} years")

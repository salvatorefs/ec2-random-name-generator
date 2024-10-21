import random
import string

# List of allowed departments
ALLOWED_DEPARTMENTS = ["Marketing", "Accounting", "FinOps"]

def generate_random_name(department, instance_count):
    unique_names = []
    for _ in range(instance_count):
        # Generate random letters and numbers (you can customize the length)
        random_letters = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # Create unique name format
        name = f"{department}_{random_letters}"
        unique_names.append(name)
    return unique_names

def ec2_name_generator():
    # Ask for user input
    department = input("Enter your department (Marketing, Accounting, FinOps): ").capitalize()
    
    # Validate department
    if department not in ALLOWED_DEPARTMENTS:
        print(f"Department '{department}' is not allowed to use this name generator.")
        return
    
    try:
        instance_count = int(input("How many EC2 instances do you need names for? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Generate the names
    ec2_names = generate_random_name(department, instance_count)
    
    # Output the results
    print("Generated EC2 Names:")
    for name in ec2_names:
        print(name)

# Execute the function
if __name__ == "__main__":
    ec2_name_generator()

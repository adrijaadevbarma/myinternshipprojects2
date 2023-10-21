import string
import secrets

def generate_password(length=12):
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+=-[]{}|;:,.<>?"
    
    all_chars = upper_chars + lower_chars + digits + special_chars
    
    if length < 8:
        length = 8
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid numbers for the number of passwords and length.")
        else:
            passwords = generate_multiple_passwords(num_passwords, password_length)
            
            print("\nSecure Generated passwords are:")
            for i, password in enumerate(passwords, start=1):
                print(f"Password {i}: {password}")
    
    except ValueError:
        print("Please enter valid numbers for the number of passwords and length!")
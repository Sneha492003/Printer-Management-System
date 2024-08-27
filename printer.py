# Imports
import mysql.connector

# Database Connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sneha",
        database="printer"
    )

# Add User
def add_user(user_id, department):
    connection = connect_to_database()
    cursor = connection.cursor()
    
    try:
        # Insert user ID and department into the database
        cursor.execute("INSERT INTO users (user_id, department) VALUES (%s, %s)", (user_id, department))
        connection.commit()
        print(f"User {user_id} from {department} department added to the system.")
    except mysql.connector.IntegrityError:
        print(f"User {user_id} already exists.")
    
    cursor.close()
    connection.close()

#Record Prints
def record_print(user_id,pages):
    connection=connect_to_database()
    cursor=connection.cursor()
    cursor.execute("SELECT print_count FROM users WHERE user_id = %s",(user_id,))
    result=cursor.fetchone()
    if result:
        new_print_count=result[0]+pages
        cursor.execute("UPDATE users SET print_count = %s WHERE user_id = %s",(new_print_count,user_id))
        connection.commit()
        print(f"{pages} pages printed by user {user_id}. Total prints: {new_print_count}")
    cursor.close()
    connection.close()

# Show User Print Summary
def user_print_summary(user_id):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT print_count FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        print(f"User {user_id} has printed {result[0]} pages.")
    cursor.close()
    connection.close()

# Display All Users
def display_all_users():
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, department, print_count FROM users")
    results = cursor.fetchall()
    
    if results:
        print("\n--- Printer Usage Summary ---")
        for user_id, department, print_count in results:
            print(f"User ID: {user_id} | Department: {department} | Total Pages Printed: {print_count}")
    else:
        print("No users in the system.")
    
    cursor.close()
    connection.close()


# Main Menu Loop
while True:
    print("\n--- Printer Management System ---")
    print("1. Add User")
    print("2. Record Print Job")
    print("3. Show User Print Summary")
    print("4. Show All Users")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        user_id = input("Enter User ID to add: ")
        department = input("Enter User's Department: ")
        add_user(user_id, department)   
    
    elif choice == '2':
        user_id = input("Enter User ID: ")
        pages = int(input("Enter number of pages to print: "))
        record_print(user_id, pages)
    
    elif choice == '3':
        user_id = input("Enter User ID: ")
        user_print_summary(user_id)
    
    elif choice == '4':
        display_all_users()
    
    elif choice == '5':
        print("Exiting the Printer Management System. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please select a valid option.")






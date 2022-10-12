import sqlite3
from Student import Student

# Connect to local database.
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create the new table students.
# c.execute("""CREATE TABLE students (
#             first text,
#             last text,
#             id integer,
#             gpa float
#             )""")

# Put new student into database "students".
def insert_student(student):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :id, :gpa)", {'first': student.first, 'last': student.last, 'id': student.id, 'gpa': student.gpa})

# Get student by last name.
def get_student_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last=:last", {'last': lastname})
    # Fetch it from the "students" table.
    return c.fetchall()

# Update gpa of student by calling the UPDATE method then seting the new gpa = to the old gpa.
def update_gpa(student, id, gpa):
    with conn:
        c.execute("""UPDATE students SET gpa = :gpa
                    WHERE first = :first AND last = :last And id = :id""",
                  {'first': student.first, 'last': student.last, 'id': id, 'gpa': gpa})

#Remove student by calling the DELETE method.
def remove_student(student):
    with conn:
        c.execute("DELETE from students WHERE first = :first AND last = :last",
                  {'first': student.first, 'last': student.last})

# Functions for user output/input.

# Get input, set input = to student then call the update_gpa function. Print new gpa.
def update_student_gpa():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    id = int(input("id: "))
    gpa = float(input("gpa: "))
    student = Student(first_name, last_name, id, gpa)
    input_gpa = float(input(f"Update the gpa of {first_name} {last_name} to: "))

    update_gpa(student, id, input_gpa)

    print("----------------------------")
    print(f"The gpa for {first_name} {last_name} has been updated to {input_gpa}.")

# Get last name input, call the get_student_by_name function then pass in last_name. Print info.
def look_up_student():
    last_name = input("Inter last name: ")

    student = get_student_by_name(last_name)

    print("----------------------------")
    print(student)

# Get each input, call the insert_student function, then print results.
def add_new_student():
    first_name = input("What is the first name: ")
    last_name = input("What is the last name: ")
    id = int(input("id: "))
    gpa = float(input("gpa: "))
    student = Student(first_name, last_name, id, gpa)

    insert_student(student)

    print("----------------------------")
    print(f"{first_name} {last_name} has been added")

# Get each input, call the delete_student function, then print results.
def delete_student():
    first_name = input("What is the first name: ")
    last_name = input("What is the last name: ")
    id = int(input("id: "))
    gpa = float(input("gpa: "))
    student = Student(first_name, last_name, id, gpa)

    remove_student(student)

    print("----------------------------")
    print(f"{first_name} {last_name} has been removed")
    
# Display the board
def display_board():

    print("\n")
    print("Student database")
    print("----------------------------")
    print("\n")
    print("select one of the following ")
    print("1: Look up student ")
    print("2: Update gpa ")
    print("3: Add new student ")
    print("4: Delete student ")
    print("5: Quit ")

# Set each function in an if statement, and calls that function based on user input.
def main():
    keep_going = True

    while keep_going:

        display_board()
        choice = int(input(": "))

        if choice == 1:
            look_up_student()

        if choice == 2: 
            update_student_gpa()

        if choice == 3:
            add_new_student()

        if choice == 4:
            delete_student()
            
        if choice == 5:
            keep_going = False
            
    conn.close()

if __name__=="__main__":
    main()
# ==========================================
# STUDENT RECORD MANAGER
# Dynamic Array ADT
# ==========================================


# ------------------------------------------
# STUDENT CLASS
# ------------------------------------------

# This class represents one student record.
class Student:

    # This method is called when creating a new Student object.
    def __init__(self, student_id, student_name, course, year_level):

        # Store the student's ID.
        self.student_id = student_id

        # Store the student's name.
        self.student_name = student_name

        # Store the student's course.
        self.course = course

        # Store the student's year level.
        self.year_level = year_level

    # This method displays the student's information.
    def display(self):

        # Display the Student ID.
        print("Student ID :", self.student_id)

        # Display the Student Name.
        print("Name       :", self.student_name)

        # Display the Course.
        print("Course     :", self.course)

        # Display the Year Level.
        print("Year Level :", self.year_level)

        # Print a line to separate student records.
        print("------------------------------")


# ------------------------------------------
# DYNAMIC ARRAY CLASS / ADT
# ------------------------------------------

# This class creates our own Dynamic Array ADT.
class DynamicArray:

    # This method runs when we create a DynamicArray object.
    def __init__(self):

        # Set the starting capacity to 5.
        self.capacity = 5

        # The array currently contains 0 students.
        self.size = 0

        # Create an array with 5 empty spaces.
        # None means that the position is currently empty.
        self.array = [None] * self.capacity


    # --------------------------------------
    # RESIZE METHOD
    # --------------------------------------

    # This method increases the capacity of the array.
    def resize(self):

        # Double the current capacity.
        # Example: 5 becomes 10.
        new_capacity = self.capacity * 2

        # Create a new array using the new capacity.
        new_array = [None] * new_capacity

        # Copy all existing students to the new array.
        for i in range(self.size):

            # Copy the student from the old array.
            new_array[i] = self.array[i]

        # Replace the old array with the new array.
        self.array = new_array

        # Update the capacity.
        self.capacity = new_capacity

        # Inform the user that the array was full.
        print("Array is full.")

        # Display the new capacity.
        print("Capacity increased to", self.capacity)


    # --------------------------------------
    # ADD METHOD
    # --------------------------------------

    # This method adds a student to the array.
    def add(self, student):

        # Check if the array is already full.
        if self.size == self.capacity:

            # If full, increase the array capacity.
            self.resize()

        # Put the new student in the next available position.
        self.array[self.size] = student

        # Increase the number of students by 1.
        self.size += 1


    # --------------------------------------
    # GET METHOD
    # --------------------------------------

    # This method gets a student using its index.
    def get(self, index):

        # Check if the index is invalid.
        if index < 0 or index >= self.size:

            # Return None if the index does not exist.
            return None

        # Return the student at the specified index.
        return self.array[index]


    # --------------------------------------
    # SET METHOD
    # --------------------------------------

    # This method replaces a student at a specific index.
    def set(self, index, student):

        # Check if the index is valid.
        if index >= 0 and index < self.size:

            # Replace the old student with the new student.
            self.array[index] = student


    # --------------------------------------
    # SEARCH METHOD
    # --------------------------------------

    # This method searches for a student using Student ID.
    def search(self, student_id):

        # Go through every student in the array.
        for i in range(self.size):

            # Compare the current student's ID
            # with the ID entered by the user.
            if self.array[i].student_id == student_id:

                # Return the position/index of the student.
                return i

        # Return -1 if the student was not found.
        return -1


    # --------------------------------------
    # REMOVE METHOD
    # --------------------------------------

    # This method removes a student using Student ID.
    def remove(self, student_id):

        # Search for the student's position.
        index = self.search(student_id)

        # Check if the student was not found.
        if index == -1:

            # Return False to indicate removal failed.
            return False

        # Shift all students after the removed student
        # one position to the left.
        for i in range(index, self.size - 1):

            # Move the next student into the current position.
            self.array[i] = self.array[i + 1]

        # Clear the last position.
        self.array[self.size - 1] = None

        # Decrease the number of students by 1.
        self.size -= 1

        # Return True to indicate successful removal.
        return True


    # --------------------------------------
    # SIZE METHOD
    # --------------------------------------

    # This method returns the current number of students.
    def get_size(self):

        # Return the size of the array.
        return self.size


    # --------------------------------------
    # DISPLAY METHOD
    # --------------------------------------

    # This method displays all student records.
    def display(self):

        # Check if there are no students.
        if self.size == 0:

            # Tell the user that there are no records.
            print("No student records found.")

            # Stop the method.
            return

        # Display a heading.
        print("\n========== STUDENT RECORDS ==========")

        # Loop through all existing students.
        for i in range(self.size):

            # Display the student number.
            print("Student #", i + 1)

            # Display the student's complete information.
            self.array[i].display()


# ==========================================
# CREATE DYNAMIC ARRAY
# ==========================================

# Create one DynamicArray object.
# This automatically starts with a capacity of 5.
students = DynamicArray()


# ==========================================
# ADD STUDENT FUNCTION
# ==========================================

# This function asks the user for student information.
def add_student():

    # Display the Add Student heading.
    print("\n========== ADD STUDENT ==========")

    # Ask the user for the Student ID.
    student_id = input("Student ID: ")

    # Search to see if the Student ID already exists.
    if students.search(student_id) != -1:

        # Tell the user that the ID already exists.
        print("Student ID already exists!")

        # Stop the function.
        return

    # Ask for the student's name.
    student_name = input("Student Name: ")

    # Ask for the student's course.
    course = input("Course: ")

    # Ask for the student's year level.
    # int() converts the input from text to an integer.
    year_level = int(input("Year Level: "))

    # Create a new Student object.
    student = Student(
        student_id,
        student_name,
        course,
        year_level
    )

    # Add the new student to our Dynamic Array.
    students.add(student)

    # Tell the user that the student was added.
    print("Student added successfully!")


# ==========================================
# SEARCH STUDENT FUNCTION
# ==========================================

# This function searches for a student.
def search_student():

    # Display the Search Student heading.
    print("\n========== SEARCH STUDENT ==========")

    # Ask the user for the Student ID.
    student_id = input("Enter Student ID: ")

    # Search for the Student ID.
    index = students.search(student_id)

    # Check if the student was found.
    if index != -1:

        # Display a success message.
        print("\nStudent found!")

        # Get and display the student's information.
        students.get(index).display()

    else:

        # Tell the user that the student does not exist.
        print("Student not found.")


# ==========================================
# UPDATE STUDENT FUNCTION
# ==========================================

# This function updates an existing student's information.
def update_student():

    # Display the Update Student heading.
    print("\n========== UPDATE STUDENT ==========")

    # Ask for the Student ID.
    student_id = input("Enter Student ID: ")

    # Search for the student.
    index = students.search(student_id)

    # Check if the student does not exist.
    if index == -1:

        # Display an error message.
        print("Student not found.")

        # Stop the function.
        return

    # Get the student using the index.
    student = students.get(index)

    # Display the current information.
    print("\nCurrent Information:")

    # Call the display method of the Student class.
    student.display()

    # Ask for the new student name.
    student_name = input("New Student Name: ")

    # Ask for the new course.
    course = input("New Course: ")

    # Ask for the new year level.
    year_level = int(input("New Year Level: "))

    # Update the student's name.
    student.student_name = student_name

    # Update the student's course.
    student.course = course

    # Update the student's year level.
    student.year_level = year_level

    # Display a success message.
    print("Student updated successfully!")


# ==========================================
# REMOVE STUDENT FUNCTION
# ==========================================

# This function removes a student.
def remove_student():

    # Display the Remove Student heading.
    print("\n========== REMOVE STUDENT ==========")

    # Ask for the Student ID.
    student_id = input("Enter Student ID: ")

    # Try to remove the student.
    result = students.remove(student_id)

    # Check if the removal was successful.
    if result:

        # Display a success message.
        print("Student removed successfully!")

    else:

        # Display an error message.
        print("Student not found.")


# ==========================================
# DISPLAY ARRAY INFORMATION
# ==========================================

# This function displays the size and capacity.
def display_array_information():

    # Display the heading.
    print("\n========== ARRAY INFORMATION ==========")

    # Display the current number of students.
    print("Current Number of Students:", students.get_size())

    # Display the current capacity.
    print("Current Array Capacity    :", students.capacity)


# ==========================================
# MAIN PROGRAM / MENU
# ==========================================

# Start an infinite loop so the menu keeps appearing.
while True:

    # Display the main menu.
    print("\n================================")
    print("     STUDENT RECORD MANAGER")
    print("================================")

    # Menu option 1.
    print("1. Add Student")

    # Menu option 2.
    print("2. Display Students")

    # Menu option 3.
    print("3. Search Student")

    # Menu option 4.
    print("4. Update Student")

    # Menu option 5.
    print("5. Remove Student")

    # Menu option 6.
    print("6. Display Array Information")

    # Menu option 7.
    print("7. Exit")

    # Display a line.
    print("================================")

    # Ask the user to select an option.
    choice = input("Enter your choice: ")


    # --------------------------------------
    # OPTION 1
    # --------------------------------------

    # If the user chooses 1...
    if choice == "1":

        # Call the add student function.
        add_student()


    # --------------------------------------
    # OPTION 2
    # --------------------------------------

    # If the user chooses 2...
    elif choice == "2":

        # Display all students.
        students.display()


    # --------------------------------------
    # OPTION 3
    # --------------------------------------

    # If the user chooses 3...
    elif choice == "3":

        # Search for a student.
        search_student()


    # --------------------------------------
    # OPTION 4
    # --------------------------------------

    # If the user chooses 4...
    elif choice == "4":

        # Update a student.
        update_student()


    # --------------------------------------
    # OPTION 5
    # --------------------------------------

    # If the user chooses 5...
    elif choice == "5":

        # Remove a student.
        remove_student()


    # --------------------------------------
    # OPTION 6
    # --------------------------------------

    # If the user chooses 6...
    elif choice == "6":

        # Display array information.
        display_array_information()


    # --------------------------------------
    # OPTION 7
    # --------------------------------------

    # If the user chooses 7...
    elif choice == "7":

        # Display exit message.
        print("Thank you for using Student Record Manager!")

        # Break stops the while loop.
        break


    # --------------------------------------
    # INVALID CHOICE
    # --------------------------------------

    # If the user enters something other than 1-7...
    else:

        # Display an error message.
        print("Invalid choice. Please try again.")
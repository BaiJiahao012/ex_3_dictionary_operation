student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}

# First, display the complete record using for loop, printing and some string formatting only
for key, value in student.items():
    print(f"{key}: {value}")

# Check if there's a key called 'email'. If not, ask the user to enter an email
if "email" not in student:
    new_email = input("Please enter an email: ").strip()
    student["email"] = new_email

# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
while True:
    new_city = input("Please enter a new city: ").strip()
    if new_city:
        student["city"] = new_city
        break
    else:
        print("Error: City cannot be empty, please try again.")

# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
phone_value = student.get("phone")
if phone_value is None:
    print("Phone number not found.")

# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
student["contact"] = {
    "phone": student.get("phone"),
    "email": student["email"]
}

# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead.
course_scores = student["courses"].values()
total = 0
count = 0
for score in course_scores:
    total = total + score
    count = count + 1
average_score = total / count

# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score.
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
if average_score >= 90:
    student["academic_status"] = "Excellent"
elif average_score >= 75:
    student["academic_status"] = "Good"
elif average_score >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

# Add the logic to search for a course.
# If the course is found, print the course name and score. If not, print "Course not found".
search_course = input("Enter course name to search: ").strip()
if search_course in student["courses"]:
    print(f"{search_course}: {student['courses'][search_course]}")
else:
    print("Course not found")

# Add the logic to update a course score.
# Ask the user to enter the course name and the new score.
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
# Recaclculate the average score and update the academic status after the course score has been updated.
update_course_name = input("Enter course name to update score: ").strip()
if update_course_name in student["courses"]:
    new_score_input = input("Enter new score: ").strip()
    if new_score_input.isdigit():
        updated_score = int(new_score_input)
        if 0 <= updated_score <= 100:
            old_score = student["courses"][update_course_name]
            student["courses"][update_course_name] = updated_score
            print(f"Score for {update_course_name} changed from {old_score} to {updated_score}")

            # Recaclculate the average score and update the academic status after the course score has been updated.
            new_total = 0
            new_count = 0
            for s in student["courses"].values():
                new_total = new_total + s
                new_count = new_count + 1
            average_score = new_total / new_count

            # Add a new key called 'academic_status' to the dictionary
            # It should be a string that indicates the student's academic status based on the average score.
            # If the score is >= 90, the status should be "Excellent".
            # If the score is >= 75, the status should be "Good".
            # If the score is >= 60, the status should be "Pass".
            # If the score is < 60, the status should be "At Risk".
            if average_score >= 90:
                student["academic_status"] = "Excellent"
            elif average_score >= 75:
                student["academic_status"] = "Good"
            elif average_score >= 60:
                student["academic_status"] = "Pass"
            else:
                student["academic_status"] = "At Risk"
        else:
            print("Error: Score must be between 0 and 100, update aborted.")
    else:
        print("Error: Score must be a number, update aborted.")
else:
    print("Course not found, cannot update score.")

# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following sample format.
print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")
print("CONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")
print("COURSE RESULTS")
for course_name, course_score in student["courses"].items():
    print(f"{course_name}: {course_score}")
print(f"Average Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("=====================================")

# STEP1- CREATE A LIST OF CLASAMATES
classmates = ["ARAV","SNEHA","PRYA","RAHUL","DEV"]
print("class list: ", classmates)

# STEP2- ACCESS THE LIST
print("TOTAL STUDENTS:", len(classmates))
print("FIRST STUDENT: ", classmates[0])
print("LAST STUDENT: ", classmates[-1])
print("FIRST THREE: ", classmates[:3])

# STEP3- MODIFY THE LIST
classmates.append("MEERA")
print("\nAFTER ADDING MEERA: ", classmates)
classmates.remove("DEV")
print("AFTER REMOVING DEV: ", classmates)
classmates.sort()
print("SORTED ALPHABATICALLY: ", classmates)
classmates.reverse()
print("REVERSED: ", classmates)

# STEP4- CREATE A TEACHER'S DICTIONARY
teacher= {"name":"MR. SHARMA", "subject":"PYTON", "experience":"5"}
print("\nTEACHER PROFILE: ", teacher)

# STEP-5 DICTIONARY OPERATIONS
print ("SUBJECT: ", teacher["subject"])
print("EXPERIENCE: ", teacher.get("experience", "NOT FOUND"))
teacher["experience"]=6
teacher["email"]= "sharma@school.com"
teacher.pop("experience")
print("UPDATED TEACHER PROFILE: ", teacher)

# STEP6- CONVERT LIST TO A STUDENT DIRECTORY
roll_numbers=[1,2,3,4,5]
names = ["ARAV","SNEHA","PRYA","RAHUL","DEV"]
student_directory= dict(zip(roll_numbers, names))
print("\nSTUDENT DIRECTORY:", student_directory)
print("STUDENT AT ROLL3:", student_directory[3])

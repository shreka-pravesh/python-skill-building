# Program to manage student course registration using sets

registered_students = {"Leena", "Tarak", "", "Gokul", "Shideek"}
new_registrations = {"Jeelani", "Shrekaa", "Nive", "Sibi"}
print(" Students already registered:", registered_students)
print(" New students trying to register:", new_registrations)
duplicates = registered_students.intersection(new_registrations)
if duplicates:
    print("\n Duplicate registrations found:", duplicates)
registered_students.update(new_registrations)
print("\n Updated Registered Students List:")
for student in sorted(registered_students):
    print("-", student)
print("\n Total Students Registered:", len(registered_students))

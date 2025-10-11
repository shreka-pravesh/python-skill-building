# Program to match employee skills with job requirements

required_skills = {"python", "sql", "git", "communication"}
employee_1 = {"python", "git", "html"}
employee_2 = {"python", "sql", "git", "communication"}
employee_3 = {"c", "c++", "python"}
employees = {
    "Shreka": employee_1,
    "Jeelani": employee_2,
    "Varun": employee_3
}
for name, skills in employees.items():
    matched = skills.intersection(required_skills)
    missing = required_skills.difference(skills)
    print(f"\n {name}'s Skill Report:")
    print(" Matched Skills:", matched)
    print(" Skills to Improve:", missing)

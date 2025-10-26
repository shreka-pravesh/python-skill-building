import datetime
def generate_report():
    data = {
        "completed_tasks": 12,
        "pending_tasks": 4,
        "issues_found": 1,
        "team_members": 5
    }
    report = (
        f" Report Date: {datetime.date.today()}\n"
        f" Completed Tasks: {data['completed_tasks']}\n"
        f" Pending Tasks: {data['pending_tasks']}\n"
        f" Issues Found: {data['issues_found']}\n"
        f" Team Members: {data['team_members']}\n"
    )
    with open("daily_report.txt", "w") as f:
        f.write(report)
    print(" Daily report created successfully: daily_report.txt")
def simulate_email_send():
    print(" Simulating email send...")
    print("Email sent successfully to: manager@company.com")
def main():
    generate_report()
    simulate_email_send()
if __name__ == "__main__":
    main()

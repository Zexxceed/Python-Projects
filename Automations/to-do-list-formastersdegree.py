# Simple To-Do List for Scholarship Applications

#National Taiwan University (AI or Data Science)
ntu_tasks = [
    "Complete NTU online application form",
    "Obtain and fill out Taiwan Scholarship application form",
    "Make a copy of your valid passport",
    "Gather academic degree and transcripts",
    "Prepare English/Chinese language proficiency proof",
    "Write a detailed study plan",
    "Obtain two letters of recommendation",
    "Check health check-up requirements",
    "Submit all documents before the deadline"
]

# Kun Shan University (Mechatronics Automation and Program Management)
icdf_tasks = [
    "Complete Taiwan ICDF online application form",
    "Submit KSU application for Mechatronics Automation",
    "Make a copy of your valid passport",
    "Gather academic degree and transcripts",
    "Prepare English/Chinese language proficiency proof",
    "Write a detailed study plan",
    "Obtain two letters of recommendation",
    "Check health check-up requirements",
    "Submit all documents before the deadline"
]

# Function to display the to-do list
def display_todo_list(tasks, scholarship_name):
    print(f"\nTo-Do List for {scholarship_name}:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Display the to-do lists
display_todo_list(ntu_tasks, "NTU Taiwan Scholarship")
display_todo_list(icdf_tasks, "Taiwan ICDF Scholarship (KSU)")

# Add your additional tasks or mark tasks as completed as you progress!

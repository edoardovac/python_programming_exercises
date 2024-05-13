team_members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer"
}

given_name = input("Enter name (quit ends): ")

while (given_name != "quit"):
    given_role = input("Enter role: ")
    team_members[given_name] = given_role
    print()
    given_name = input("Enter name (quit ends): ")

print()

for key, value in sorted(team_members.items()):
    print(f"{key:7s} {value}")
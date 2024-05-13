team_members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer"
}

given_text = input("Enter name (quit ends): ")

while (given_text != "quit"):
    if (given_text not in team_members.keys()):
        print(f"{given_text} is not in the team")
    else:
        print(f"{given_text} is a {team_members[given_text]}")
    print()
    given_text = input("Enter name (quit ends): ")
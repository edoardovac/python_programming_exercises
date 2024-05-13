team_members = {
    "John": "software developer",
    "Ann": "project manager",
    "Susan": "software developer",
    "Jill": "lead developer"
}

print(*sorted(set(team_members.values())), sep= "\n")
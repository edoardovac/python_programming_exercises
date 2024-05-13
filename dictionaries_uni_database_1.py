def insert_degree_program(db: dict, degree_program: str):
    if degree_program in db.keys():
        print("is already in the database")
    else:
        db[degree_program] = []

def insert_course(db: dict, degree: str, course: tuple):
    if degree not in db:
        print(f"Unknown degree program: {degree}")
    else:
        if course in db[degree]:
            print(f"{course[0]} is already in the database")
        else:
            db[degree].append(course)

def print_degree_program(db, degree):
    print(f"{degree} ({len(db)} courses)")
    total = 0
    for course, credits in db[degree]:
        print(f"  {course}, {credits} credits")
        total += credits
    print(f"  Total credits: {total}")

def main():
    db = {}

    insert_degree_program(db, "ITBBA")
    insert_degree_program(db, "EXPER")

    insert_course(db, "ITBBA", ("Python Programming", 5))
    insert_course(db, "ITBBA", ("Time Management", 3))
    insert_course(db, "EXPER", ("Creative Hospitality and Tourism", 5))
    insert_course(db, "EXPER", ("Managing Dynamic Restaurant Business", 10))

    print_degree_program(db, "ITBBA")
    print_degree_program(db, "EXPER")
    
main()
def insert_degree_program(db: dict, degree_program: str):
    if degree_program in db.keys():
        print(f"{degree_program} is already in the database")
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
    if degree not in db:
        print(f"Unknown degree program: {degree}")
    else:
        word = "course"
        if len(db[degree]) > 1:
            word = "courses"
        print(f"{degree} ({len(db[degree])} {word})")
        total = 0
        for course, credits in db[degree]:
            print(f"  {course}, {credits} credits")
            total += credits
        print(f"  Total credits: {total}")

def remove_course(db, degree, course):
    if degree not in db:
        print(f"Unknown degree program: {degree}")
    else:
        flag = False
        for course_name, _ in db[degree]:
            if course_name == course:
                flag = True
                db[degree].remove((course_name, _))
        if flag is False:
            print(f"Unknown course: {course}")

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
    print()

    remove_course(db, "ITBBA", "Python Programming")
    print_degree_program(db, "ITBBA")
    print()

    # Testing error handling
    insert_degree_program(db, "ITBBA")
    insert_course(db, "ITBBA", ("Time Management", 3))

    print_degree_program(db, "LOBBY")
    remove_course(db, "COMPU", "Surfing")
    remove_course(db, "ITBBA", "Surfing")
main()
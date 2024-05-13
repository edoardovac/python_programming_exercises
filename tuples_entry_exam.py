def grade_exam(applicants: list, exam_passing_score: int):
    good_students = []
    for i in range(len(applicants)):
        if applicants[i][1] >= exam_passing_score:
            good_students.append(applicants[i])
    return good_students

def main(): 
    applicants = [
        ("Ann", 30), 
        ("Jack", 25), 
        ("Jill", 40)
        ] 
    passed_applicants = grade_exam(applicants, 30) 
    print("Entry exam passed") 
    for name, points in passed_applicants: 
        print(f"{name}, {points} points") 

if __name__ == "__main__": 
    main()
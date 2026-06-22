students=[]
def calculate_avg(scores):
    if len(scores)==0:
        return 0
    else:
        return sum(scores)/len(scores)

def letter_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    elif avg>=60:
        return "D"
    else:
        return "F"

def add_student():
    scores=[]
    name=input("student name:").strip()

    while True:
        score=input("enter score or 'done':").strip()
        if score.lower() == "done":
            break
        try:
            score = int(score)
        except ValueError:
            print("please enter a valid integer score or 'done'")
            continue

        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("score must be between 0 and 100")

    avg = calculate_avg(scores)
    grade = letter_grade(avg)
    students.append({"name":name,"scores":scores,"avg":avg,"grade":grade})
    print("student added successfully")
def display_students():
    for student in students:
        print(f"name:{student['name']},scores:{student['scores']},avg:{student['avg']},grade:{student['grade']}")
def show_class_report():
    if len(students)==0:
        print("no students in class")
    else:
        total_avg=sum(student['avg'] for student in students)/len(students)
        print(f"class average:{total_avg}")
        grade_counts={"A":0,"B":0,"C":0,"D":0,"F":0}
        for student in students:
            grade_counts[student['grade']]+=1
        print("grade distribution:")
        for grade,count in grade_counts.items():
            print(f"{grade}:{count}")
        highest_avg=max(students,key=lambda x:x['avg']) 
        lowest_avg=min(students,key=lambda x:x['avg'])  
        print(f"highest average:{highest_avg['name']} with avg {highest_avg['avg']}")
        print(f"lowest average:{lowest_avg['name']} with avg {lowest_avg['avg']}")
def main():
     while True:
         print("\n1. add student\n2. display students\n3. show class report\n4. exit")
         choice=input("enter your choice:")
         if choice=="1":
                 add_student()
         elif choice=="2":
                 display_students()
         elif choice=="3":
                 show_class_report()
         elif choice=="4":
                 break
         else:
                print("invalid choice. please try again.")
if __name__=="__main__":
    main()
students=[]
def add_student(name,age,course):
    student={"name":name,"age":age,"course":course}
    students.append(student)
def display_student():
    for s in students:
        print(f"Name:{s['name']},Age:{s['age']},Course:{s['course']}")
add_student("pooza",20,"information technology")
add_student("nila",20,"computer sicence")
display_student()
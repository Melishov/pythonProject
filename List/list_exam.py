import os
QUESTIONS=20
def main():
    true_answers=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
    student_answers=[]
    wrong_answers=[]
    file_answers=open('student_solution.txt','r')
    line=file_answers.readline()
    while line!='':
        line=line.rstrip('\n')
        student_answers.append(line)
        line = file_answers.readline()
    file_answers.close()
    for compare in range(QUESTIONS):
        if true_answers[compare]!=student_answers[compare]:
            wrong_answers.append(f"{compare+1} answer is wrong, it must be {true_answers[compare]}")
    if len(wrong_answers)>5:
            print("Exam is not pass, try it again later...")
    else:
            print("Exam is pass, congratulations!")
    print(f"Total correct answers-{QUESTIONS-len(wrong_answers)}, {len(wrong_answers)} answer(s) is incorrect:")
    for wrong in wrong_answers:
        print(wrong)
if __name__=="__main__":
    main()


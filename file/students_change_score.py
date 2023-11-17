import os
def main():
    flag=False
    file_with_score=open("students.txt","r")
    new_file=open("new_file.txt","w")
    name=file_with_score.readline()
    while name!="":
        name=name.rstrip("\n")
        score=file_with_score.readline()
        if name!="Джулия Милан":
            new_file.write(f"{name}\n")
            new_file.write(f"{score}")
            name=file_with_score.readline()
        else:
            flag=True
            new_file.write(f"{name}\n")
            score="Оценка 100\n"
            new_file.write(f"{score}")
            name = file_with_score.readline()
    new_file.close()
    file_with_score.close()
    os.remove("students.txt")
    os.rename("new_file.txt","students.txt")
main()
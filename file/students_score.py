import os
def main():
    flag=False
    file_with_score=open("students.txt","r")
    new_file=open("new_file.txt","w")
    name=file_with_score.readline()
    while name!="":
        name=name.rstrip("\n")
        score=file_with_score.readline()
        if name!="Джон Перц":
            new_file.write(f"{name}\n")
            new_file.write(f"{score}")
            name=file_with_score.readline()
        else:
            flag=True
            name = file_with_score.readline()
    new_file.close()
    file_with_score.close()
    os.remove("students.txt")
    os.rename("new_file.txt","students.txt")
main()
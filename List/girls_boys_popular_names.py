import os
def main():
    girls_list=[]
    boys_list=[]
    girls_file=open("GirlNames.txt","r")
    boys_file=open("BoyNames.txt","r")
    girl_name_line=girls_file.readline()
    while girl_name_line!="":
        girl_name_line=girl_name_line.rstrip('\n')
        girls_list.append(girl_name_line)
        girl_name_line = girls_file.readline()
    girls_file.close()
    boy_name_line=boys_file.readline()
    while boy_name_line!="":
        boy_name_line=boy_name_line.rstrip("\n")
        boys_list.append(boy_name_line)
        boy_name_line = boys_file.readline()
    boys_file.close()
    boy_name_for_search=input("Если нужно проверить имя мальчика, введите его имя с большой буквы, на английском языке иначе просто нажмите 'Enter' ")
    girl_name_for_search=input("Если нужно проверить имя девочки, введите её имя с большой буквы, на английском языке иначе просто нажмите 'Enter' ")
    if boy_name_for_search!='':
        if boy_name_for_search in boys_list:
            print("Данное имя мальчика входит в топ 200 популярных в США")
        else:
            print("Данное имя мальчика не входит в топ 200 США")
    if girl_name_for_search!='':
        if girl_name_for_search in girls_list:
            print("Данное имя девочки входит в топ 200 популярных в США")
        else:
            print("Данное имя девочки не входит в топ 200 США")
if __name__=="__main__":
    main()


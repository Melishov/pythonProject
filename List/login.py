def get_login_name(first,last,id):
    part1=first[:3]
    part2=last[:3]
    part3=id[-3:]
    login_name=part1+part2+part3
    return login_name
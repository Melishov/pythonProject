def main():
    name=input("Input your name: \n")
    info=input("Input some information about you: \n")
    html_file=open("about.html","w")
    html_file.write(f"<html>\n<head>\n</head>\n<body>\n  <center>\n    <h1>{name}</h1>\n  </center>\n  <hr />\n  {info}\n  <hr />\n</body>\n</html>")
    html_file.close()
    print("Your HTML file is created with name about.html!")
main()
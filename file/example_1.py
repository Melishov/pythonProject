import random
random=random.randint(100,100000)
num_fil1e=open("num.txt","w")
num_fil1e.write(str(random))
num_fil1e.close()
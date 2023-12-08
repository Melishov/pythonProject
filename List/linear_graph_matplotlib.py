
import matplotlib.pyplot as plt
x_coords=[0,1,2,3,4]
y_coords=[0,3,1,5,2]
plt.plot(x_coords,y_coords,marker="o")
plt.title("It's hills!")
plt.ylabel("Hills height")
plt.xlabel("Hills length")
plt.grid(True)
plt.xlim(xmin=0,xmax=10)
plt.ylim(ymin=0,ymax=10)
plt.xticks([1,2,3,4,5,6,7,8,9,10],["One","Two","Three","Four","Five",
                                   "Six","Seven","Eight","Nine","Ten"])
plt.yticks([1,2,3,4,5,6,7,8,9,10],["One","Two","Three","Four","Five",
                                   "Six","Seven","Eight","Nine","Ten"])
plt.show()
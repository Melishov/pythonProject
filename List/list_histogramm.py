import matplotlib.pyplot as plt
def main():
    left_edges=[1,2,3,4,5]
    heights=[500,175,315,600,10]
    bar_width=0.1
    plt.bar(left_edges,heights,bar_width,color=('r', 'g', 'b', 'm', 'k'))
    plt.show()
main()
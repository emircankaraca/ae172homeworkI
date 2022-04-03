PATHFILE = "data.txt"
H_REYNOLDS_PATH = "HighestReynolds.csv"
L_REYNOLDS_PATH = "LowestReynolds.csv"
PATHFILE = "data.txt"
from matplotlib import pyplot as plt
import csv, math
airfoil_data = open(PATHFILE)
datalist = airfoil_data.readlines()
x_data = []
y_data = []
for item in datalist:
    item = item[:-2]
    q = item.split(" ")
    coor = (float(q[0]), float(q[1]))
    x_data.append(coor[0])
    y_data.append(coor[1])
airfoil_data.close()
camber_data = []
for i in range(23):
    camber_data.append((y_data[i]+y_data[i+23])/2)
# plt.xlim((0,1))
# plt.ylim((-0.0404, 0.0678))
# plt.plot(x_data, y_data)
# plt.plot(x_data[:23], camber_data, color="green")
# plt.plot([0,1],[0,0], linewidth=1.5, color="red")
# plt.axis("equal")
# plt.title("BOEING 737 OUTBOARD AIRFOIL")
# plt.legend(["Airfoil".upper(), "Mean Camber Line".upper(), "Chord Line".upper()])
# plt.show()
plot_data = []
with open(H_REYNOLDS_PATH, "r") as data_file:
    data_reader = csv.reader(data_file)
    next(data_reader)
    for line in data_reader:
        plot_data.append(line)
alpha, cl, cd, cdp, cm, top_xtr, bot_xtr, xcp_data = [], [], [], [], [], [], [], []
for row in plot_data:
    alpha.append(float(row[0]))
    cl.append(float(row[1]))
    cd.append(float(row[2]))
    cdp.append(float(row[3]))
    cm.append(float(row[4]))
    a = float(row[0])*math.pi/180
    top_xtr.append(float(row[5]))
    bot_xtr.append(float(row[6]))
    xcp = (0.25+(float(row[4])/(float(row[1])*math.cos(a)+float(row[2])*math.sin(a))))
    xcp_data.append(xcp)
plot_data1 = []
with open(L_REYNOLDS_PATH, "r") as data_file:
    data_reader = csv.reader(data_file)
    next(data_reader)
    for line in data_reader:
        plot_data1.append(line)
alpha1, cl1, cd1, cdp1, cm1, top_xtr1, bot_xtr1, xcp_data1 = [], [], [], [], [], [], [], []
for row in plot_data1:
    alpha1.append(float(row[0]))
    cl1.append(float(row[1]))
    cd1.append(float(row[2]))
    cdp1.append(float(row[3]))
    cm1.append(float(row[4]))
    a1 = float(row[0])*math.pi/180
    top_xtr1.append(float(row[5]))
    bot_xtr1.append(float(row[6]))
    xcp1 = (0.25+(float(row[4])/(float(row[1])*math.cos(a1)+float(row[2])*math.sin(a1))))
    xcp_data1.append(xcp1)
# plt.plot(alpha, xcp_data, label="Highest Re")  # (X AXIS, Y AXIS)
# plt.plot(alpha1, xcp_data1, label="Lowest Re")
# plt.legend()
# plt.title("XCP vs. Alpha Graph")
# plt.show()












# Name: Eli Manashirov
# ID: 208676742
# Name: Niv Tal
# ID: 207992975

ax=[[4,2,0],[2,10,4],[0,4,5]]
b=[2,6,5]
def GaussSeidel(ax,b):
    x = 0
    y = 0
    z = 0
    epsilon = 0.001
    i = 0
    for i in range (10):
        X_1 =   (b[0] - ax[0][1]*y - ax[0][2]*z) / ax[0][0]
        Y_1 =   (b[1] - ax[1][0]*X_1 - ax[1][2]*z) / ax[1][1]
        Z_1 =   (b[2] - ax[2][0]*X_1 - ax[2][1]*Y_1) / ax[2][2]
        print("Gauss–Seidel i number",i,":",X_1," ",Y_1," ",Z_1)
        if X_1 - x < epsilon and Y_1 - y < epsilon and Z_1 - z < epsilon:
            break

        x = X_1
        y = Y_1
        z = Z_1


def Jacobi(ax,b):
    x = 0
    y = 0
    z = 0
    epsilon = 0.001
    i = 0
    for i in range (10):
        X_1 =   (b[0] - ax[0][1]*y - ax[0][2]*z) / ax[0][0]
        Y_1 =   (b[1] - ax[1][0]*x - ax[1][2]*z) / ax[1][1]
        Z_1 =   (b[2] - ax[2][0]*x - ax[2][1]*y) / ax[2][2]
        print("Jacobi i number",i,":",X_1," ",Y_1," ",Z_1)
        if X_1 - x < epsilon and Y_1 - y < epsilon and Z_1 - z < epsilon:
            
            break

        x = X_1
        y = Y_1
        z = Z_1

def Dominant_diagonal(ax):
    if(abs(ax[0][0]>ax[0][1] + ax[0][2]) and abs(ax[1][1]>ax[1][0]+ax[1][2]) and abs(ax[2][2]>ax[2][0]+ax[2][1])):
        print("Is Dominant_diagonal")
        return True
    print("Not Dominant_diagonal")
    return False
GaussSeidel(ax,b)
Jacobi(ax,b)
Dominant_diagonal(ax)



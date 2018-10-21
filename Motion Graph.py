import matplotlib.pylab as plt
import numpy as np
import math as m

#velocity
v1 = int(input("Enter the initial Velocity (m/s) >> "))
#gravity
g = 9.8
#angle
theta1 = m.radians(int(input("Enter angle of projection (degrees) >> ")))


tmax1 = ((2*v1)*np.sin(theta1))/g   # Formula to find time
timemat1 = tmax1*np.linspace(0,1)  # Time vector

x = (v1*timemat1) * np.cos(theta1)  # Formula to find the x position
y = (v1*timemat1) * np.sin(theta1) - (0.5*g)*(timemat1**2)


#velocity
v2 = int(input("Enter the initial Velocity (m/s) >> "))
#gravity
g = 9.8
#angle
theta2 = m.radians(int(input("Enter angle of projection (degrees) >> ")))

tmax2 = ((2*v2)*np.sin(theta2))/g   # Formula to find time
timemat2 = tmax2*np.linspace(0,1)  # Time vector

x2 = (v2*timemat2) * np.cos(theta2)  # Formula to find the x position
y2 = (v2*timemat2) * np.sin(theta2) - (0.5*g)*(timemat2**2)

#velocity
v3 = int(input("Enter the initial Velocity (m/s) >> "))
#gravity
g = 9.8
#angle
theta3 = m.radians(int(input("Enter angle of projection (degrees) >> ")))
tmax3 = ((2*v3)*np.sin(theta3))/g   # Formula to find time
timemat3 = tmax3*np.linspace(0,1)  # Time vector

x3 = (v3*timemat3) * np.cos(theta3)  # Formula to find the x position
y3 = (v3*timemat3) * np.sin(theta3) - (0.5*g)*(timemat3**2)


# Graph title and x axis and y axis labels
plt.title("Projectile Motion", fontsize=20)
plt.xlabel("Angle")
plt.ylabel("Velocity")

#Plotting the data
plt.plot(x,y, label = "Ball 1")
plt.plot(x2,y2, label = "Ball1 ")
plt.plot(x3,y3, label = "Ball 3")

#Displaying a legend and showing the graph
plt.legend()
plt.show()

#Reference from Jason

# Celestial-Mechanics-Application
Physics simulation deploying three-body model and four-body model to achieve a fuel-efficient spaceship trajectory

Firstly, the three-body system is constructed with earth, moon and a spaceship as example. The trajectory of spaceship around earth is designed to maximize the utilization of gravitational pulls of earth and moon to keep the change in the gravitational energy of the third body (the spaceship) to a minimum.

Firstly, the Lagrange point of the earth and moon system need to be found. The Lagrange point is position where the gradational pulls of the two bodies, earth and moon in this case, together to give the centripetal force that the third body needs:

Animation for Lagrange point 1 in normalized earth and moon frame:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/L1.gif)

Then, the gravitational potential field of the earth and moon is computed which gives both the Lagrange points and the general idea of the ideal trajectory.

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/2-D%20plot.png)

The trajectory, with a specfic starting point, is then found using Legendre transformation and Euler-Lagrange equations to give a low-energy path way. 

Animation: Using three-body model with a conservation of energy

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/Lagrange-Potential-Field/animation.gif)

The Energy change is concluded to be within 1E-5 J and trajectory is concluded to be around the lagrange points and has a specfic shape as follow:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation/Energy.png)

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation/Position%203-body.png)

# Celestial-Mechanics-Application
Physics simulation deploying three-body model and four-body model to achieve a fuel-efficient spaceship trajectory

Firstly, the three-body system is constructed with earth, moon and a spaceship as example. The trajectory of spaceship around earth is designed to maximize the utilization of gravitational pulls of earth and moon to keep the change in the gravitational energy of the third body (the spaceship) to a minimum.

Firstly, the Lagrange point of the earth and moon system need to be found. The Lagrange point is position where the gradational pulls of the two bodies, earth and moon in this case, together to give the centripetal force that the third body needs:

Animation for Lagrange point 1 in normalized earth and moon frame:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/L1.gif)

Then, the gravitational potential field of the earth and moon is computed which gives both the Lagrange points and the general idea of the ideal trajectory.

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/2-D%20plot.png)

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/four_body-problem/Lagrange%20field%20and%20point/output.png)

The trajectory, with a specfic starting point, is then found using Legendre transformation and Euler-Lagrange equations to give a low-energy path way. 

Animation: Using three-body model with a conservation of energy

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Animation%20part/Animation.gif)

The Energy change is concluded to be within 1E-5 J and trajectory is concluded to be around the lagrange points and has a specfic shape as follow:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation%20by%20Jacob/Position_3_body--Jacob.png)

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation%20by%20Jacob/Energy--Jacob.png)

Next step how ever is to escalate to a general three body, but we start with the two body problem in a zero momentum frame and call them test case 1 and 2,
test case 1

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/2_body_testcase1.gif)

Then we add a third body, the spaceship into it, but still keep the total momentum of the system the same while considering the force of the two other bodies on the spaceship:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/spaceship%20ani.gif)

A trajectory stating from given intial point goes into the two body and then leaves to infinity. However, the trajectory can be considered to be a best apporximation and low-energy pathway for the spaceship. To move this problem into the earth moon frame, just give whatever intial condition and change the speed of the spaceship will push the spaceship in the desired spaceship in a desired trajectory in a most efficient way.

The same idea goes in test case 2, however, exception exists when the intial condition happens to give the spaceship a trajectory which is relatively stable. In that case, another accerlaratin is needed.

test case 2:

2 body:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/2body_case2.gif)

stable trajectory:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/stable_testcase2.gif)

normal case:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/unstable_testcase2.gif)

At the end, the deterministic chaotic pattern in the optimal trajectory in the solution can be justified by modeling a scenrio where 1000 spaceships are added into concentric orbits around a star with different radius. And at the same time, a second planet is added at the boundary and its force on those spaceships are considered. The effect will be like this:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/Influence%20on%20test%20spaceship/restricted_threebody/optimized.gif)

P.S.
justification of RK4 in this method is not proved with error drop by 16 with h drops by a factor of 1/2:
![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/output.png)

The RK2 behaviour is due to the way to find the partial derivative use only central limit therom which is RK2 level, thus, a change of method will be applied.





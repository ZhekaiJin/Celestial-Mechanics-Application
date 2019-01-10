# Celestial-Mechanics-Application
* Physics simulation deploying three-body model and four-body model to achieve a fuel-efficient spaceship trajectory

## Three-body Problem

* The three-body system is constructed with earth, moon, and a spaceship as an example. The trajectory of spaceship around the earth is designed to maximize the utilization of gravitational pulls of earth and moon to keep the change in the gravitational energy of the third body (the spaceship) to a minimum.

#### Lagrange Point and Potential

* Firstly, the Lagrange point of the earth and moon system need to be found. The Lagrange point is the position where the gradational pulls of the two bodies, earth, and moon in this case, together to give the centripetal force that the third body needs:

* Animation for Lagrange point 1 in normalized earth and moon frame:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/L1.gif)

* Then, the gravitational potential field of the earth and moon is computed which gives both the Lagrange points and the general idea of the ideal trajectory.

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Lagrange%20field%20and%20point/2-D%20plot.png)

#### Fuel-free Trajectory

* The trajectory, with a specific starting point, is then found using Legendre transformation and Euler-Lagrange equations to give a low-energy pathway. 

* Animation: Using a three-body model with conservation of energy

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Animation%20part/Animation.gif)

* The Energy change is concluded to be within 1 e<sup>-5</sup> J and trajectory is concluded to be around the Lagrange points and has a specific shape as follow:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation%20by%20Jacob/Position_3_body--Jacob.png)

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Optimum%20Trajectory%20in%20earth_moon%20system/RK4%20approximation%20by%20Jacob/Energy--Jacob.png)

#### General Three-body problem 

* Next step, however, is to escalate to a general three body, but we start with the two body problem in a zero momentum frame and call them test case 1 and 2,

##### Test Case 1

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/2_body_testcase1.gif)

* Then we add a third body, the spaceship into it, but still keep the total momentum of the system the same while considering the force of the two other bodies on the spaceship:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/spaceship%20ani.gif)

* A trajectory starting from given initial point goes into the two bodies and then leaves to infinity. However, the trajectory can be considered to be a best approximation and low-energy pathway for the spaceship. To move this problem into the earth-moon frame, just give whatever initial condition and change the speed of the spaceship will push the spaceship in the desired spaceship in the desired trajectory in a most efficient way.

* The same idea goes in test case 2, however, an exception exists when the initial condition happens to give the spaceship a trajectory which is relatively stable. In that case, another acceleration is needed.

##### Test Case 2

`2 bodies: ` 

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/2body_case2.gif)

`stable trajectory: `

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/stable_testcase2.gif)

`normal case:`

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/unstable_testcase2.gif)

#### Deterministic Chaos

* At the end, the deterministic chaotic pattern in the optimal trajectory in the solution can be justified by modeling a scenario where 1000 spaceships are added into concentric orbits around a star with different radius. And at the same time, a second planet is added at the boundary and its force on those spaceships are considered. The effect will be like this:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/Influence%20on%20test%20spaceship/restricted_threebody/optimized.gif)

#### A newly upgraded accurate approximation to Euler's three-body problem with changeable speed. ([link](https://sites.google.com/site/celestialmechanicspresentation/home/three-body-design))

#### Justification of RK4

* justification of RK4 in this method is proved with error drop by 16 with h drops by a factor of 1/2:
![alt tag](src/Optimum%20Trajectory%20in%20earth_moon%20system/output-2.png)

* After three-body problem, we extend to the problem to include the sun's effect on the spaceship, too. But we are still focused on the earth and moon rotating frame.



## Four Body Probelm:

#### Fuel-free Trajectory

* Animation including the sun:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/four_body-problem/Presentation/4%20BODY.gif)


* The final trajectory and energy change of the trajectory:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/four_body-problem/Presentation/18217721_1908629269426223_312539679_n.png)

* The energy conservation is held.

* And the final trajectory is like this:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/four_body-problem/Presentation/18254533_1908629252759558_1318339708_n.png)


#### Optimazaiotn:


![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/master/src/Presentation/show.png)



![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/four_body-problem/Optimazation%20in%20four%20body%20system/output.png)


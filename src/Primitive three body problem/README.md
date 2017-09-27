#Primitive three body problem

**Contributer** Scott Jin

## Zero Momentum Attempt

* Next step how ever is to escalate to a general three body, but we start with the two body problem in a zero momentum frame and call them test case 1 and 2,

### Test Case 1

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/2_body_testcase1.gif)

* Then we add a third body, the spaceship into it, but still keep the total momentum of the system the same while considering the force of the two other bodies on the spaceship:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%201/spaceship%20ani.gif)

* A trajectory stating from given intial point goes into the two body and then leaves to infinity. However, the trajectory can be considered to be a best apporximation and low-energy pathway for the spaceship. To move this problem into the earth moon frame, just give whatever intial condition and change the speed of the spaceship will push the spaceship in the desired spaceship in a desired trajectory in a most efficient way.

* The same idea goes in test case 2, however, exception exists when the intial condition happens to give the spaceship a trajectory which is relatively stable. In that case, another accerlaratin is needed.

### Test Case 2

`2 body:` 

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/2body_case2.gif)

`stable trajectory:`

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/stable_testcase2.gif)

`normal case:`

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/zero%20momentum%20attempt/test%20case%202/unstable_testcase2.gif)

### Deterministic Chaos

* At the end, the deterministic chaotic pattern in the optimal trajectory in the solution can be justified by modeling a scenrio where 1000 spaceships are added into concentric orbits around a star with different radius. And at the same time, a second planet is added at the boundary and its force on those spaceships are considered. The effect will be like this:

![alt tag](https://github.com/ZhekaiJin/Celestial-Mechanics-Application/blob/three_body_problem/Primitive%20three%20body%20problem/Influence%20on%20test%20spaceship/restricted_threebody/optimized.gif)

### An new upgraded Euler-accuray program with changable speed.
https://sites.google.com/site/celestialmechanicspresentation/home/three-body-design

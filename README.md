# Silly Autonomous Cars
The silly autnomous car project was the result of the two-day San Francisco Science Hackday event.

## Project Inspiration
At the start of the Science Hackday, Helen Lurie spoke about how she is leading the way at Lyft towards an autonmous vehicle future. She talked about a particular challenge in the autonomous vehicle world: how does a car make trusted decisions when the underlying AI processor can't be trusted (either because of hardware failure or an AI algorithm that has gone rogue)?

One way that you can solve this problem is by using a "Voting Architecture" with multiple AI processors working against the same input. To implement this, you might put three different computers on board each car.  The car is constantly asking each computer "What should I do next?"  If Computer A says "go left" and Computer B and C say "go right", the car should turn right.  That is how the car safely handles if Computer A winds up going haywire. It's a really neat solution to a problem that has dire consequences.

For this hackathon, we asked the question: what would happen if we build the voting architecture but rewire it for sillyness?  What if we had multiple cars tied together on a single voting architecture?  Could we have Car A respond to what Car B sees and vice versa?  What weird behavior can we make?

## What We Hope To Learn
The purpose of this project is to roll up our sleeves and get first-hand experience learning about how autonomous cars are built. We want to rapidly explore how Deep Learning and a rules engine (voting engine) can be used together to control RC cars. 

## Our Plan
Since we have 24 hours, we know that we will have to take some shortcuts and get creative.  We decided to split into the following subteams so that we could move quickly:
1) The Eyes - Machine Learning Sensor built as an iPhone app.
2) The Brain - A python web server to consume events from The Eyes, calculate all of the acutal logic, and send events to The Car.
3) The Car - A hacked RC-car to which we strapped an Arduino + Particle.

Why didn't we do everything on-board the Arduino?  Because it would have slowed us down and it would be hard to build our multicar voting architecture. Plus, our architecture is intentionally silly.  

## Credits
Harshita
Samira
Heidi
Peter
Joanna
Rolf
Seth
Trevor
Daisy
Cherry

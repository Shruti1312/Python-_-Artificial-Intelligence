# Python-_-Artificial-Intelligence

<h1>There are two Problems here with two Algo's</h1>
<ul>
  <li><h3>Min-Max Algorithm for Housing Assignment Problem</h3>
    Problem Description: Los Angeles Homeless Services Authority (LAHSA) and Safe Parking LA (SPLA) are
    two organizations in Los Angeles that service the homeless community. LAHSA
    provides beds in shelters and SPLA manages spaces in parking lots for people living
    in their cars. In the city’s new app for homelessness, people in need of housing can
    apply for a space with either service. For this homework, you will help SPLA choose
    applicants that meet the SPLA specific requirements for the space and that also
    optimize the use of the parking lot for that week.
    </li>
  <li>
    <h3>Reinforcement Learning Algorithm using Move Policy:</h3>
        You are the CTO of a new startup company, SpeedRacer, and you want your
        autonomous cars to navigate throughout the city of Los Angeles. The cars can move
        North, South, East, or West. The city can be represented in a grid, as below:
        
                    0,0 1,0 2,0 3,0 4,0
                    0,1 1,1 2,1 3,1 4,1
                    0,2 1,2 2,2 3,2 4,2
                    0,3 1,3 2,3 3,3 4,3
      
     
    There will be some obstacles, such as buildings, road closings, etc. If a car crashes
    into a building or road closure, SpeedRacer has to pay $100. You also spend $1 for
    gas when at each grid location along the way. The cars will start from a given
    SpeedRacer parking lot, and will end at another parking lot. When you arrive at your
    destination parking lot, you will receive $100. Your goal is to make the most
    money over time with the greatest likelihood. Your cars have a faulty turning
    mechanism, so they have a chance of going in a direction other than the one
    suggested by your model. They will go in the correct direction 70% of the time, with
    a 10% chance of going in each of the other three directions instead.
    The first part of your task is to design an algorithm that determines where your cars
    should try to go in each city grid location given your goal of making the most money.
    Then, to make sure that this is a good algorithm when you present it to the rest of
    your board, you should simulate the car moving through the city grid. To do this,
    you will use your policy from your start location. You will then check to see if the car
    went in the correct direction using a random number generator with specific seeds
    to make sure you can reproduce your output. You will simulate your car moving
    through the city grid 10 times using the random seeds 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10.
    You will report the mean over these 10 simulations as an integer after using the
    floor operation (e.g., numpy.floor(meanResult)).
  </li>
</ul>

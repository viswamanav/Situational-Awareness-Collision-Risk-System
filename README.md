# Situational-Awareness-Collision-Risk-System
This project is a simple real-time situational awareness system built using Python and Pygame. The idea behind this project is to simulate multiple vessels moving in a radar environment and continuously monitor the collision risk between them using CPA (Closest Point of Approach) and TCPA (Time to Closest Point of Approach).

The system displays an own ship along with multiple target ships on a radar screen. As the simulation runs, every target vessel is analyzed and classified as Safe, Warning, or Danger depending on its predicted collision risk. The information is updated in real time and displayed on the radar interface.

# Features

- Real-time vessel movement simulation
- CPA and TCPA based collision risk analysis
- Risk classification into Safe, Warning and Danger
- Interactive radar display
- Zoom in and zoom out using the mouse wheel
- Pan the radar by dragging with the mouse
- Add new target vessels during simulation
- Remove target vessels dynamically
- Display vessel ID, CPA, TCPA and current risk level

# Project Structure

- main.py - Starts the application, handles user input and connects all the modules.
- vessel.py - Contains the Vessel class and handles movement and velocity calculations.
- simulation.py - Manages the simulation by creating, updating and removing vessels.
- risk.py - Calculates CPA, TCPA and determines the collision risk.
- ui.py - Draws the radar, vessels and information panel using Pygame.

# Technologies Used
- Python
- Pygame
- Object Oriented Programming
- Mathematical calculations for collision prediction
- 
# Installation

- Clone the repository
- git clone https://github.com/viswamanav/Situational-Awareness-Collision-Risk-System.git

Move into the project folder

- cd Situational-Awareness-Collision-Risk-System

- Install the required package

- pip install pygame

You can also install all dependencies using

- pip install -r requirements.txt
- Running the Project
- python main.py
  
# Controls
- Space - Pause or Resume the simulation
- A - Add a target vessel
- D - Remove the last target vessel
- Mouse Wheel - Zoom In or Zoom Out
- Left Mouse Button + Drag - Pan the radar view
  

# SYSC3010 Lab4 Deliverables

## The deliverables consist of:

### 1. [*`Lab4-fritzing-conflict-breadboard-view.png`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/Lab4-fritzing-conflict-breadboard-view.png)
   - A screenshot of fritzing breadboard view showing the resolution of the conflict presented in the lab manual. 

### 2. [*`Lab4-fritzing-conflict-schematic-view.png`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/Lab4-fritzing-conflict-schematic-view.png)
   - A screenshot of fritzing schematic view showing the resolution of the conflict presented in the lab manual. 

### 3. [*`Lab4-fritzing-i2c-breadboard-view.png`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/Lab4-fritzing-i2c-breadboard-view.png)
   - A screenshot of the breadboard view in fritzing showing an example of connecting an I2C sensor to the Raspberry Pi.

### 4. [*`traffic_lights.py`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/traffic_lights.py)
   - A Python class written to initialize three LEDs via GPIO pins and contains 3 methods where each method, when called, sets one LED and turns off the other two LEDs, depicting a traffic light operation. 
   
### 5. [*`traffic_lights_test.py`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/traffic_lights_test.py)
   - A Python script to test the written class in number 4 above. Where it checks if only one LED  is active at once and throws an error otherwise. 

### 6. [*`crosswalk_simulation.py`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/crosswalk_simulation.py)
   - A Python script that runs the traffic light LEDs and crosswalk Button. If the light is currently green, and the crosswalk button is triggered, it will transition from Green to Amber to Red, allowing a pedestrian to cross. After which it will resume normal operation, 5 seconds Green, 2 seconds Amber, 5 seconds Red. 
   
### 7. [*`crosswalk_circuit.png`*](https://github.com/ahmadalkawasmeh/RPi-Experiments/blob/main/Lab4/crosswalk_circuit.png)
   - A picture depicting the circuit components and connections on the breadboard used for running the crosswalk in number 6 above. 
   

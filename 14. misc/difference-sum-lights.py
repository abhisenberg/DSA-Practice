from typing import List

'''
Question:
You are on a street with street lights, represented by an array lights.
Each light is given as [position, radius], which means that the light is located at position, and shines to the left and right at a distance of radius. Let's say the brightest spot on the street is the spot where the most lights are shining.
Return any such position.
Note that the street is extremely long - position <= 10^18.
'''

#Since the problem mentions that the street is very long,
#it would be too expensive to use the same method as in the first example where we "build" the street and then walk along it
#Hence we will build a "change" array

def brightestLight(lights: List[List[Int]]):
    
    #0. Create the change array, which records the change in light at relevant spots
    change = []
    for position, radius in lights:
        change.append([position, 1])    #Add 1, indicating we enter a lightup zone
        change.append([position + radius + 1, -1]) #Subtract 1, we exit that zone

    #1. Sort the change array to traverse the zones linearly in correct order
    change.sort()

    #2. Traverse the array and keep track of the current brightness
    currBrightness, maxBrightness, maxBrightSpot = 0, 0, 0
    for position, value in change:
        currBrightness += value
        if currBrightness > maxBrightness:
            maxBrightness = currBrightness
            maxBrightSpot = position
    
    return maxBrightSpot

# Author:      Eddie F. Carrizales
# Date:        07/20/2022
# Problem Description:
"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going
from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one
destination city.
"""

# ------UMPIRE------

# --Understand--
"""
Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. 
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"
"""

# --Match--
# -hashtable/dictionary

# --Plan--
"""
1. create an empty hashtable/dictionary
2. using a for loop add the first city as the key, and the destination of that city as a value
3. using a second for loop traverse every key and check if the value of that key is a key in the dictionary
4. if the vale is not a key, then return the value as that will be the last destination city
"""

# --Implement--
input_paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def destination_city(paths):
    city_dict = {}

    # add every city into our city_dictionary as key: first city, value: destination city
    for cities in paths:
        city_dict[cities[0]] = cities[1]

    for key in city_dict:
        # if the destination city is not a first city, return the destination city
        if city_dict[key] not in city_dict.keys():
            return city_dict[key]

print(destination_city(input_paths))

# --Review--
# Was a simple problem to solve/implement
# Solution ran successfully on leetcode

# --Evaluate--
# Time complexity: O(N) due to adding all the cities in the dictionary using for loop and comparing destination cities to first cities
# Space complexity: O(N) since we created a hashtable/dictionary to add our cities into
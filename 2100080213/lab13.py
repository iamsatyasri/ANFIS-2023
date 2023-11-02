import numpy as np
def euclidean distance(pointi, point2)
Calculate the Euclidean distance between two points in 20 space.
return np linalg norm(np.array(point) op array(point2))
def nea neighbor_tsp(points)
Solve the Traveling Salesman Froblem using the nearest neighbor algorithm.
Args:
points: A list tuples representing the coordinates of cities
Returns
tour A list representing the order in which cities should be visited.
total distance The total distance of the tour
mum cities len(points)
unvisited cities set(range(num cities))
current city Start from the first city tour [current_city]
total distance
while len(tour) nue cities
nearest city in(visited cities, key lambda city exclidean distance(paints[current city), points(city)))
total distance euclidean distance(points[current_city), points[nearest city))
current city nearest city Tour append(current city)
isited cities.remove(current city)
Return to the starting city to complete the tour.
total distance euclidean distance(points[current_city], points [tour[e]])
tour append(tour[0])
return tour, total_distance
#Example usage:
cities [(0, 0), (2, 4), (3, 1), (5, 3), (6, 6)] tour, total distance nearest neighbor_tsp(cities)
print("Optimized Tour Order:", tour)
print("Total Distance:", total distance)

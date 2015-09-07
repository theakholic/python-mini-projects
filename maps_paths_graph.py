Inf = float("inf")
CITIES = ["A", "B", "C", "D", "E"]
paths  = {("A","A"):0, ("A","B"):1, ("A","C"):3, ("A","D"):7 , ("A","E"):Inf,
               ("B","A"):Inf, ("B","B"):0, ("B","C"):42, ("B","D"):6, ("B","E"):27,
               ("C","A"):Inf, ("C","B"):Inf, ("C","C"):0, ("C","D"):2, ("C","E"):13,
               ("D","A"):Inf, ("D","B"):Inf, ("D","C"):Inf, ("D","D"):0, ("D","E"):5,
               ("E","A"):Inf, ("E","B"):Inf, ("E","C"):Inf, ("E","D"):Inf, ("E","E"):0
}

def shortest_path(cities = CITIES, cost = paths):
	"""Return the shortest path from the first city to the last city in cities."""
	
	if len(cities) == 1:
		return 0 #we've reached
	
	first = cities[0]
	#print(first)
	rest = cities[1:]
	#print(len(rest))
	
	#print "Shortest path from", cites[0], "to", cities[-1],"is",
	best_route = min([(cost[(first,x)] + shortest_path(rest[i:],paths)) for i,x in enumerate(rest)])
	# sprint best_route
	return best_route





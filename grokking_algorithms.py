from collections import deque


def main():        
    ### BINARY SEARCH
    ## O(log n)
    # list = [1, 3, 5, 7, 9, 13, 15, 17, 19, 21, 23, 25]        
    # item = 19
    # low = 0
    # high = len(list) - 1

    # while low <= high:
    #     mid = (low + high)//2
    #     # print("\n low: " + str(low) + "\n high: " + str(high) + "\n mid: " + str(mid))
    #     guess = list[mid]

    #     if guess == item:
    #         print("answer is: " + str(mid))
    #         break
    #     if guess > item:
    #         print ("Guess is to high, mid - 1= " + str(mid-1))
    #         high = mid - 1
    #     else:
    #         print ("Guess is to low, mid + 1= " + str(mid+1))
    #         low = mid + 1
    
    ### SELECTION SORT 
    ## O(n^2)
    ## First a function to find the smallest item
    # arr = [5, 6, 3, 2, 10]
    # def findSmallest(arr):        
    #     smallest = arr[0]
    #     smallest_index = 0

    #     for i in range(1, len(arr)):
    #         if arr[i] < smallest:
    #             smallest = arr[i]
    #             smallest_index = i
    #     return smallest_index

    ## Then a function that uses the smallest item function to sort the array into a new one
    # newArr = []
    # for i in range(len(arr)):
    #     smallest = findSmallest(arr)
    #     newArr.append(arr.pop(smallest))
    # print(newArr)

    ### RECURSION    
    ## Simple recursive function
    # def countdown(i):        
    #     print(i)
    #     if i <= 1: # Base Case
    #         return
    #     else: # Recursive Case
    #         countdown (i-1)
    # x = 10

    # countdown(x)

    ## Recursive function to sum an array(it would easier to write a loop but this is how to do it with recursion/D&C mentality)
    # def rsum(list):
    #     if list == []:
    #         return(0)
    #     return list[0] + rsum(list[1:])
    
    # a = [2, 4, 6]
    # in the case of this array it is
    # 2 + our function, which is 4 + our fucntion, which is 6 + our function, which is empty so it's 6 + 0
    # 2 + 4 + 6 + 0. It's not adding the array on top of itself again and again. it's kinda like looping
    # remember it's list[0] + whatver the result of our function is. Just some extra layers to it. 
    
    # print(rsum(a))

    # def fact(x):
    #     if x ==1:
    #         return 1
    #     else:
    #         return x * (fact(x-1))

    # x = 3
    #print(fact(5))
    # same here, 5 * 4 * 3 * 2 * 1
    # b/c 5 * func, which is 4 * func, which is 3 * func which is 2 * func, which returns 1

    ### QUICKSORT 
    ## O(n log n) in the average case if you use a random pivot. This is one of the fastest sorts as a result
    ## O(n^2) if you use the first element as the pivot (my example below)
    # def quicksort(array):
    #     if len(array) < 2:
    #         return array
    #     else:
    #         pivot = array[0] # The pivot you choose can affect the sort
    #         less = [i for i in array[1:] if i <= pivot] 

    #         greater = [i for i in array[1:] if i > pivot] 

    #         return quicksort(less) + [pivot] + quicksort(greater)
    # print (quicksort([10, 5, 2, 3]))

    ### GRAPHS & Breadth-First Searches - Breadth-first finds the shorted path for an unweighted graph
    ## O(V+E) for breadth-first graph search - worst case scenario
    ## E is the edge, following each edge of the graph to find your mango seller. Worst case scenario you have to follow every edge
    ## V is every vertices, or every person in your queue. Worst case you also have to search through the whole queue
    # Graph of my friend network, starting with my friends, then friends of friends, friends of friends of friends etc
    # We're trying to find a mango seller friend (someone who's name ends in n)
    # To create a graph in python, make a hash table where the key is the person, the value is an array of all their friends
    # add each item to a QUEUE. It's called deque in python
    # Because we use a queue, we go through FIFO. So fiurst level friends get checked first, then secon level friends get added and checked
    # Etc. This ensures you're checking by level (next closest AKA breadth level search) before you move to the next level
    # We add a check to make sure a name hasn't already been included in the queue 
    # ex - Peggy is both a second level friend twice (a friend of bob who is my friend and a friend of alic who is my friend)
    # so she appears in the queue twice unless we check for her. In this case it's good practice
    # but it also prevents an infinite loop. Suppose peggy is my only friend and I am peggy's only friend
    # we would keep getting added to the next friends to search queue endlessly unless we check that we've already searched each other
    # so we keep a list of people we've already checked to reference
    # graph = {}
    # graph["you"] = ["alice", "bob", "claire"]
    # graph["bob"] = ["anuj", "peggy"]
    # graph["alice"] = ["peggy"]
    # graph["claire"] = ["thom", "jonny"]
    # graph["anuj"] = []
    # graph["peggy"] = []
    # graph["thom"] = []
    # graph["jonny"] = []
    # # print(graph)

    # def person_is_seller(name):
    #     return name[-1] == 'm'

    # search_queue = deque()
    # search_queue += graph["you"]
    # searched = []

    # def search_for_seller(search_queue):
    #     while search_queue:
    #         person = search_queue.popleft()
    #         if not person in searched:
    #             if person_is_seller(person):
    #                 print (person + " is a mango seller")
    #                 return True
    #             else:
    #                 search_queue += graph[person]
    #                 searched.append(person)
    #     return False

    # print(search_for_seller(search_queue))

    ### GRAPHS & DIJKSTRA'S ALGORITHM - Dijkstra's algo finds the shortest path of a weighted graph
    ## Graphs can also have cycles, where you can start at a node and come back around to that same node. 
    ## Undirected graphs (where nodes point back at each other) are also cycled graphs
    ## Dijkstra's Algorithm only works on graphs with no cycle or graphs with a positive weight cycle(you could 
    ## easily get stuck in the cycle and every time you run the cycle you just add weight)
    ## (Bellman-Ford algorithm works on neg-weight graphs but that's out of the book's scope)

    # graph = {}
    
    # graph["start"] = {}
    # graph["start"]["a"] = 6
    # graph["start"]["b"] = 2

    # graph["a"] = {}
    # graph["a"]["fin"] = 1
    
    # graph["b"] = {}
    # graph["b"]["a"] = 3
    # graph["b"]["fin"] = 5

    # graph["fin"] = {}

    # infinity = float("inf")
    # costs = {}
    # costs["a"] = 6
    # costs["b"] = 2
    # costs["fin"] = infinity

    # parents = {}
    # parents["a"] = "start"
    # parents["b"] = "start"
    # parents["fin"] = None

    # processed = []

    # def find_lowest_cost_node(costs):
    #     lowest_cost = float("inf")
    #     lowest_cost_node = None
    #     for node in costs:
    #         cost = costs[node]
    #         if cost< lowest_cost and node not in processed:
    #             lowest_cost = cost
    #             lowest_cost_node = node
    #     return lowest_cost_node

    # node = find_lowest_cost_node(costs)

    # while node is not None:
    #     cost = costs[node]
    #     neighbors = graph[node]
    #     for n in neighbors.keys():
    #         new_cost = cost + neighbors[n]
    #         if costs[n] > new_cost:
    #             costs[n] = new_cost
    #             parents[n] = node
    #     processed.append[node]
    #     node = find_lowest_cost_node(costs)

    ### Dynamic Programming
    ## It uses a grid! Start with smaller sub-problems and you can use those later to solve the larger problems. 
    ## It progressively builds on your estimate/subproblems so you can continue to add items
    ## It only works on descrete subproblems - there can't be subproblems with dependencies on each other
    ## When you get to your final max calculation in the grid, if you have some leftover, you can use the previously
    ## calculated maxes for smaller parts of the grid to math what is the best final grid max
    ## This was done using the knapsack problem - a thief has a 4 pound knapsack and three items to choose to steal to get the
    ## highest value of itesm - a 1 pound guitar worth $1500, a 4 pound stereo worth $3000, a 3 pound laptop worth $2000
    ## Dynamic Programming is a concept there is no one single formula. Just know it involves a grid and you build off subproblems
    ## With this you either take all of an "item" or don't take the item (you can't decide on half a cell phone.)
    ## You'd use a greedy algorithm to solve something like that

    ### KNN (K-Nearest neighbors)
    ## Good for classifying    
    ## You don't know what something is. Look at it's nearest neighbors and use that to classify it
    ## Fearure Extraction - how you find the items are similar/neighbors. The features you compare to find similar items.
    ## You want to make sure you pick good features that have meaning!
    ## These items are on a graph. Use the Pythagorean formula to find distances between graph points (will have to google it)
    ## Ex - you have a fruit that is between grapefruit and orange on a graph from small & orange to big & reddish
    ## Between it's 3 nearest neighbors, 2 are orange and 1 is grapefruit, so it's probably an orange
    ## This is also like a Netflix movie recommendation system - based on this movie, others who watched that movie watched this movi
    ## 2 parts to KNN:
    ## Classification - categorization into a group
    ## Regression - predicting a response (like a number) - so once you find the K nearest neighbors, you can math out the 
    ## "responses" or make an average of those nearest neigbors - for example, guessing what someone will rate a movie based on their 
    ## past movie ratings
    ## For the book we are using the distance formula (pythagorean formula) but in some cases it's better to use cosine similarity

    ### Trees

    ### Fourier Transorm - check out better explained site
    
    ### SHA - Secure Hash Algortihm - hashes string to string. Different hash for every string. SHA is a family of algorithms.
    ## Use newer versions SHA if you want to store, bcrypt is the current standard for password-hashing
    ## SHA is locality insensitive - dog and dot create some completely different hashes so you can't compare hashes to guess the original string
    ## Simhash and others are locality sensitive. That's useful if you just want to use a hash for comparison purposes but not security
    
    ###Diffie-Hellman & RSA - you have a public key that anyone can use to encrypt and send a message. ONLY YOU have the private key to decrypt the message
    ## Makes for very strong encryption

    print("These are Jen's notes!")

if __name__ == '__main__':
    main()
    
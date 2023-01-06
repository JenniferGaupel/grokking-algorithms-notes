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

    graph = {}
    
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1
    
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    processed = []

if __name__ == '__main__':
    main()
    
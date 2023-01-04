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
    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0] # The pivot you choose can affect the sort
            less = [i for i in array[1:] if i <= pivot] 

            greater = [i for i in array[1:] if i > pivot] 

            return quicksort(less) + [pivot] + quicksort(greater)
    print (quicksort([10, 5, 2, 3]))
if __name__ == '__main__':
    main()
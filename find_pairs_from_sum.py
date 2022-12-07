def find_pairs_integers_sum(arr, n, sum): #Time complexity is O(n) / Linear Time (faster than O(n^2))
    loop_numbers_collection = {} #Dictionary to save all numbers collection after looping arr
    for i in range(n):
        if sum - arr[i] in loop_numbers_collection: #Check if sum - arr[i] is in loop_numbers_collection
            print("Sum of pairs found in the list:",sum - arr[i],"+", arr[i], "= "+ str(sum))
        else:
            loop_numbers_collection[arr[i]] = 1 #loop_numbers_collection (save numbers into a dictionary)

if __name__ == '__main__':
    numbers_to_evaluate = str(input('Enter only integer numbers separated by space (no repeated) to find pairs of numbers that result in a definied sum: ')) #Example: 1 9 5 0 20 -4 12 16 7
    target_sum = int(input('Enter the target sum (only an integer): '))#Example 12
    user_list = numbers_to_evaluate.split()
    user_list = [int(i) for i in user_list]
    total_numbers = len(user_list)
    find_pairs_integers_sum(user_list, total_numbers, target_sum)

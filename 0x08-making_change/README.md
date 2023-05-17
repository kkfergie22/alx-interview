# 0x08-making_change

The makeChange project is a Python function that calculates the minimum number of coins required to reach a given total using different coin denominations. It utilizes a dynamic programming approach to efficiently solve this problem.

## Function Description

The makeChange function takes two arguments:

    coins (List[int]): A list of coin denominations available for making change. Each coin denomination must be a positive integer greater than 0.

    total (int): The target total for which we want to calculate the minimum number of coins.

The function returns the minimum number of coins required to reach the target total. The following rules apply:

    If the total is 0 or less, the function returns 0.

    If the total cannot be reached using the available coin denominations, the function returns -1.

## Algorithm

The makeChange function utilizes a dynamic programming approach to efficiently solve the problem. It follows these steps:

   1. Initialize an array minimum_number_array with infinity values for indices 1 to the target total, and set the first index to 0.

   2. Iterate through the amounts from 1 to the target total.

   3. For each amount, iterate through the coin denominations.

   4. Check if the current coin denomination is less than or equal to the current amount.

   5. If it is, compare the number of coins needed using the current coin denomination with the number of coins needed without using the current coin. Update minimum_number_array with the smaller value.

   6. Repeat this process for each coin denomination.

   7. After completing the iterations, check the value at minimum_number_array[total]. It represents the minimum number of coins required to reach the target total.

   8. If the value at minimum_number_array[total] is still infinity, it means it's not possible to reach the target total using the available coin denominations. In this case, the function returns -1.

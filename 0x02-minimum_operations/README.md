# Minimum Operations

## Algorithm

    1. Check if n equals 0 or 1. If so, return 0 since no operations are needed.
    2. Initialize a variable "num_ops" to 0 and "factor" to 2.
    3. While "factor" squared is less than or equal to "n", do the following:
        a. While "n" is divisible by "factor", add "factor" to "num_ops" and update "n" to be "n" divided by "factor".
         b. Increment "factor" by 1.
    4. If "n" is greater than 1, add "n" to "num_ops".
    5. Return "num_ops".

Here's a step-by-step breakdown of how the algorithm works:

    * If n equals 0 or 1, the function immediately returns 0 since no operations are needed to obtain those values.

    * The variables "num_ops" and "factor" are initialized to 0 and 2, respectively.

    * We use a while loop to iterate through each potential factor starting at 2 up to the square root of "n". We don't need to check factors greater than the square root of "n" because they will have already been accounted for by smaller factors. For example, if we've already checked factors up to 5 and found that none of them divide "n", we can be sure that the remaining factors greater than 5 won't divide "n" either.

    * Within the loop, we use another while loop to divide "n" by "factor" as many times as possible, adding "factor" to "num_ops" each time it does. This counts the number of times "factor" divides "n".

    * We increment "factor" by 1 and repeat the process with the next potential factor.

    * If "n" is greater than 1 after all the factors up to the square root of "n" have been checked, it must be a prime factor greater than the square root of "n". We add "n" to "num_ops" to count this factor.

    * Finally, we return "num_ops" which represents the sum of all the factors that divide "n".

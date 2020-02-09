## Prime numbers (with Python)
### Explanation of the code:
  The version 1 of the program starts by identifying the prime numbers. This is done by deviding every integer from 2 to n (n being the integer itself. Also the program will not divide n because of how python works). If the remainder is 0, this means that the integer is False (not prime). otherwise, it is a prime number.
  
  Later on at the video, after doing a test of how long it will take to identify the first 100,000, we see that the it takes 56 seconds and that can be decreased.
 
 The first step is to devide only until the square root. This is because after the square root, the factors of the integers starts repeting itself. For instance if we take 36, the factors are 31*1 8*4 6*6 4*8 1*31. You can see that all of the factors after 6*6 are repeating. In order to get square roots, we import the math module `import math`
  We set the max devisor as rounded square root n with this line: `max_divisor = math.floor(math.sqrt(n))` 
  ( the `math.floor` function will round it down) 
  
  After doing the adjustement, we can see that the time to run the program changed dramatically. But there is still more room for improvement.
  
  In the loop, it uses all even integers up to the limit. That is not necesarry. If the input is odd, there is no need to check the even devisers. In order to eliminate this problem we start by identifying if the integer is even or not. We do this by this code: ``if n == 2: 
  return True
if n > 2 and n % 2 == 0: 
  return False``
  Moreover, we add a third pirameter and add 3 in the range so it covers all of the odd numbers. The new range looks like this `for d in range (3, 1 + max_divisor, 2):`
  
  To sum it up, with just a few simple optimizations, there are dramatic improvement in the performence of the program. (From roughly 56
seconds to less then 0.2)


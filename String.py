
#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.'

#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6



#answer
def sum13(nums):
  while 13 in nums:
    k=nums.index(13)
    if k+1!=len(nums):
      nums.pop(k+1)
    nums.pop(k)
  return sum(nums)  
    

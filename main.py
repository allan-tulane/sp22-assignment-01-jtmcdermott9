"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
      return x
    else:
      return foo(x-1) + foo(x-2)
    

def longest_run(mylist, key):
    ### TODO
    runCount = 0
    maxRunCount = 0
    previous = None
    
    for i in mylist:
      if i == previous == key:
        runCount += 1
        if runCount > maxRunCount:
          maxRunCount = runCount
      else:
        runCount = 0
      previous = i



    return maxRunCount+1



class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    return _longest_run_recursive(mylist,key).longest_size



def _longest_run_recursive(mylist, key):
  
  if len(mylist) == 1:
    if mylist[0] == key:
      x = Result(1, 1, 1, True)
      return x
    else:
      y = Result(0, 0, 0, False)
      return y

  else:
    mid = (len(mylist))//2
    leftList = mylist[:mid]
    rightList = mylist[mid:]

    left = _longest_run_recursive(leftList, key)
    right = _longest_run_recursive(rightList, key)

    if left.is_entire_range and right.is_entire_range:
      total = left.longest_size + right.longest_size
      return Result(total, total, total, True)
    else:
      left_size = left.left_size
      if left.is_entire_range:
        left_size += right.left_size

      right_size = right.right_size
      if right.is_entire_range:
        right_size += left.right_size

    longest_size = max(left_size, right_size, right.left_size + left.right_size)

    return Result(left_size, right_size, longest_size, False)

    
    




      

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3




#   produces AssertionError when run normally
#   run with __debug__ disabled '-O' to disable assertion tests



def example(param):
    """param must be greater than 0!""" 
    assert param > 0
    # do stuff here
    print("abc")

example(1);
example(0);


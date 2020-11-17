
#   doctest example:
""" any text (like this) that isn't in shell format is ignored by doctest
>>> from typedlist import TypedList
>>> a_typed_list = TypedList(1, [1, 2, 3])
>>> a_typed_list[1] == 2
True
>>> a_typed_list[1] = 3
>>> a_typed_list[1]
3
"""

class TypedList:
    def __init__(self, example_element, initial_list=[]):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypedList must " "be a list.")
        for element in initial_list: 
            self.__check(element)
        self.elements = initial_list[:] 

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of "
                            "incorrect type to a typed list.") 

    def __setitem__(self, i, element):
        self.__check(element)
        self.elements[i] = element 

    def __getitem__(self, i):
        return self.elements[i]

if __name__ == "__main__": 
    import doctest
    doctest.testmod()


#   doctest traps
#   Because doctests expect a character-by-character match for a successful test, you’ll sometimes find tests failing unexpectedly. In particular, dictionaries aren’t guaranteed to print in a particular order. If you had a test like this
#   >>> my_dict = {'one': 1, 'two': 2} >>> my_dict
#   {'one': 1, 'two': 2}
#   the two items could conceivably print in either order, causing the test to fail unpre- dictably. In cases like this, a direct comparison is more reliable:
#   >>> my_dict == {'one': 1, 'two': 2} True
#   >>> my_dict == {'two': 2, 'one': 1} True
#   
#   for blank lines to be considered part of the output, you need to indicate them with a line containing just <BLANKLINE>, because a blank line is normally a signal to doctest of the end of output.


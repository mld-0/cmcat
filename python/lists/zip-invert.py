
list_input= [[1, 2, 3], [4, 5, 6]]
list_output = list(zip(*list_input)) 
print("list_input=(%s)" % str(list_input))
print("list_output=(%s)" % str(list_output))
#>>     list_input=([[1, 2, 3], [4, 5, 6]])
#>>     list_output=([(1, 4), (2, 5), (3, 6)])


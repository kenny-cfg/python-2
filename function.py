def get_greeting(name):
  return f'Hello {name}'

def function_with_no_return():
  pass

name = "Erika"
greeting = get_greeting(name)
print(greeting)

return_value = function_with_no_return()
print(return_value)

# mypy app6_mypy.py

def myfunction(myparameter: int) -> str: # -> str is return type
    print(myparameter)
    # return f"{myparameter + 10}" # works
    return myparameter + 10 # doesn't work

def otherfunction(otherparamter: str):
    print(otherparamter)

# myfunction("Hello World!") # doesn't work
# myfunction(1) # work

otherfunction(myfunction(1))

def dosth(param: list[int]): # we can even do that
    pass


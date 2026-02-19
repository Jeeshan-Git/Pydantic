from pydantic import validate_call, StrictInt, PositiveInt

@validate_call   # Validate
def add_number(a:StrictInt, b:PositiveInt):
    print(type(a))
    return(a + b)

res = add_number(14,5)
print(res)
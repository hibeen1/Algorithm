import random
def random_List(size, min, max):
    result = []
 
    for v in range(size):
        result.append(random.randint(min, max))
 
    return result

def random_String(size, min, max):
    result = ""

    for v in range(size):
        result += str(random.randint(min, max))
    return result
def average(*args):
    return sum(args) / len(args)

#print(average (10, 20, 30, 40))

def strings_processed(*args):
    args = [x.capitalize() for x in args]
    return sorted(args)

#print(strings_processed('snow', 'glacier', 'iceberg', 'fog'))

def find_sum(**kwargs):
    return sum(kwargs.values())
    
#print(find_sum(a=3, b=6))

def find_max(*args):
    return max(args)

#print(find_max(3, 99, 1001, 2, 8, 2002))

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))


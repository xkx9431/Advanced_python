from functools import wraps

def memo(func):
    cache ={}
    @wraps(func)
    def _wraps(*args,**kwargs):
        key = str(args)+str(kwargs)
        if key not in cache:
            cache[key] = func(*args,**kwargs)
        return cache[key]
    return _wraps
    
@memo
def edit_counts(str1,str2):
    other = {str1:str2,str2:str1}
    for string in other:
        if len(string) == 0:
            return 0
    return min(edit_counts(str1[:-1],str2)+1,
                edit_counts(str2[:-1],str1)+1,
                edit_counts(str1[:-1],str2[:-1])+(0 if str1[-1]==str2[-1] else 2)
    )


def test():
    assert(edit_counts('xkx','xkx1')==1)
    assert(edit_counts('nihao','nihao')==0)
    print('test pass')
test()
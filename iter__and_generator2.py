def gen(k):
    i = 1
    while True :
        yield i**k
        i +=1

gen_1 = gen(1)
gen_3 = gen(3)

def get_sum(n):
    sum_1,sum_3 = 0,0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {},next_3 = {}'.format(next_1,next_3))
        sum_1 += next_1
        sum_3 += next_3

    print(sum_1*sum_1,sum_3)


#get_sum(8)


# 使用迭代器做到列表中查找值

def index_generator(L,target):
    for i,num  in enumerate(L):
        if num == target:
            yield i
print(list(index_generator([1,6,2,4,5,2,8,6,3,2,8,6,3,2],2)))


# 迭代器子序列
def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))



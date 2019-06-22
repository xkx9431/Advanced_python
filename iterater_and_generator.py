def is_iterabale(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


params  = [
    12345,
    '12345',
    [1,2,3,4,5],
    {1:1,2:'w',3:'q'},
    (1,2,3,4)
]




### 生成器

import os
import psutil

# 显示当前python 程序占用的内纯大小

def show_memory_info_(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss/1024./1024
    print('{} memory used:{}MB'.format(hint,memory))


def test_iterator():
    show_memory_info_('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info_('after iterator initiated')
    print(sum(list_1))
    show_memory_info_("after sum called")


def test_generator():
    show_memory_info_('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info_('after generator initiated')
    print(sum(list_2))
    show_memory_info_("after sum called")



def test():
    # for param in params:
    #
    #     print('{} is iterable? \n {}'.format(param,is_iterabale(param)))


#test()

%time test_iterator()
%time test_generator()
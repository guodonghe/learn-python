import time
def count_running_time(func):
    def _count_running_time(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        print ('cost time : {0}'.format(time.time() - start))
        return res
    return _count_running_time
@count_running_time
def test():
    time.sleep(3)
    print ("in the test1")
if __name__ == '__main__':
    test()

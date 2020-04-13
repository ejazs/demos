#Simple and Old method
import threading, time, timeit
import concurrent.futures
start = timeit.default_timer()
def my_func(seconds):
  time.sleep(seconds)
  print(f'Slept for {seconds} seconds')

t1 = threading.Thread(target=my_func, args=[5,])
t2 = threading.Thread(target=my_func, args=[5,])
t1.start()
t2.start()
t1.join()
t2.join()
took = (timeit.default_timer() - start) 
print(took)  

#New style
with concurrent.futures.ProcessPoolExecutor() as executor:
  ex = [1,1]
  results = executor.map(my_func,ex)
  print(results)
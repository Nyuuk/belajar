from time import time
start_time = time()
print(str(time())+'\n'+str(start_time)+'\n'+str((time()-start_time)))
print("--- %s seconds ---" % (time() - start_time))
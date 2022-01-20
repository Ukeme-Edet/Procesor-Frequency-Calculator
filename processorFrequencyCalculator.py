import time, os#, psutil
c = 0
times = 0
for i in range(1000):
    while c <= 1000:
        c += 1
        timess = time.thread_time()
        times += timess
cores = os.cpu_count()
if cores == 1:
    verb = " is "
else:
    verb = " are "
print(f"The number of processor cores {verb} {cores}")
print("And the average processor speed: " + str((1 / (times / 1000) / os.cpu_count())) + " GHz")
#print(psutil.cpu_freq())
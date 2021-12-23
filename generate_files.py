import time
start = time.time()
for x in range(10):
    open("file%03d.txt" % x, "w").write("Test File Generation")
end = time.time()
print(end - start)
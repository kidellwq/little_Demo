# 如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

# step 1,枚举法，把啊，b，c三个数各循环1000次，列出所有的可能
# import time
# start_time = time.time()
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a,b,c:%s,%s,%s" % (a, b, c))
# end_time = time.time()
# print("time:%s" % (end_time-start_time))
# 输出 time:167.75959539413452

# step 2,改进，如果a和b确认了，c=1000-a-b，c的循环就没有必要了
import time
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000-a-b
        if a**2+b**2 == c**2:
            print("a,b,c:%s,%s,%s" % (a, b, c))
end_time = time.time()
print("time:%s" % (end_time-start_time))
# 输出 time:0.9790558815002441

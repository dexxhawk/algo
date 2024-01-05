# n = int(input())
# reply = [0] * n
# topics = [''] * n
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         reply[i] = i
#         topics[i] = input()
#         input()
#     else:
#         reply[i] = reply[num - 1]
#         input()
# cntreplys = {}
# for rep in reply:
#     cntreplys[rep] = cntreplys.get(rep, 0) + 1
# ans = []
# for topic in cntreplys:
#     ans.append((-cntreplys[topic], topic))
# print(topics[min(ans)[1]])
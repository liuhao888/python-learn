num = 10
print("guess what i think?")
answer = int(input())
if answer<num:
    print('小了')
if answer>num:
    print('大了')
if answer==num:
    print('正确')
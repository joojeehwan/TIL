lst = [1,2,2,4,4,5,7,7,2]

cnt_up = 1
maxup_cnt = 1
for i in range(len(lst)-1):
    if lst[i] <= lst[i + 1] :
        cnt_up += 1
    else:
        cnt_up = 1
    if maxup_cnt < cnt_up:
        maxup_cnt = cnt_up

cnt_down = 1
maxdown_cnt = 1
for i in range(len(lst)-1):
    if lst[i] >= lst[i + 1] :
        cnt_down += 1
    else:
        cnt_down = 1
    if maxdown_cnt < cnt_up:
        maxdown_cnt = cnt_up

if maxup_cnt > maxdown_cnt:
    print(maxup_cnt)

else:
    print(maxdown_cnt)
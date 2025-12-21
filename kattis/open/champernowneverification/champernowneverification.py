to_test = input()

chap_num = 0
where = 0
while where < len(to_test):
    chap_num += 1
    str_chap_num = str(chap_num)
    len_str_chap_num = len(str_chap_num)

    if to_test[where:where+len_str_chap_num] != str_chap_num:
        print(-1)
        exit()
    else:
        where += len_str_chap_num

print(chap_num)

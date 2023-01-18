test_status = {
    '김싸피': 'solving',
       '이코딩': 'solving',
       '최이썬': 'cheating',
       '오디비': 'solving',
       '임온실': 'cheating',
       '조실습': 'solving',
       '박장고': 'solving',
       '염자바': 'cheating'
}

print(list(test_status.values()))

for i in list(test_status.keys()):
    # print(i)
    if test_status[i] == 'cheating':
        print(i)
    else:
        continue

# print(test_status)
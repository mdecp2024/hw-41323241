n = 5  # 總共的行數
space = '_'
for i in range(n):  # 對於每一行
    # 印出空格
    print(space * (n - i - 1), end='')  # 在每行前面印出空格
    # 印出星號
    print('*' * (2 * i + 1))  # 每行印出 2*i + 1 個星號
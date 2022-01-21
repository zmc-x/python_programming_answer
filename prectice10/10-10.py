def Read(filename):
    try:
        with open(filename,encoding='utf-8') as f:#当系统的编码和读取的文件的编码的不一致的时，必须定义encoding
            mid = f.read()
    except FileNotFoundError :
        pass
    else:
        mid=mid.lower()
        lists=mid.split()
    return lists

lists=Read('file\\book.txt')
length=lists.count('the ')#'the'&'the '
print(length)


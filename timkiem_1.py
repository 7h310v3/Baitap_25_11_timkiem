import random

def taodulieu(lim, a, b):
    tao = []
    count = 0
    while(count < lim):
        tao.append(int(random.uniform(a, b)))
        count += 1
    return tao

def timkiem(a, tmp):
    ketqua = []
    for i in range(0, len(a)):
        if a[i] == tmp:
            ketqua.append(i)
    if len(ketqua) > 0:
        return ketqua
    else:
        return -1

def main():
    lim = int(input("Nhập số phần tử cần tạo: "))
    a = int(input("Nhập giới hạn dưới: "))
    b = int(input("Nhập giới hạn trên: "))
    num = taodulieu(lim, a, b)

    print("Ban đầu:")
    print(num)

    n = int(input("Nhập số cần tìm kiếm:"))
    KQ = timkiem(num, n)
    if(KQ == -1):
        print("Không có kết quả!")
    else:
        print("Phần tử", n, "xuất hiện đầu tiên tại vị trí: ",KQ[0])

if __name__== "__main__":
    main()
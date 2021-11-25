import random

def taodulieu(lim, a, b):
    tao = []
    count = 0
    while(count < lim):
        tao.append(int(random.uniform(a, b)))
        count += 1
    return tao

def sapxep(x):
    for i in range (0, len(x)-1):
        for j in range (i+1, len(x)):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    return x

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

    print("Dữ liệu của mảng sau khi sắp xếp tăng dần:")
    print(sapxep(num))

    n = int(input("Nhập số cần tìm kiếm:"))
    if(timkiem(sapxep(num), n) == -1):
        print("Không có kết quả!")
    else:
        print("Phần tử", n, "xuất hiện tại vị trí: ",timkiem(sapxep(num), n))

if __name__== "__main__":
    main()
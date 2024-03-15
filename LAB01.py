# Task 1: Enter 4 integers then calculate the average
print("$$ Bài 1: Tính trung bình cộng của 4 số nguyên")
iValue1 = int(input("a = "))
iValue2 = int(input("b = "))
ivalue3 = int(input("c = "))
iValue4 = int(input("d = "))
print(f"-Trung bình cộng: {(iValue1 + iValue2 + ivalue3 + iValue4) / 4}")

# Task 2: Enter 2 integers then caculate the calculate sum, difference, product, quotient
print("$$ Bài 2: Tính tổng, hiệu, tích, thương của 2 số nguyên")
iValue1 = int(input("a = "))
iValue2 = int(input("b = "))
print(
    f"-Tổng: {iValue1 + iValue2} || Hiệu: {iValue1 - iValue2} || Tích: {iValue1 * iValue2} || Thương: {iValue1 / iValue2}")

# Task 3: Enter two positive integers, indicating the result of dividing the integer part and the remainder
print("$$ Bài 3: Tính phần dư và phần nguyên của phép chia")
iValue1 = int(input("a = "))
iValue2 = int(input("b = "))
print(f"-Phần nguyên: {iValue1 // iValue2} || Phần dư: {iValue1 % iValue2}")

# Task 4: Enter a 2-digit positive integer then calculate the sum of the digits
print("$$ Bài 4: Tính tổng các chữ số của số hàng chục")
iValue = int(input("Số hàng chục: "))
print(f"-Tổng các chữ số: {iValue // 10 + iValue % 10}")

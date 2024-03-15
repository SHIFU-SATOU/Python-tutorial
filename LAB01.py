import math
import random

# # Task 1: Enter 4 integers then calculate the average
# print("$$ Bài 1: Tính trung bình cộng của 4 số nguyên")
# iValue1 = int(input("a = "))
# iValue2 = int(input("b = "))
# ivalue3 = int(input("c = "))
# iValue4 = int(input("d = "))
# print(f"-Trung bình cộng: {(iValue1 + iValue2 + ivalue3 + iValue4) / 4}")
#
# # Task 2: Enter 2 integers then caculate the calculate sum, difference, product, quotient
# print("$$ Bài 2: Tính tổng, hiệu, tích, thương của 2 số nguyên")
# iValue1 = int(input("a = "))
# iValue2 = int(input("b = "))
# print(f"-Tổng: {iValue1 + iValue2} || Hiệu: {iValue1 - iValue2} || "
#       f"Tích: {iValue1 * iValue2} || Thương: {round(iValue1 * iValue2, 3)}")
#
# # Task 3: Enter two positive integers, indicating the result of dividing the integer part and the remainder
# print("$$ Bài 3: Tính phần dư và phần nguyên của phép chia")
# iValue1 = int(input("a = "))
# iValue2 = int(input("b = "))
# print(f"-Phần nguyên: {iValue1 // iValue2} || Phần dư: {iValue1 % iValue2}")
#
# # Task 4: Enter a 2-digit positive integer then calculate the sum of the digits
# print("$$ Bài 4: Tính tổng các chữ số của số hàng chục")
# iValue = int(input("Số hàng chục: "))
# print(f"-Tổng các chữ số: {iValue // 10 + iValue % 10}")
#
# # Task 5: Enter the time in hh:mm:ss format then convert it to seconds
# print("$$ Bài 5: Đổi thời gian sang giây")
# sTime = str(input("Thời gian(hh:mm:ss): "))
# lTime = sTime.split(':')
# print(f"-Sau khi đổi sang giây: {int(lTime[0]) * 3600 + int(lTime[1]) * 60 + int(lTime[2])}")
#
# # Task 6: Enter your birth year then calculate your current age
# print("$$ Bài 6: Tính tuổi hiện tại")
# iYearOfBirth = int(input("Năm sinh = "))
# print(f"-Tuổi hiện tại: {2024 - iYearOfBirth}")
#
# # Task 7: Enter the radius of the circle then calculate the circumference and area
# print("$$ Bài 7: Tính chu vi và diện tích hình tròn")
# iRadius = int(input("r = "))
# print(f"-Chu vi hình tròn: {round(2 * math.pi * iRadius, 3)} || "
#       f"Diện tích hình tròn: {round(math.pi * iRadius * iRadius, 3)}")

# # Task 8: Enter weight and height then calculate BMI index
# print("$$ Bài 8: Tính chỉ số sức khỏe BMI")
# fWeight = float(input("Cân nặng(Kg) = "))
# fHeight = float(input("Chiều cao(m) = "))
# print(f"-BMI: {round(fWeight / fHeight, 3)}")

# # Task 9: Print the Food Menu
# print("$$ Bài 9: In Menu món ăn")
# sFrame1 = "============"
# sFrame2 = "=============================="
# print(f"{sFrame1} MENU {sFrame1}\n1. Hu tieu\n2. Chao long\n3. Banh canh\n"
#       f"4. Bun rieu\n5. Pho bo\n{sFrame2}\nMoi nhap lua chon:\n{sFrame2}")

# # Task 10: Enter a 4-digits car license plate then caculate lucky number
# print("$$ Bài 10: Tính nút biển số xe 4 số")
# iCarLicensePlate = int(input("Biển số = "))
# iLuckyNumber = iCarLicensePlate // 1000 + iCarLicensePlate // 100 + iCarLicensePlate // 10 + iCarLicensePlate % 10
# print(f"-Nút của biển số: {iLuckyNumber % 10}")

# # Task 11: Enter lower case then convert to upper case
# print("$$ Bài 11: Chuyển chữ cái in thường sang chữ cái in hoa")
# sLowerCase = str(input("Chữ cái in thường: "))
# print(f"-Chữ cái in hoa: {chr(ord(sLowerCase) - 32)}")

# # Task 12: Random integer number and float number
# print("$$ Bài 12: In số nguyên và số thực ngẫu nhiên")
# print("-[0~100]:")
# print(f"-Số nguyên ngẫu nhiên: {random.randint(0, 100)} || "
#       f"Số thực ngẫu nhiên: {round(random.uniform(0, 100), 2)}")
# print("-[50~99]:")
# print(f"-Số nguyên ngẫu nhiên: {random.randint(50, 99)} || "
#       f"Số thực ngẫu nhiên: {round(random.uniform(50, 99), 2)}")
# print("-[-39~79]:")
# print(f"-Số nguyên ngẫu nhiên: {random.randint(-39, 79)} || "
#       f"Số thực ngẫu nhiên: {round(random.uniform(-39, 79), 2)}")
# print("-[-79~-39]:")
# print(f"-Số nguyên ngẫu nhiên: {random.randint(-79, -39)} || "
#       f"Số thực ngẫu nhiên: {round(random.uniform(-79, -39), 2)}")

# # Task 13: Enter time then convert to other format
# print("$$ Bài 13: Chuyển đổi định dạng thời gian")
# sTime = str(input("Thời gian(dd mm yyyyy): "))
# lTime = sTime.split(' ')
# sTimeFormat1 = '/'.join(lTime)  ##dd/mm/yyyy format
# print(f"-dd/mm/yyyy: {sTimeFormat1}")
# Temp = lTime.copy()
# Temp[-1] = Temp[-1][-2::] ##dd/mm/yy format
# sTimeFormat2 = '/'.join(Temp)
# print(f"-dd/mm/yy: {sTimeFormat2}")
# sTimeFormat3 = '/'.join(lTime[::-1]) ##yyyy/mm/dd format
# print(f"-yyyy/mm/dd: {sTimeFormat3}")
#
# print("-Chuyển đổi về định dạng ban đầu:")
# sTimeFormatOrigin1 = ' '.join(sTimeFormat1.split('/')) ##dd mm yyyy format
# print(f"-dd mm yyyy: {sTimeFormatOrigin1}")
# sTimeFormatOrigin2 = ' '.join(sTimeFormat2.split('/')) ## dd mm yy format
# print(f"-dd mm yy: {sTimeFormatOrigin2}")
# sTimeFormatOrigin3 = ' '.join(sTimeFormat3.split('/')) ## yyyy mm dd format
# print(f"-yyyy mm dd: {sTimeFormatOrigin3}")

# Task 14: Caculate Expression
print(f"A = {round(pow(32, 1 / 5) - pow(1 / 64, -1 / 4) + pow(8 / 27, 1 / 3), 3)}")

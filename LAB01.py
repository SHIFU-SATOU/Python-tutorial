import math
import random
import re

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

# # Task 14: Caculate Expression
# print("$$ Bài 14: Tính toán biểu thức")
# print(f"A = {round(pow(32, 1 / 5) - pow(1 / 64, -1 / 4) + pow(8 / 27, 1 / 3), 3)}")

# # Task 15: Enter 2 numbers then caculate express
# print("$$ Bài 15: Tính toán biểu thức có 2 biến")
# iA = int(input("A = "))
# iB = int(input("B = "))
# fResult = round(((iA + iB) / (iA ** 1 / 2 + iB ** 1 / 2) - (iA * iB) ** 1 / 2) / ((iA ** 1 / 2 - iB ** 1 / 2) ** 2), 3)
# print(fResult)

# # Task 16: Enter time in format hh/mm/ss then convert to seconds
# print("$$ Bài 16: Chuyển đổi định dạng thời gian sang giây")
# sTime = str(input("Thời gian:"))
#
# lTimeNumbers = re.findall(r"[0-9]+", sTime)
# print(f"-Thời gian sau khi đổi ra giây: {int(lTimeNumbers[0]) * 3600 + int(lTimeNumbers[1]) * 60
#                                         + int(lTimeNumbers[2])}s")

# # Task 17: Enter 3 integer numbers then find max and min
# print("$$ Bài 17: Tìm số lớn nhất và nhỏ nhất trong 3 số")
# iList = []
# iList.append(int(input("A = ")))
# iList.append(int(input("B = ")))
# iList.append(int(input("C = ")))
# print(f"-Số lớn nhất: {max(iList)} || số nhỏ nhất: {min(iList)}")

# # Task 18: Enter 2 time points in day then add and subtract these 2 time points
# print("$$ Bài 18: Cộng trừ 2 giờ")
# iTime1 = re.findall(r'[0-9]+', input("Mốc thời gian trong ngày thứ nhất: "))
# iTime2 = re.findall(r'[0-9]+', input("Mốc thời gian trong ngày thứ hai: "))
# print(f"-Khoảng thời gian sau khi cộng: {int(iTime1[0]) + int(iTime2[0])}h"
#       f"{int(iTime1[1]) + int(iTime2[1])}p{int(iTime1[2]) + int(iTime2[2])}s\n"
#       f"-Khoảng thời gian sau khi trừ: {int(iTime1[0]) - int(iTime2[0])}h"
#       f"{int(iTime1[1]) - int(iTime2[1])}p{int(iTime1[2]) - int(iTime2[2])}s")

### BRANCH STRUCTURE

# # Task 19: Enter 4 integer numbers then find min number
# print("$$ Bài 19: Tìm số nhỏ nhất không dùng hàm min")
# iList = []
# iList.append(int(input("A = ")))
# iList.append(int(input("B = ")))
# iList.append(int(input("C = ")))
# iList.append(int(input("D = ")))
# iMin = iList[0]
# for item in iList:
#     if item < iMin:
#         iMin = item
# print(f"-Số nhỏ nhất: {iMin}")

# # Task 20: Enter 4 integer numbers then find max number
# print("$$ Bài 19: Tìm số lớn nhất không dùng hàm max")
# iList = []
# iList.append(int(input("A = ")))
# iList.append(int(input("B = ")))
# iList.append(int(input("C = ")))
# iList.append(int(input("D = ")))
# iMax = iList[0]
# for item in iList:
#     if item > iMax:
#         iMax = item
# print(f"- Số lớn nhất: {iMax}")

# # Task 21: Enter 1 integer number between 1 and 9 then print that number in text format
# print("$$ Bài 21: Chuyển đổi số sang kiểu văn bản")
# dNumbers = {
#     1: 'Mot',
#     2: 'Hai',
#     3: 'Ba',
#     4: 'Bon',
#     5: 'Nam',
#     6: 'Sau',
#     7: 'Bay',
#     8: 'Tam',
#     9: 'Chin'
# }
# print(f"-Dạng văn bản: {dNumbers.get(int(input("Dạng số: ")), "Khong doc duoc")}")

# # Task 22: Solving and arguing first-order equations
# print("$$ Bài 22: Giải và biện luận phương trình bậc nhất")
# iA = int(input("A = "))
# if (iA != 0):
#     iB = int(input("B = "))
#     print(f"-Nghiệm của phương trình: {round(-iB / iA, 2)}")
# else:
#     print("Đây không phải phương trình bậc nhất!")

# # Task 23: Solving and arguing second-order equations
# print("$$ Bài 22: Giải và biện luận phương trình bậc hai")
# iA = int(input("A = "))
#
# if (iA == 0):
#     print(f"-Phương trình vô nghiệm!")
# else:
#     iB = int(input("B = "))
#     iC = int(input("C = "))
#     fDelta = iB ** 2 - 4 * iA * iC
#     print(fDelta)
#     if (fDelta == 0):
#         print(f"-Phương trình có 1 nghiệm: {-iB / (2 * iA)}")
#     elif (fDelta > 0):
#         print(f"-Phương trình có 2 nghiệm phân biệt: x1 = {(-iB + fDelta ** 1 / 2) / (2 * iA)} ||"
#               f"x2 = {(-iB - fDelta ** 1 / 2) / (2 * iA)}")

# # Task 24: Enter hour, time, second then check logic of time
# print("$$ Bài 24: Kiểm tra tính logic của giờ, phút, giây")
# sTime = re.findall(r'[0-9]+', input("Thời gian trong ngày: "))
# if (int(sTime[0]) >= 0 and int(sTime[0]) <= 23 and int(sTime[1]) >= 0
#         and int(sTime[1]) <= 59 and int(sTime[2]) >= 0 and int(sTime[2]) <= 59):
#     print(f"-Thời gian hợp lệ.")
# else:
#     print(f"-Thời gian không hợp lệ!")

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

# # Task 25: Enter 1 character then convert it to upper case or lower case
# print("$$ Bài 25: Nhập vào 1 chữ cái sau đó chuyển về kiểu hoa hoặc thường")
# sCharacter = str(input("Chữ cái cần chyển: "))
# if (ord(sCharacter) >= 65 and ord(sCharacter) <= 90):
#     print(f"-Kiểu thường: {chr(ord(sCharacter) + 32)}")
# if (ord(sCharacter) >= 97 and ord(sCharacter) <= 122):
#     print(f"-Kiểu hoa: {chr(ord(sCharacter) - 32)}")

# # Task 26.1: Enter 3 integer number then sort in ascending order
# print("$$ Bài 26-a: Nhập vào 3 số nguyên, sắp xếp theo thứ tự tăng dần")
# lNumbers = []
# lNumbers.append(int(input(f"A = ")))
# lNumbers.append(int(input(f"B = ")))
# lNumbers.append(int(input(f"C = ")))
# lNumbers.sort()
# print(f"-Dãy số tăng dần: {lNumbers}")

# # Task 26.2: Enter 1 integer number then sort its numbers in ascending order
# sNumber = str(input("N = "))
# lNumbers = []
# for key in sNumber:
#     lNumbers.append(int(key))
# lNumbers.sort()
# sNewNumber = ''
# for key in lNumbers:
#     sNewNumber += str(key)
# print(sNewNumber)

# # Task 27: Enter type of shape, length and width then caculate perimeter and area
# dShapes = {
#     'v': 'vuông',
#     'n': "chữ nhật",
#     't': 'tròn'
# }
# sTypeOfShape = str(input("Nhập hình: "))
# if sTypeOfShape in dShapes:
#     print(f"Tính P và S của hình {dShapes[sTypeOfShape]}")
#     fPerimeter = None
#     fArea = None
#     if (sTypeOfShape == 'v'):
#         iLength = int(input("Nhập chiều dài: "))
#         fPerimeter = 4 * iLength
#         fArea = iLength ** 2
#     elif (sTypeOfShape == 'n'):
#         iWidth = int(input("Nhập chiều rộng: "))
#         iLength = int(input("Nhập chiều dài: "))
#         fPerimeter = 2 * (iWidth + iLength)
#         fArea = iWidth * iLength
#     elif (sTypeOfShape == 't'):
#         iRadius = int(input("Nhập bán kính: "))
#         fPerimeter = round(2 * math.pi * iRadius, 3)
#         fArea = round(math.pi * iRadius ** 2, 3)
# print(f"   Kết quả P = {fPerimeter}    S = {fArea}")

### LOOP STRUTURE
# # Task 28: Enter 1 positive integer number. If that number valid then find all divisors
# print("$$ Bài 28: Tìm ước số")
# iNumber = 0
# while (iNumber <= 0):
#     iNumber = int(input("N = "))
# print(f"-Các ước số của {iNumber}: ", end='')
# for element in range(iNumber + 1):
#     if (element > 0 and iNumber % element == 0):
#         print(element, end=' ')

# # Task 29: Enter 1 positive integer number then sum its numbers
# print("$$ Bài 29: Tính tổng các chữ số")
# sNumber = str(input("N = "))
# iSum = 0
# for element in sNumber:
#     iSum += int(element)
# print(f"-Tổng các chữ số: {iSum}")

# # Task 30: Enter month and year then find number of days in month
# print("$$ Bài 30: In ra số ngày trong tháng")
# dMonths = {
#     1: 31,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
# dFebruary = {
#     True: 29,
#     False: 28
# }
# lTime = re.findall(r'[0-9]+', input("Tháng và năm: "))
# print(f"-Số ngày trong tháng: {dMonths.get(int(lTime[0]), dFebruary.get(int(lTime[1]) % 4 == 0 or (lTime[1][-2:] == '00' and int(lTime[1]) % 400 == 0), False))}")

# # Task 31: Enter 3 width of triangle then find type of triangle
# print("$$ Bài 31: Tìm loại tam giác")
# lWidths = []
# lWidths.append(int(input("a = ")))
# lWidths.append(int(input("b = ")))
# lWidths.append(int(input("c = ")))
# # Check logic of triangle
# isTriangle = lWidths[0] + lWidths[1] > lWidths[2] and lWidths[1] + lWidths[2] > lWidths[0] and lWidths[2] + lWidths[0] > \
#              lWidths[1]
# dInvalidTriangle = {False: "Không phải tam giác!"}
# # Finding of type triangle
# isIsoscelesTriangle = lWidths[0] == lWidths[1] or lWidths[1] == lWidths[2] or lWidths[2] == lWidths[0]
# isRightTriangle = lWidths[0] ** 2 + lWidths[1] ** 2 == lWidths[2] ** 2 or lWidths[1] ** 2 + lWidths[2] ** 2 == lWidths[
#     0] ** 2 or lWidths[2] ** 2 + lWidths[0] ** 2 == lWidths[1] ** 2
# isEquilateralTriangle = lWidths[0] == lWidths[1] and lWidths[1] == lWidths[2]
#
# dIsocelseTriangle = {2: 'Tam giác cân'} #True + True == 2
# dRightTriangle = {2: 'Tam giác vuông'} #True + True == 2
# dEquilateralTriangle = {2: 'Tam giác đều'} #True + True == 2
#
# print(f"-Kết quả kiểm tra: {dRightTriangle.get(isRightTriangle + isRightTriangle, '')}"
#       f"{dIsocelseTriangle.get(isTriangle + isIsoscelesTriangle, '')}"
#       f"{dEquilateralTriangle.get(isTriangle + isEquilateralTriangle, '')}"
#       f"{dInvalidTriangle.get(isTriangle, '')}")

# # Task 32: Enter distance then find taxi tax
# print("$$ Bài 32: Tính tiền taxi")
# fDistance = float(input("Quãng đường đã đi: "))
# # Prices list
# dFirstPrice = {True: 15000}
# dSecondPrice = {True: 13500}
# dThirdPrice = {True: 11000}
# dFourthPrice = {True: 0.1}
# # Check distance
# isLessThan1Km = fDistance <= 1
# isBetween2and5Km = fDistance >= 2 and fDistance <= 5
# isBetween5and119Km = fDistance >= 5
# isGreaterThan120Km = fDistance >= 120
# # Print tax
# print(
#     f"-Giá cước taxi: {round(dFirstPrice.get(isLessThan1Km, dSecondPrice.get(isBetween2and5Km, dThirdPrice.get(isBetween5and119Km))) *
#                              fDistance - dThirdPrice.get(isBetween5and119Km, 0) * fDistance * dFourthPrice.get(isGreaterThan120Km, 0), 2)}đ")

# # Task 33: Enter 1 positive integer number then check it is square number
# print("$$ Bài 33: Kiểm tra số chính phương")
# iNumber = int(input("N = "))
# dSquareNumber = {True: "Số chính phương",
#                  False: "Không phải số chính phương!"}
# isSquareNumber = iNumber ** 1 / 2 % 1 == 0
# print(f"-Kết quả kiểm tra: {dSquareNumber.get(isSquareNumber)}")

# # Task 34: Enter 1 positive integer number then check prime number
# print("$$ Bài 34: Kiểm tra số nguyên tố")
# iNumber = int(input("N = "))
# # Count divisors of number
# dDivisor = {
#     True: 1,
#     False: 0
# }
# iCount = 0
# for element in range(1, iNumber + 1):
#     iCount += dDivisor.get(iNumber % element == 0)
# # Check prime number
# dPrimeNumber = {True: "Số nguyên tố.",
#                 False: "Không phải số nguyên tố!"}
# isPrimeNumber = iCount == 2
# print(f"-Kết quả kiểm tra: {dPrimeNumber.get(isPrimeNumber)}")

# # Task 35: Enter n then caculate express S = 1 + 2 + 3 + ... + n(n is positive integer number)
# print("$$ Bài 35: Tính biểu thức S = 1 + 2 + 3 + ... + n")
# iLastNumber = int(input("N = "))
# iSum = 0
# for element in range(1, iLastNumber + 1):
#     iSum += element
# print(f"-S = {iSum}")

# # Task 36: Enter n then caculate express S = 1**2 + 2**2 + 3**2 + ... + n**2(n is positive integer number)
# print("$$ Bài 36: Tính biểu thức S = 1**2 + 2**2 + 3**2 + ... + n**2")
# iLastNumber = int(input("N = "))
# iSum = 0
# for element in range(1, iLastNumber + 1):
#     iSum += element ** 2
# print(f"-S = {iSum}")

# # Task 37: Enter n then caculate express S = 2 + 4 + 6 + ... + n (n is positive even number)
# print("$$ Bài 37: Tính biểu thức S = 2 + 4 + 6 + ... + n")
# # Check even number
# iLastNumber = int(input("N = "))
# isOddNumber = iLastNumber % 2 != 0
# while (isOddNumber):
#     print("Vui lòng nhập số chẵn!")
#     iLastNumber = int(input("N = "))
#     isOddNumber = iLastNumber % 2 != 0
# iSum = 0
# # Caculating express
# for element in range(2, iLastNumber + 1, 2):
#     iSum += element
# print(f"-S = {iSum}")

# # Task 38: Enter n then caculate express S = 1 * 2 * 3 * ... * n (n is positive odd number)
# print("$$ Bài 38: Tính biểu thức S = 1 * 2 * 3 * ... * n")
# # Check odd number
# iLastNumber = int(input("N = "))
# isEvenNumber = iLastNumber % 2 == 0
# while(isEvenNumber):
#     print("Vui lòng nhập số lẻ!")
#     iLastNumber = int(input("N = "))
#     isEvenNumber = iLastNumber % 2 == 0
# iProduct = 1
# # Caculate express
# for element in range(1, iLastNumber + 1):
#     iProduct *= element
# print(f"-S = {iProduct}")

# # Task 39: Enter n then caculate express S = 1 + 1/2 + 1/3 + ... + 1/n
# print("$$ Bài 39: Tính biểu thức S = 1 + 1/2 + 1/3 + ... + 1/n")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(1, iLastNumber + 1):
#     fSum += 1 / element
# print(f"-S = {round(fSum, 3)}")

# # Task 40: Enter n then caculate express S = 1/2 + 1/4 + ... + 1/2n
# print("$$ Bài 40: Tính biểu thức S = 1/2 + 1/4 + ... + 1/2n")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(1, iLastNumber + 1):
#     fSum += 1 / 2 * element
# print(f"-S = {round(fSum, 3)}")

# # Task 41: Enter n then caculate express S = 1 + 1/3 + 1/5 + ... + 1/(2n + 1)
# print("$$ Bài 41: Tính biểu thức S = 1 + 1/3 + 1/5 + ... + 1/(2n + 1)")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(1, iLastNumber + 1):
#     fSum += 1 / (2 * element + 1)
# print(f"-S = {round(fSum, 3)}")

# # Task 42: Enter n then caculate express S = 1/(1 * 2) + 1/(2 * 3) + ... + 1/(n * (n + 1))
# print("$$ Bài 42: Tính biểu thức S = 1/(1 * 2) + 1/(2 * 3) + ... + 1/(n * (n + 1))")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(1, iLastNumber + 1):
#     fSum += 1 / (element * (element + 1))
# print(f"-S = {round(fSum, 3)}")

# # Task 43: Enter n then caculate express S = 1/2 + 2/3 + ... + n/(n+1)
# print("$$ Bài 43: Tính biểu thức S = 1/2 + 2/3 + ... + n/(n+1)")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(1, iLastNumber + 1):
#     fSum += element / (element + 1)
# print(f"-S = {round(fSum, 3)}")

# # Task 44: Enter n then caculate express S = 1/2 + 3/4 + ... + (2 * n + 1)/(2 * n + 2)
# print("$$ Bài 44: Tính biểu thức S = 1/2 + 3/4 + ... + (2 * n + 1)/(2 * n + 2)")
# iLastNumber = int(input("N = "))
# fSum = 0
# for element in range(iLastNumber + 1):
#     fSum += (2 * element + 1) / (2 * element + 2)
# print(f"-S = {round(fSum, 3)}")

# # Task 45: Enter n and x then caculate express S = x + x ** 2 / (1 + 2) + x ** 3 / (1 + 2 + 3) + ... + x ** n / (1 + 2 + 3 + ... + n)
# print(
#     "$$ Bài 45: Tính biểu thức S = x + x ** 2 / (1 + 2) + x ** 3 / (1 + 2 + 3) + ... + x ** n / (1 + 2 + 3 + ... + n)")
# iLastNumber = int(input("N = "))
# iX = int(input("X = "))
# fSum = 0
# iTotalDenominator = 0
# for element in range(1, iLastNumber + 1):
#     iTotalDenominator += element
#     fSum += iX ** element / iTotalDenominator
# print(f"-S = {round(fSum, 3)}")

# # Task 46: Find all integer root of equation 2 * x + 7 * y + 9 * z = 979
# print("$$ Bài 46: Tìm bộ nghiệm nguyên của phương trình 2 * x + 7 * y + 9 * z = 979")
# for x in range(980):
#     for y in range(980):
#         for z in range(980):
#             if (2 * x + 7 * y + 9 * z == 979):
#                 print(f"{x} {y} {z}")

# # # Task 47: Find all integer root of equation 2 * x + 7 * y + 9 * z = 979 then find largest total of x, y, z
# # print("$$ Bài 47: Tìm bộ nghiệm nguyên của phương trình 2 * x + 7 * y + 9 * z = 979 và tổng x, y, z lớn nhất")
# iLargestTotal = 0
# lNumbersWithLargestTotal = [0, 0, 0]
# for x in range(980):
#     for y in range(980):
#         for z in range(980):
#             if (2 * x + 7 * y + 9 * z == 979):
#                 if (x + y + z > iLargestTotal):
#                     iLargestTotal = x + y + z
#                     lNumbersWithLargestTotal = [x, y, z]
#                 print(f"{x} {y} {z}")
# print(f"- {lNumbersWithLargestTotal} là bộ nghiệm có tổng lớn nhất. {lNumbersWithLargestTotal[0]} + "
#       f"{lNumbersWithLargestTotal[1]} + {lNumbersWithLargestTotal[2]} = {iLargestTotal}")
#
# # Task 48: Find all integer root of equation 2 * x + 7 * y + 9 * z = 979 then find smallest total of x, y, z
# print("$$ Bài 48: Tìm bộ nghiệm nguyên của phương trình 2 * x + 7 * y + 9 * z = 979 và tổng x, y, z nhỏ nhất")
# iSmallestTotal = 979
# lNumbersWithSmallestTotal = [0, 0, 0]
# for x in range(980):
#     for y in range(980):
#         for z in range(980):
#             if (2 * x + 7 * y + 9 * z == 979):
#                 if (x + y + z < iSmallestTotal):
#                     iSmallestTotal = x + y + z
#                     lNumbersWithSmallestTotal = [x, y, z]
#                 print(f"{x} {y} {z}")
# print(f"- {lNumbersWithSmallestTotal} là bộ nghiệm có tổng nhỏ nhất. {lNumbersWithSmallestTotal[0]} + "
#       f"{lNumbersWithSmallestTotal[1]} + {lNumbersWithSmallestTotal[2]} = {iSmallestTotal}")

### FUNCTION

# # Task 49: Checking number is even negative number
# print("$$ Bài 49: Kiểm tra số âm chẵn")
#
#
# def checkingEvenNegativeNumber(iNumber: int) -> bool:
#     return iNumber % 2 == 0 and iNumber < 0
#
#
# iNumber = int(input("N = "))
# print(f"-Kết quả kiểm tra: {checkingEvenNegativeNumber(iNumber)}")

# # Task 50: Checking number is odd negative number
# print("$$ Bài 50: Kiểm tra số âm lẻ")
#
#
# def checkingOddNegativeNumber(iNumber: int) -> int:
#     dOddNegativeNumber = {True: -1}
#     dEvenPositiveNumber = {True: 1}
#     isOddNegativeNumber = iNumber % 2 != 0 and iNumber < 0
#     isEvenPositiveNumber = iNumber % 2 == 0 and iNumber > 0
#     iResult = dOddNegativeNumber.get(isOddNegativeNumber, dEvenPositiveNumber.get(isEvenPositiveNumber, 0))
#     return iResult
#
#
# iNumber = int(input("N = "))
# print(f"-Kết quả kiểm tra: {checkingOddNegativeNumber(iNumber)}")

# # Task 51: Checking value in range [-89, 90]
# print("$$ Bài 51: Kiểm tra giá trị trong khoảng")
#
#
# def checkingValueInRange():
#     iNumber = int(input("N = "))
#     while (iNumber < -89 or iNumber > 90):
#         iNumber = int(input("N = "))
#
#
# checkingValueInRange()

# # Task 52:
# print("$$ Bài 52:")
# iNumber = int(input("N = "))
#
# # a) Caculating x root of number
#
# iRoot = int(input("Căn bậc x = "))
#
#
# def caculatingXRoot(iNumber: int, iRoot):
#     return round(iNumber ** 1 / iRoot, 3)
#
#
# print(f"-Căn bậc {iRoot} của {iNumber} bằng {caculatingXRoot(iNumber, iRoot)}")
#
#
# # b) ReversingNumber
# def reversingNumber(iNumber: int):
#     return int("".join(reversed(str(iNumber))))
#
#
# print(f"-Số sau khi đảo ngược: {reversingNumber(iNumber)}")
#
#
# # c) Checking square number
# def checkingSquareNumber(iNumber: int):
#     return iNumber ** 1 / 2 % 1 == 0
#
#
# print(f"-Kết quả kiểm tra số chính phương: {checkingSquareNumber(iNumber)}")
#
#
# # d) Checking prime number
# def checkingPrimeNumber(iNumber: int):
#     # Count divisors of number
#     dDivisor = {
#         True: 1,
#         False: 0
#     }
#     iCount = 0
#     for element in range(1, iNumber + 1):
#         iCount += dDivisor.get(iNumber % element == 0)
#     # Check prime number
#     isPrimeNumber = iCount == 2
#     return isPrimeNumber
#
#
# print(f"-Kết quả kiểm tra số nguyên tố: {checkingPrimeNumber(iNumber)}")
#
#
# # e) Caculating product of odd numbers
# def multiplyingOddNumbers(iNumber: int) -> int:
#     iProductOfOddNumbers = 1
#     for number in range(1, len(str(iNumber)) + 1):
#         if (int(number) % 2 != 0):
#             iProductOfOddNumbers *= int(number)
#     return iProductOfOddNumbers
#
#
# print(f"-Tích của các chữ số lẻ: {multiplyingOddNumbers(iNumber)}")
#
#
# # f) Caculating total of prime numbers is smaller n
# def summingPrimeNumbersSmallerN(iNumber: int) -> int:
#     iTotalOfPrimeNumbers = 0
#     for number in range(iNumber):
#         if (checkingPrimeNumber(number)):
#             iTotalOfPrimeNumbers += number
#     return iTotalOfPrimeNumbers
#
#
# print(f"-Tổng các số nguyên tố nhỏ hơn {iNumber}: {summingPrimeNumbersSmallerN(iNumber)}")
#
#
# # g) Caculating total of square numbers is smaller n
# def summingSquareNumbersSmallerN(iNumber: int) -> int:
#     iTotalOfSquareNumbers = 0
#     for number in range(iNumber):
#         if (checkingSquareNumber(number)):
#             iTotalOfSquareNumbers += number
#     return iTotalOfSquareNumbers
#
#
# print(f"-Tổng các số chính phương nhỏ hơn {iNumber}: {summingSquareNumbersSmallerN(iNumber)}")
#
#
# # h) Caculating total of positve divisors
# def summingPositiveDivisors(iNumber: int) -> int:
#     iTotalOfPositiveDivisors = 0
#     for number in range(1, iNumber + 1):
#         if (iNumber % number == 0 and number > 0):
#             iTotalOfPositiveDivisors += number
#     return iTotalOfPositiveDivisors
#
#
# print(f"-Tổng các ước số dương của {iNumber}: {summingPositiveDivisors(iNumber)}")

# # Task 53: Enter 1 positive integer number then caculate follows methods:
# print("$$ Bài 53: Nhập N sau đó tính các biểu thức sau")
# iNumber = int(input("N = "))
#
#
# # a) S = 1 + 2 + 3 + ... + n
# def summingIncreasingIntegerSmallerN(iNumber):
#     iTotal = 0
#     for number in range(iNumber + 1):
#         iTotal += number
#     return iTotal
#
#
# print(f"-Tổng các số nguyên tăng dần nhỏ hơn {iNumber}: {summingIncreasingIntegerSmallerN(iNumber)}")
#
#
# # b) S = 12 + 22 + 32 + ... + n * 10 + 2
# def caculatingExpression2(iNumber: int) -> int:
#     iTotal = 0
#     for number in range(1, iNumber + 1):
#         iTotal += number * 10 + 2
#     return iTotal
#
#
# print(f"- S = 12 + 22 + 32 + ... + n * 10 + 2 = {caculatingExpression2(iNumber)}")
#
#
# # c) S = 1 + 1/2 + 1/3 + ... + 1/n
# def caculatingExpression3(iNumber: int) -> float:
#     iTotal = 0
#     for number in range(1, iNumber + 1):
#         iTotal += 1 / number
#     return round(iTotal, 3)
#
#
# print(f"- S = 1 + 1/2 + 1/3 + ... + 1/n = {caculatingExpression3(iNumber)}")
#
#
# # d) S = 1! + 2 ! + 3! + ... + n!
# def caculatingFactorial(iNumber: int) -> int:
#     if (iNumber == 0):
#         return 1
#     else:
#         iProduct = 1
#         for number in range(1, iNumber + 1):
#             iProduct *= number
#         return iProduct
#
#
# def caculatingExpress4(iNumber: int) -> float:
#     iTotal = 0
#     for number in range(1, iNumber + 1):
#         iTotal += caculatingFactorial(number)
#     return iTotal
#
#
# print(f"- S = 1! + 2! + 3! + ... + n! = {caculatingExpress4(iNumber)}")
#
#
# # e) S = 1 * 2 * 3 * ... * n
# def caculatingExpress5(iNumber: int) -> int:
#     iProduct = 1
#     for number in range(1, iNumber + 1):
#         iProduct *= number
#     return iProduct
#
#
# print(f"- S = 1 * 2 * 3 * ... * n = {caculatingExpress5(iNumber)}")

# # Task 54: Enter n then find n Fibonacci numbers
# print("$$ Bài 54: In ra n số Fibonacci")
# iSize = int(input(" N = "))
#
#
# def findTheNthFibonacciNumber(iNth: int) -> int:
#     if iNth == 0:
#         return 0
#     elif iNth == 1:
#         return 1
#     else:
#         return findTheNthFibonacciNumber(iNth - 1) + findTheNthFibonacciNumber(iNth - 2)
#
#
# def findNFibonacciNumbers(iSize: int):
#     for index in range(1, iSize + 1):
#         print(findTheNthFibonacciNumber(index), end=' ')
#
#
# print("-Dãy số Fibonacci: ", end=' ')
# findNFibonacciNumbers(iSize)

# # Task 55: Enter length and width of rectangle then caculate perimeter and area. After caculate, draw rectangel with *
# print("$$ Bài 55: Tính chu vi và diện tích hình chữ nhật, sau đó vẽ bằng ký tự *")
# iLength = int(input("Chiều dài = "))
# iWidth = int(input("Chiều rộng  = "))
#
#
# def caculatingPerimeterOfRectangle(iLength: int, iWidth: int) -> int:
#     return 2 * (iLength + iWidth)
#
#
# def caculatingAreaOfRectangle(iLength: int, iWidth: int) -> int:
#     return iLength * iWidth
#
#
# def drawRectangle(iLength: int, iWidth: int):
#     for index1 in range(iWidth):
#         print()
#         for index2 in range(iLength):
#             if (index1 == 0 or index1 == iWidth - 1 or index2 == 0 or index2 == iLength - 1):
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#
#
# print(f"-Chu vi hình chữ nhật: {caculatingAreaOfRectangle(iLength, iWidth)}")
# print(f"-Diện tích hình chữ nhật: {caculatingPerimeterOfRectangle(iLength, iWidth)}")
# drawRectangle(iLength, iWidth)


# Task 56: Apply kwargs, *args, **args techniques to design functions to calculate perimeter and area of squares,
# rectangles, circles
print("$$ Bài 56: Áp dụng kỹ thuật kwargs, *args, **args để thiết kế hàm tính chu vi, "
      "diện tích của hình chữ nhật, hình vuông, hình tròn")


def caculatingPerimeterAndAreaOfRectangleSquareCircle(*iSizes, **ShapesAndMethods):
    if (ShapesAndMethods.get('hinh') == 'chu_nhat' and ShapesAndMethods.get('tinh') == 'cv'):
        return 2 * (iSizes[0] + iSizes[1])
    if (ShapesAndMethods.get('hinh') == 'chu_nhat' and ShapesAndMethods.get('tinh') == 'dt'):
        return iSizes[0] * iSizes[1]
    if (ShapesAndMethods.get('hinh') == 'vuong' and ShapesAndMethods.get('tinh') == 'cv'):
        return iSizes[0] * 4
    if (ShapesAndMethods.get('hinh') == 'vuong' and ShapesAndMethods.get('tinh') == 'dt'):
        return iSizes[0] ** 2
    if (ShapesAndMethods.get('hinh') == 'tron' and ShapesAndMethods.get('tinh') == 'cv'):
        return round(2 * math.pi * iSizes[0], 3)
    if (ShapesAndMethods.get('hinh') == 'tron' and ShapesAndMethods.get('tinh') == 'dt'):
        return round(math.pi * iSizes[0] ** 2, 3)


iLength = 10
iWidth = 6
iRadius = 3
print(f"-Chu vi hình chữ nhật có chiều dài {iLength} và chiều rộng {iWidth}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='chu_nhat', tinh='cv')}")
print(f"-Diện hình chữ nhật có chiều dài {iLength} và chiều rộng {iWidth}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='chu_nhat', tinh='dt')}")
print(f"-Chu vi hình vuông có chiều dài {iLength}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='vuong', tinh='cv')}")
print(f"-Diện tích hình vuông có chiều dài {iLength}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='vuong', tinh='dt')}")
print(f"-Chu vi hình tròn có bán kính {iRadius}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='tron', tinh='cv')}")
print(f"-Chu vi hình tròn có bán kính {iRadius}: "
      f"{caculatingPerimeterAndAreaOfRectangleSquareCircle(iLength, iWidth, hinh='tron', tinh='dt')}")

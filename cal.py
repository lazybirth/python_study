

# 두개의 숫자로 사칙연산하고 출력 + - / * % 
# print("더하기 : ",result)
# print("뺴기 : ", result)

while(True):
    num1 = int(input("첫번째 숫자 입력 : "))
    sign = input("기호 입력(끝내고 싶으면 q 입력) : ")
    if(sign == 'q'):
        print("q입력으로 끝낼꺼임")
        break
    num2 = int(input("두번째 숫자 입력 : "))

    if (sign == '+'):
        result = num1 + num2
        print("더하기", result)

    elif(sign == '-'):
        result = num1 - num2
        print("빼 기", result )

    elif(sign == '/'):
        result = num1 / num2
        print("나누기", result)

    elif(sign == '*'):
        result = num1 * num2
        print("곱하기", result)

    elif(sign == '%'):
        result = num1 % num2
        print("나머지", result)

    elif(sign == '//'):
        result = num1 // num2
        print("몫", result)

    else:
        print("그 냥 니가 ㅅ=잘못함")



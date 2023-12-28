# 한 줄 주석 (command + /)
# 설명글을 작성하기 위해 사용
# 지금 당장 사용하지 않는 코드에 사용한다.


'''
    범위 주석
'''

"""
# 이름을 출력하는 부분
print('장태훈')

# 나이를 출력하는 부분
print('20살')
"""


#제어 문자
# 반드시 "" 안에 작성한다.
# 줄바꿈: \n
print('장태훈\n20살')
# 위 아래 간격 맞춰 띄우기: \t
print('이름:\t장태훈')
print('나이:\t20살')


# 출력 함수
# end: 출력할 값 마지막에 붙일 문자 설정
print("저는 ", end="")
print("장태훈입니다.")
# sep: 값과 값 사이에 들어갈 문자 설정
print('안녕', '반가워', sep=', ')
# 출력함수는 사용자가 아닌 개발자를 위한 도구이다.
# 오류를 구체화할 때 사용한다.
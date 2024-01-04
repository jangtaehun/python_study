# keyword argument

def introduce(**intro):
    print(intro)
    print(type(intro))
    print(f'name: {intro["name"]}')


introduce(name="John")
#   {'name': 'John'}
#   <class 'dict'>
#   name: John
introduce(**{'name':'ddeock'})
"""
info_dict = {
    'name':'zzone'
}
introduce(**info_dict)
"""

"""
#주문 가격과 주문한 회원의 정보 출력
def order_info(*args, **kwargs):
    total = 0
    for i in args:
        total += i

    print(f'{kwargs["name"]}님의 총 주문 가격: {total}원')

order_info(3000, 2000, 3000, 4000, name='zzoneddeock')
"""

#국어, 영어, 수학 점수의 평균 구하기
#kwargs를 사용
def total_average(*args, **kwargs):
    '''
    주문 총 가격과 주문한 회원의 정보 출력
    :param args: 점수
    :param kwargs: 이름
    :return:
    '''
    total = 0
    for i in args:
        total += i
    ave = total / len(args)
    print(f'zzoneddeock이의 총 점: {ave}, 평균: {total}')
total_average(98, 45, 26, 95, 22, name='zzoneddeock')
help(total_average)


def total_average1(**kwargs):
    total = 0
    for i in kwargs:
        total += kwargs[i]
    ave = total / len(kwargs)
    print(f'zzoneddeock이의 총 점: {ave}, 평균: {total}')
    """
    kor = kwargs['kor']
    eng = kwargs['eng']
    math = kwargs['math']
    return (kor + eng + math) / 3
    total_average(kor=60, eng=93, math=52)
    """
total_average1(zzone=60, ddeock=90)


#사용자가 원하는 자리수(round)에서 반올림해준다.
#자리수를 받지 않았다면 기본값을 리턴한다.
def total_average2(**kwargs):
    if "round" in kwargs:
        kor, eng, math = kwargs.get('kor'), kwargs.get('eng'), kwargs.get('math')
        total = kor + eng + math
        avg = total / 3
        if 'round' in kwargs:
            return round(avg, kwargs['round'])
        return avg

total_average2(kor=60, eng=93, math= 62, round=2)

"""
def average(kor, eng, math):
    return (kor + eng + math) / 3
print(average(60, 93, 52))

#반드시 key와 함께 사용하고자 할 때는 매개변수의 시작을 *로 한다.
def average(*, kor, eng, math):
    return (kor + eng + math) / 3
print(average(kor=60, eng=93, math=52))
"""
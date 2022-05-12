# 프로그레머스 코딩테스트 연습 - 숫자 문자열과 영단어
# dictionary 사용
# replace 함수를 이용한 문자열 치환
# 에러사항 - replace 함수를 알기전 index함수를 이용해 테스트케이스의 문자열의 영단어의 인덱스를 확인하고, 인덱스를 치환할려고 시도함.

def solution(s):
    strToNum = {'zero':0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}  # dict 구조
    answer = s
    for i in strToNum:
        answer = answer.replace(i,str(strToNum[i]))
        
    return int(answer)

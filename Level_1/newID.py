# new_id = "...!@BaT#*..y.abcdefghijklm"

import string

def solution(new_id):

    lower_new_id = new_id.lower()
    
    new_symbols = string.punctuation.replace('-','').replace('_','').replace('.','')

    for i in new_symbols:
        if i in lower_new_id:
            lower_new_id = lower_new_id.replace(i,'')

    lower_new_id_list = list(lower_new_id)
    pop_dot = []

    for i in range(0,len(lower_new_id_list)):
        if lower_new_id_list[i] == '.':
            try:
                if lower_new_id_list[i] == lower_new_id_list[i+1]:
                    pop_dot.append(i)
            except:
                pass

    pop_dot = list(reversed(pop_dot))
    # pop이 되고 나면 index의 위치가 꼬임 >> 리스트를 역순서로 뒤에부터 제거할 수 있도록 수정
    for i in pop_dot:
        lower_new_id_list.pop(i)

    #list를 문자열로 재생성
    lower_new_id = ''.join(s for s in lower_new_id_list)
    lower_new_id = lower_new_id.replace(' ','')

    lower_new_id = lower_new_id.strip('.')
    
    if lower_new_id == '' or lower_new_id == None:
        lower_new_id = "a"
        
    if len(lower_new_id) >= 16:
        lower_new_id = lower_new_id[:15]
    
    lower_new_id = lower_new_id.rstrip('.')
    
    if len(lower_new_id) <= 2:
        while True:
            lower_new_id += lower_new_id[(len(lower_new_id)-1)]
            if len(lower_new_id) == 3:
                break

    answer = lower_new_id
    print(answer)
    return answer

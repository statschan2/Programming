# 단어
w = input()

# 크로아티아 알파벳 리스트
c_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 크로아티아 알파벳 하나씩 추출
for s in c_alphabet :
    # 추출한 크로아티아 알파벳이 단어에 있는지 확인
    if s in w :
        # 있다면 임의의 'x' 문자로 변환
        w = w.replace(s,'x')

# 알파벳 개수 확인
print(len(w))
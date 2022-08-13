import random

def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__" :
    data = [1,2,3,4,5]
    while data : print(random_pop(data))


# main이 있으므로 이 스크립트를 실행할 수 있다.(자바와 동일)
# 실행방법1) ctrl +f5(디버깅없이 실행)
# 실행방법2) 터미널에서 python random_pop.py
# 실행방법3) 주피터에서 os.system("python random_pop.py") / 결과 보고 싶다면 os.popen("").read()
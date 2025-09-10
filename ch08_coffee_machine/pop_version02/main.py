MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    },
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}

logo = '''              _____  _____              
  ____  _____/ ____\/ ____\____   ____  
_/ ___\/  _ \   __\\   __\/ __ \_/ __ \ 
\  \__(  <_> )  |   |  | \  ___/\  ___/ 
 \___  >____/|__|   |__|  \___  >\___  >
     \/                       \/     \/ '''

def is_resources_enough(
        order_ingredient):  # 만약에 특정 함수/메서드의 결과값이 boolean이라면 대개 다음 조건문/반복문의 조건식으로 쓰이는 경우가 많습니다. 함수형 프로그래밍 개념을 떠올리시면 됩니다.
    for item in order_ingredient:  # order_ingredient의 자료형은 무엇이고, 그 근거는 ?
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True


def process_coins():
    sum = 0
    sum += float(input('쿼터 동전을 몇개나 넣으시겟습니까? >>>')) * 0.25
    sum += float(input('다임 동전을 몇개나 넣으시겟습니까? >>>')) * 0.1
    sum += float(input('니켈 동전을 몇개나 넣으시겟습니까? >>>')) * 0.05
    sum += float(input('페니 동전을 몇개나 넣으시겟습니까? >>>')) * 0.01
    return sum

def is_transaction_successful(money_received, drink_cost):
    change = money_received - drink_cost
    if change >= 0:
        global profit  # 전역 변수인 profit을 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost  # 근데 함수 호출을 통한 전역 변수의 값 변화는 권장하지 않습니다.
        print(f'잔돈 ${change}을(를) 반환합니다.')
        return True  # 그래야 음료 제조 과정의 조건식으로 쓸 수 있으니까요
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False  # 얘는 음료 제조 과정의 조건식으로 쓰이더라도 실행이 안되겠네요

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f'{drink_name}이(가) 나왔습니다. 맛있게 드세요 !!')

is_on = True
while is_on:
    print(logo)
    choice = input('어떤 음료를 드시겠습니까? (에스프레스 / 라떼 / 카푸치노) >>>')
    if choice == 'off':
        is_on = False
        print('자판기가 종료되었습니다.')
    elif choice == 'report':
        print(f'물 : {resources['물']}')
        print(f'우유 : {resources['우유']}')
        print(f'커피 : {resources['커피']}')
        print(f'수익 : ${profit}')
    elif choice in ('에스프레소', '라떼', '카푸치노'):
        drink = MENU[choice]                            # 세 번 나와서 refactoring 예시로 남겨두겠습니다.
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                make_coffee(drink_name=choice, order_ingredient=drink['재료'])
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요.')
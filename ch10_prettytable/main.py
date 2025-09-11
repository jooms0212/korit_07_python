'''
외부 패키지의 설치 # 1 : settings를 통한 방법
메뉴 -> file -> settings -> 좌측에 project: 프로젝트명 으로 되어잇는 부분 클릭
-> python interpreter 클릭 -> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 # 2 : 터미널을 이용한 방법
pip install prettytable

'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['번호', '이름', '타입']
for pokemon in pokemon_data:
    table.add_row(pokemon)
# 아래의 코드는 17~18 코드와 동일하게 결과값이 나옵니다
# table.add_rows(pokemon_data)

print(table)

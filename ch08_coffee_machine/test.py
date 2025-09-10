#
# phone = input('전화번호를 입력하세요 >>>')
# if len(phone)!= 13 :
#     print(f'{phone} 유효하지 않은 전화번호 형식입니다.')
# else:
#     mid = phone[4:8]
#     print(f'{phone} 전화번호의 중간 4자리는 {mid}입니다.')

# li=[0,1,2,3,4,5,6,7,8,9,10]
# result = "".join(map(str, li))
# print(result)


# class Student():
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = {}
#
#     def add_grade(self, subject, score):
#         self.grades[subject] = score
#
#     def get_average_grade (self):
#         if not self.grades:
#             return 0
#         total = sum(self.grades.values())
#         return total / len(self.grades)
#
#     def print_grades(self):
#         print(f'학생이름: {self.name} \n 평균성적: {self.get_average_grade():.2f}')
#
#
# student1 = Student("김일", "12345")
# student1.add_grade('수학', 90)
# student1.add_grade('영어', 80)
# student1.add_grade('국어', 72)
# student1.print_grades()


# pos_count = 0
# neg_count = 0
# zero_count = 0
# numbers = []
# num = int(input('몇 개의 숫자를 입력하시겠습니까? >>>'))
# for i in range(num):
#     number = int(input(f'{i+1}번째 숫자를 입력하시오 >>>'))
#     numbers.append(number)
#     if number > 0:
#         pos_count += 1
#     elif number < 0:
#         neg_count += 1
#     else:
#         zero_count += 1
# print(f'양수: {pos_count}개')
# print(f'음수: {neg_count}개')
# print(f'0: {zero_count}개')


votes = {}
candidates = []
result = {}
num = int(input('후보자 수를 입력하시오 >>>'))
for i in range(num):
    name = input(f'{i+1}번째 후보자의 이름을 입력하시오 >>>')
    candidates.append(name)
    votes[i+1] = name
    result[i+1] = 0


num_votes = int(input('전체 투표 횟수를 입력하시오 >>>'))
for i in range(num_votes):
    candidate_num = int(input(f'{i + 1}번째 투표{votes} >>>'))
    if 1 <= int(candidate_num) <= num:
        result[candidate_num] += 1
    else:
        print('잘못된 번호입니다. 무효처리합니다.')

print("--- 투표 결과 ---")

for candidate_num, count in result.items():
    candidate_name = votes[candidate_num]
    print(f'{candidate_name}: {count}표')


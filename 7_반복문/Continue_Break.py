# continue 와 break

absent=[2,5] # 결석
no_book=[7] # 책을 놓고 옴

for student in range(1,11):
    if student in absent:
        continue # 아래 문장 실행하지 않고 조건 검사로 이동
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 가장 가까운 반복문 탈출
    print("{0}, 책을 읽어줘".format(student))

scores=[90,85,77,65,97] # 학생들 성적
cheated_student_list={2,4} # 부정행위 학생(2번째, 4번째)

for i in range(5):
    if i+1 in cheated_student_list: # i는 0부터 시작하므로 i+1로 해야 2번째, 4번째 학생은 제외함
        continue
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")




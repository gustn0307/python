from random import *

class Unit: # 일반 유닛
    def __init__(self, name, hp, speed):  # __init__ => 파이썬에서 생성자
        self.name = name
        self.hp = hp
        self.speed=speed
        print("{} 유닛이 생성 되었습니다".format(name))

    def move(self, location):
        print("{} 유닛이 {} 방향으로 이동합니다 [속도 {}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):  # 공격 유닛, 일반 유닛을 상속받음
    def __init__(self, name, hp, speed, damage):  # __init__ => 파이썬에서 생성자
        Unit.__init__(self,name,hp, speed)
        self.damage = damage

    # self는 자기 자신을 의미하고 클래스 내에서 메소드 안에는 항상 self를 적어주어야 한다.
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다 [공격력 {}]".format(
            self.name, location, self.damage))

class Flyable: # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed=flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp, 0, damage) # 지상 속도(speed)는 0
        Flyable.__init__(self,flying_speed)

    def move(self, location): # 메소드 오버라이딩
        self.fly(self.name, location)


class Marine(AttackUnit): # 마린
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40, 1, 5)

    def stimpack(self): # 스팀팩 : 체력 10 소모해서 이속, 공속 증가
        if self.hp > 10:
            self.hp-=10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
            self.speed+=5
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

class Tank(AttackUnit): # 탱크
    seize_developed=False # 시즈모드 개발 여부
    
    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode=False

    def set_seize_mode(self):
        if Tank.seize_developed==False: # 시즈 업글 안됐을 때는 그냥 리턴
            return
        
        if self.seize_mode == False: # 현재 시즈모드가 아닐 때
            print("{} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mode=True
        else: # 현재 시즈모드일 때
            print("{} : 시즈 모드를 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mode=False
        
class Wraith(FlyableAttackUnit): # 레이스
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 모드 (해제상태)

    def clocking(self):
        if self.clocked == True:
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked=False
        else:
            print("{} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked=True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start() # 게임 시작

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

attack_units=[]
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seize_developed= True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다")

# 공격 모드 준비(마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # 객체(1번 째 인자)가 어떠한 클래스(2번 째 인자)의 인스턴스인지를 확인하는 함수
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해 입음
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 5 ~ 20 의 공격을 받음 == randrange(5, 21)

game_over() # 게임 종료
        
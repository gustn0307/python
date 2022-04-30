# 클래스(__init__, 멤버변수, 메소드, 상속, 다중 상속, 메소드 오버라이딩, pass , super, 퀴즈)

# 마린: 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"  # 유닛의이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력{}, 공격력 {}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있고 일반모드와 시즈모드가 있음
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력{}, 공격력 {}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력{}, 공격력 {}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{} 유닛이 {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)  # 객체가 많아질수록 공통된 성질들을 일일이 정의하기 ㅈ같음


# __init__()
# 일반유닛, 클래스는 붕어빵 틀이라고 생각하면 좋다
class Unit:
    def __init__(self, name, hp, damage):  # __init__ => 파이썬에서 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력{}, 공격력 {}\n".format(self.hp, self.damage))

# marine1은 Unit 클래스로부터 만들어진 객체이며 Unit 클래스의 인스턴스라고 한다
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
# marine3=("마린") # init 생성자의 self를 제외한 개수만큼의 인자를 넣어줘야만 한다
# marine4=("마린", 40)


# 멤버변수, 위의 클래스에서 self.name, self.hp, self.damage
# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

# 다크아콘, 마인드컨트롤
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True  # 클래스 외부에서 객체에 멤버변수를 만들어서 사용가능

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다".format(wraith2.name))


# 메소드
class AttackUnit:  # 공격유닛 클래스
    def __init__(self, name, hp, damage):  # __init__ => 파이썬에서 생성자
        self.name = name
        self.hp = hp
        self.damage = damage

    # self는 자기 자신을 의미하고 클래스 내에서 메소드 안에는 항상 self를 적어주어야 한다.
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다 [공격력 {}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 상속(상속받은 클래스의 멤버변수와 메소드를 사용가능)
class Unit:  # 일반 유닛
    def __init__(self, name, hp):  # __init__ => 파이썬에서 생성자
        self.name = name
        self.hp = hp

class AttackUnit(Unit):  # 공격 유닛, 일반 유닛을 상속받음
    def __init__(self, name, hp, damage):  # __init__ => 파이썬에서 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage

    # self는 자기 자신을 의미하고 클래스 내에서 메소드 안에는 항상 self를 적어주어야 한다.
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다 [공격력 {}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 다중 상속(부모가 둘 이상인 상속)
class Flyable:  # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(
            name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# 메소드 오버라이딩(부모 클래스에서 정의한 함수를 자식 클래스에서 재정의하여 사용하고 싶을때 사용)
class Unit:  # 일반 유닛
    def __init__(self, name, hp, speed):  # __init__ => 파이썬에서 생성자
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} 유닛이 {} 방향으로 이동합니다 [속도 {}]".format(
            self.name, location, self.speed))

class AttackUnit(Unit):  # 공격 유닛, 일반 유닛을 상속받음
    def __init__(self, name, hp, speed, damage):  # __init__ => 파이썬에서 생성자
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # self는 자기 자신을 의미하고 클래스 내에서 메소드 안에는 항상 self를 적어주어야 한다.
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다 [공격력 {}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 속도(speed)는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상유닛, ㅈㄴ 빠름
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")


# pass
class BuindingUnit(Unit):  # 건물
    def __init__(self, name, hp, location):
        pass  # 아무것도 안하고 일단 넘어가라는 뜻

# 서플 : 건물, 인구수 증가
supply_Depot = BuindingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


# super
class BuindingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)  # 위와 동일한 기능이지만 괄호를 붙여야 하고, self를 사용하지 않는다
        self.location = location

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
# 2개 이상의 다중 상속을 받은 클래스에서 super를 쓰면 상속 인자 중에서 처음 인자로 들어온 클래스에 대해서만 __init__ 함수가 호출이 된다
# 그래서 다중 상속에서 모든 부모 클래스에 대해 초기화가 필요하다면 super를 사용하지 않고 각각의 __init__ 함수를 이용해 초기화 해준다.
dropship = FlyableUnit()


# 퀴즈
"""
부동산 프로그램 작성

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass
"""
# 내 답안
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{0: <5} {1: <5} {2: <5} {3: <10} {4: <10}" # {0: <5} => 0번째 인자는 빈칸은 공백문자로 두고 5칸 할당해서 왼쪽정렬
        .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

h1 = House("강남", "아파트", "매매", "10억", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

estate = []
estate.append(h1)
estate.append(h2)
estate.append(h3)
print("총 {}대의 매물이 있습니다".format(len(estate)))
for house in estate:
    house.show_detail()


# 나도코딩 답안
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {}대의 매물이 있습니다".format(len(houses)))
for house in houses:
    house.show_detail()

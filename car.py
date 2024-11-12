class Car:
    def __init__(self, engine_on=False, speed=0, lock=True, trunk_status=True):
        self.__engine_on = engine_on  # True = ON / False = OFF
        self.__speed = speed  # km/h
        self.__lock = lock  # True = Locked / False = Unlocked
        self.__trunk_status = "TRUNK_CLOSED"  # TRUNK_ClOSED / TRUNK_OPENED
        self.__left_door_status = "CLOSED"  # "OPEN" or "CLOSED"
        self.__right_door_status = "CLOSED"  # "OPEN" or "CLOSED"
        self.__left_door_lock = "LOCKED"  # "LOCKED" or "UNLOCKED"
        self.__right_door_lock = "LOCKED"  # "LOCKED" or "UNLOCKED"

        self.__gear_status = "P" # R, N, D, P
        self.__brake_status = "RELEASE" #PRESS or RELEASE
 
    # 엔진 상태 읽기
    @property
    def engine_on(self):
        return self.__engine_on

    # 속도 읽기
    @property
    def speed(self):
        return self.__speed

    @property
    def lock(self):
        return self.__lock
    
        # 기어 상태 읽기
    @property
    def gear_status(self):
        return self.__gear_status

    # 브레이크 상태 읽기
    @property
    def brake_status(self):
        return self.__brake_status
    
    def set_gear(self, gear):
        self.__gear_status = gear

    def set_brake_status(self, status):
        self.__brake_status = status

    def set_accident(self):
        self.unlock_vehicle()
        self.unlock_left_door()
        self.unlock_right_door()

    # 차량 전체 잠금/잠금 해제
    def lock_vehicle(self):
        self.__lock = True
        self.__left_door_lock = "LOCKED"
        self.__right_door_lock = "LOCKED"

    def unlock_vehicle(self):
        self.__lock = False
        self.__left_door_lock = "UNLOCKED"
        self.__right_door_lock = "UNLOCKED"

    # 트렁크 상태 읽기
    @property
    def trunk_status(self):
        return self.__trunk_status

    # 좌측 도어 상태 읽기
    @property
    def left_door_status(self):
        return self.__left_door_status

    # 우측 도어 상태 읽기
    @property
    def right_door_status(self):
        return self.__right_door_status

    # 좌측 도어 잠금 상태 읽기
    @property
    def left_door_lock(self):
        return self.__left_door_lock

    # 우측 도어 잠금 상태 읽기
    @property
    def right_door_lock(self):
        return self.__right_door_lock

    # 엔진 토글
    def toggle_engine(self):
        self.__engine_on = not self.__engine_on

    # 가속
    def accelerate(self):
        if self.__engine_on and self.__gear_status in ["D", "R"]:
            self.__speed += 10

    # 브레이크
    def brake(self):
        if self.__engine_on:
            self.__speed = max(0, self.__speed - 10)

    # 트렁크 열기
    def open_trunk(self):
        self.__trunk_status = "TRUNK_OPENED"

    # 트렁크 닫기
    def close_trunk(self):
        self.__trunk_status = "TRUNK_CLOSED"

    # 좌측 도어 열기/닫기
    def open_left_door(self):
        self.__left_door_status = "OPEN"

    def close_left_door(self):
        self.__left_door_status = "CLOSED"

    # 우측 도어 열기/닫기
    def open_right_door(self):
        self.__right_door_status = "OPEN"

    def close_right_door(self):
        self.__right_door_status = "CLOSED"

    # 좌측 도어 잠금/잠금 해제
    def lock_left_door(self):
        self.__left_door_lock = "LOCKED"

    def unlock_left_door(self):
        self.__left_door_lock = "UNLOCKED"

    # 우측 도어 잠금/잠금 해제
    def lock_right_door(self):
        self.__right_door_lock = "LOCKED"

    def unlock_right_door(self):
        self.__right_door_lock = "UNLOCKED"

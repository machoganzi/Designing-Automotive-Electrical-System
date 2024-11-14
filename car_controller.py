class CarController:
    def __init__(self, car):
        self.car = car

    def toggle_engine(self):
        self.car.toggle_engine()

    def accelerate(self):
        self.car.accelerate()

    def brake(self):
        self.car.brake()

    # 차량 전체 잠금 상태
    def lock_vehicle(self):
        self.car.lock_vehicle()

    def unlock_vehicle(self):
        self.car.unlock_vehicle()

    def open_trunk(self):
        self.car.open_trunk()

    def close_trunk(self):
        self.car.close_trunk()

    # 좌/우 도어 열기/닫기
    def open_left_door(self):
        self.car.open_left_door()

    def close_left_door(self):
        self.car.close_left_door()

    def open_right_door(self):
        self.car.open_right_door()

    def close_right_door(self):
        self.car.close_right_door()

    # 좌/우 도어 잠금/잠금 해제
    def lock_left_door(self):
        self.car.lock_left_door()

    def unlock_left_door(self):
        self.car.unlock_left_door()

    def lock_right_door(self):
        self.car.lock_right_door()

    def unlock_right_door(self):
        self.car.unlock_right_door()

    def get_engine_status(self):
        return self.car.engine_on

    def get_lock_status(self):
        return self.car.lock

    def get_speed(self):
        return self.car.speed

    def get_trunk_status(self):
        return self.car.trunk_status

    # 좌/우 도어 상태 및 잠금 상태 읽기
    def get_left_door_status(self):
        return self.car.left_door_status

    def get_right_door_status(self):
        return self.car.right_door_status

    def get_left_door_lock(self):
        return self.car.left_door_lock

    def get_right_door_lock(self):
        return self.car.right_door_lock

    # 기어 제어 메서드들
    def gear_p(self):
        self.car.set_gear("P")
    
    def gear_r(self):
        self.car.set_gear("R")
    
    def gear_n(self):
        self.car.set_gear("N")
    
    def gear_d(self):
        self.car.set_gear("D")

    def brake_press(self):
        self.car.set_brake_status("PRESS")
        self.car.brake()

    def brake_release(self):
        self.car.set_brake_status("RELEASE")

    # 사고 상황 처리
    def accident(self):
        self.car.set_accident(True)

    # 기어 상태 확인
    def get_gear_status(self):
        return self.car.gear_status

    # 브레이크 상태 확인
    def get_brake_status(self):
        return self.car.brake_status

    #오작동 알림
    def on_alarm(self):
        self.car.on_alarm()

    def off_alarm(self):
        self.car.off_alarm()

    def get_alarm(self):
        return self.car.alarm_status
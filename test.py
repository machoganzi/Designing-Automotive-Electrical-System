import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback

class Test_Car_simul(unittest.TestCase):
    def setUp(self):
        self.car = Car()  # car 객체 생성
        self.car_controller = CarController(self.car)  # car_controller에 car 객체 전달

# vali
    def test_door_unlocked_open(self):  # 문이 잠겨있지 않을 때, 문 열기
        self.car_controller.unlock_left_door()  # 전제조건 설정
        self.car_controller.unlock_right_door()  # 왼, 오른 문 잠금해제
        self.car.__right_door_status = "CLOSED"  # 왼, 오른 문 닫기
        self.car.__left_door_status = "CLOSED"
        
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller) # 기능 호출
        execute_command_callback("RIGHT_DOOR_OPEN", self.car_controller)
        self.assertEqual("OPEN", self.car_controller.get_left_door_status())  # 왼쪽 문이 "OPEN"인지 확인
        self.assertEqual("OPEN", self.car_controller.get_right_door_status())  # 오른쪽 문이 "OPEN"인지 확인
        
    def test_door_unlocked_closed(self):  # 문이 잠겨있지 않을 때, 문 닫기
        self.car.__right_door_lock = "UNLOCKED"  # 전제조건 설정
        self.car.__left_door_lock = "UNLOCKED"  # 왼, 오른 문 잠금해제
        self.car.__right_door_status = "OPEN"  # 왼, 오른 문 열기
        self.car.__left_door_status = "OPEN"
        
        execute_command_callback("LEFT_DOOR_CLOSE", self.car_controller) # 기능 호출
        execute_command_callback("RIGHT_DOOR_CLOSE", self.car_controller)
        self.assertEqual("CLOSED", self.car_controller.get_left_door_status())  # 왼쪽 문이 "CLOSED"인지 확인
        self.assertEqual("CLOSED", self.car_controller.get_right_door_status())  # 오른쪽 문이 "CLOSED"인지 확인

#defect
    def test_door_locked_open(self):  # 문이 잠겨있을 때, 문 열기
        self.car.__right_door_lock = "LOCKED"  # 전제조건 설정
        self.car.__left_door_lock = "LOCKED"  # 왼, 오른 문 잠금
        self.car.__right_door_status = "CLOSED"  # 왼, 오른 문 닫기
        self.car.__left_door_status = "CLOSED"
        
        execute_command_callback("LEFT_DOOR_OPEN", self.car_controller) # 기능 호출
        execute_command_callback("RIGHT_DOOR_OPEN", self.car_controller)
        self.assertEqual("CLOSED", self.car_controller.get_left_door_status())  # 왼쪽 문이 "CLOSED"(변화x)인지 확인
        self.assertEqual("CLOSED", self.car_controller.get_right_door_status())  # 오른쪽 문이 "CLOSED"(변화x)인지 확인
        
    def test_door_locked_closed(self):  # 문이 잠겨있을 때, 문 닫기
        self.car_controller.lock_right_door()  # 전제조건 설정
        self.car_controller.lock_left_door()  # 왼, 오른 문 잠금
        self.car.__right_door_status = "OPEN"  # 왼, 오른 문 열기
        self.car.__left_door_status = "OPEN"
        
        execute_command_callback("LEFT_DOOR_CLOSE", self.car_controller) # 기능 호출
        execute_command_callback("RIGHT_DOOR_CLOSE", self.car_controller)
        self.assertEqual("OPEN", self.car_controller.get_left_door_status())  # 왼쪽 문이 "OPEN"(변화x)인지 확인
        self.assertEqual("OPEN", self.car_controller.get_right_door_status())  # 오른쪽 문이 "OPEN"(변화x)인지 확인

if __name__ == "__main__":
    unittest.main(exit=False)

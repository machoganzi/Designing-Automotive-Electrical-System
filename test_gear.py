import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class Test_Car_simul(unittest.TestCase):
    def setUp(self):
        self.car = Car()  # car 객체 생성
        self.car_controller = CarController(self.car)  # car_controller에 car 객체 전달

    def test_gear_engine_off(self):  # 엔진이 꺼져있을 때
        # 전제조건
        # 엔진은 이 시점에 꺼져있는 상태
        # 초기 기어는 P상태
        self.car_controller.brake_press()

        execute_command_callback("GEAR_D", self.car_controller)  # 기능 호출
        self.assertEqual("P", self.car_controller.get_gear_status())

    def test_gear_not_brake(self):  # 브레이크 페달을 밟지 않은 상태
        # 전제조건
        # 초기 기어는 P상태
        self.car_controller.toggle_engine()
        self.car_controller.brake_release()

        execute_command_callback("GEAR_D", self.car_controller)  # 기능 호출
        self.assertEqual("P", self.car_controller.get_gear_status())

    def test_gear_speed_not_zero(self):  # 차량의 속력이 0이 아닐 때
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.brake_press()
        self.car_controller.gear_d()
        self.car_controller.brake_release()
        self.car_controller.accelerate()
        self.car_controller.accelerate()
        self.car_controller.accelerate()
        self.car_controller.brake_press()

        execute_command_callback("GEAR_R", self.car_controller)  # 기능 호출
        self.assertEqual("D", self.car_controller.get_gear_status())

    def test_gear(self):  # 모든 조건을 만족하는 상태
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.brake_press()

        execute_command_callback("GEAR_D", self.car_controller)  # 기능 호출
        self.assertEqual("D", self.car_controller.get_gear_status())


if __name__ == "__main__":
    unittest.main(exit=False)

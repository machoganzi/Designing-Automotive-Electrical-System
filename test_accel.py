import unittest
from car import Car
from car_controller import CarController
from main import execute_command_callback


class Test_Car_simul(unittest.TestCase):
    def setUp(self):
        self.car = Car()  # car 객체 생성
        self.car_controller = CarController(self.car)  # car_controller에 car 객체 전달

    def test_accel_engine_off(self):  # 엔진이 꺼져있을 때
        # 전제조건
        # 엔진은 이 시점에 꺼져있는 상태
        self.car_controller.gear_d()
        self.car_controller.lock_vehicle()
        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(0, self.car_controller.get_speed())

    def test_accel_gear_pn(self):  # 기어의 상태가 P 또는 N인 상태
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.gear_p()
        self.car_controller.lock_vehicle()

        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(0, self.car_controller.get_speed())

    def test_accel_brake(self):  # 브레이크 페달을 밟고 있는 상태
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.brake_press()
        self.car_controller.gear_d()
        self.car_controller.lock_vehicle()

        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(0, self.car_controller.get_speed())

    def test_accel_door_trunk_open(self):  # 브레이크 페달을 밟고 있는 상태
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.brake_press()
        self.car_controller.gear_d()
        self.car_controller.brake_release()
        self.car_controller.unlock_vehicle()  # 해제하고
        self.car_controller.open_left_door()  # 열어놨을 때
        self.car_controller.open_right_door()

        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(0, self.car_controller.get_speed())

        self.car_controller.close_left_door()  # 트렁크만 열어놨을 때
        self.car_controller.close_right_door()
        self.car_controller.open_trunk()

        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(0, self.car_controller.get_speed())

    def test_accel(self):  # 브레이크 페달을 밟고 있는 상태
        # 전제조건
        self.car_controller.toggle_engine()
        self.car_controller.brake_press()
        self.car_controller.gear_d()
        self.car_controller.brake_release()
        self.car_controller.lock_vehicle()  # 해제하고

        execute_command_callback("ACCELERATE", self.car_controller)  # 기능 호출
        self.assertEqual(10, self.car_controller.get_speed())


if __name__ == "__main__":
    unittest.main(exit=False)

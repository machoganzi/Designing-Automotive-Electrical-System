import threading
from car import Car
from car_controller import CarController
from gui import CarSimulatorGUI

# execute_command를 제어하는 콜백 함수
# -> 이 함수에서 시그널을 입력받고 처리하는 로직을 구성하면, 알아서 GUI에 연동이 됩니다.

def execute_command_callback(command, car_controller):
    # 엔진 시동/정지
    if command == "ENGINE_BTN":
        # 요구사항-1: 기어 P + 브레이크 밟음
        if (car_controller.get_gear_status() == "P" and 
            car_controller.get_brake_status() == "PRESS" and
            car_controller.get_speed() == 0):
            car_controller.toggle_engine()
            car_controller.off_alarm()

        else:
            car_controller.on_alarm()

    # 가속
    elif command == "ACCELERATE":
        # 요구사항-3: 엔진 ON + 기어 D/R + 브레이크 해제 + 도어/트렁크 닫힘 
        if (car_controller.get_engine_status() and 
            car_controller.get_gear_status() in ["D", "R"] and
            car_controller.get_brake_status() == "RELEASE" and
            car_controller.get_left_door_status() == "CLOSED" and
            car_controller.get_right_door_status() == "CLOSED" and 
            car_controller.get_trunk_status()):
            car_controller.accelerate()
            # 요구사항-10.3: 속도 15km/h 이상 시 전체 자동 잠금
            if car_controller.get_speed() >= 15:
                car_controller.lock_vehicle()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    # 브레이크 제어
    elif command == "BRAKE_PRESS":
        car_controller.brake_press()
        car_controller.off_alarm()

    elif command == "BRAKE_RELEASE":
        car_controller.brake_release()
        car_controller.off_alarm()

    # 전체 잠금장치 제어
    elif command == "LOCK":
        # 요구사항-2: 모든 문이 닫힘 상태
        if (car_controller.get_left_door_status() == "CLOSED" and
            car_controller.get_right_door_status() == "CLOSED" and
            car_controller.get_trunk_status()):
            car_controller.lock_vehicle()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "UNLOCK":
        # 요구사항-2: 잠금해제는 정차상태
        if car_controller.get_speed() == 0:
            car_controller.unlock_vehicle()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    # 좌측 문 제어 
    elif command == "LEFT_DOOR_LOCK":
        # 요구사항-6: 15km/h 미만 + 문 닫힘
        if car_controller.get_speed() < 15 and car_controller.get_left_door_status() == "CLOSED":
            car_controller.lock_left_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "LEFT_DOOR_UNLOCK":
        # 요구사항-6: 15km/h 미만
        if car_controller.get_speed() < 15:
            car_controller.unlock_left_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "LEFT_DOOR_OPEN":
        # 요구사항-5: 잠금해제 상태
        if car_controller.get_left_door_lock() == "UNLOCKED":
            car_controller.open_left_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "LEFT_DOOR_CLOSE":
        if car_controller.get_left_door_lock() == "UNLOCKED":
            car_controller.close_left_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    # 우측 문 제어 
    elif command == "RIGHT_DOOR_LOCK":
        # 요구사항-6: 15km/h 미만 + 문 닫힘
        if car_controller.get_speed() < 15 and car_controller.get_right_door_status() == "CLOSED":
            car_controller.lock_right_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "RIGHT_DOOR_UNLOCK":
        # 요구사항-6: 15km/h 미만
        if car_controller.get_speed() < 15:
            car_controller.unlock_right_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "RIGHT_DOOR_OPEN":
        # 요구사항-5: 잠금해제 상태
        if car_controller.get_right_door_lock() == "UNLOCKED":
            car_controller.open_right_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "RIGHT_DOOR_CLOSE":
        if car_controller.get_right_door_lock() == "UNLOCKED":
            car_controller.close_right_door()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    # 트렁크 제어
    elif command == "TRUNK_OPEN":
        # 요구사항-7: 전체 잠금해제 상태
        if not car_controller.get_lock_status():
            car_controller.open_trunk()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "TRUNK_CLOSE":
        # 요구사항-7: 전체 잠금해제 상태
        if not car_controller.get_lock_status():
            car_controller.close_trunk()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    # 사고 상황 처리
    elif command == "ACCIDENT":
        # 요구사항-10.4: 충돌 시 자동 잠금해제
        car_controller.accident()
        car_controller.on_alarm()

    # 기어 제어
    elif command in ["GEAR_P", "GEAR_R", "GEAR_N", "GEAR_D"]:
        # 요구사항-8: 엔진 ON + 브레이크 밟음
        if (car_controller.get_engine_status() and 
            car_controller.get_brake_status() == "PRESS" and
            car_controller.get_speed() == 0):  # 정지상태 추가
            if command == "GEAR_P":
                car_controller.gear_p()
            elif command == "GEAR_R":
                car_controller.gear_r()
            elif command == "GEAR_N":
                car_controller.gear_n()
            elif command == "GEAR_D":
                car_controller.gear_d()
            car_controller.off_alarm()
        else:
            car_controller.on_alarm()

    elif command == "SOS":
        # 1. 차량 정지
        while car_controller.get_speed() > 0:
            car_controller.brake_press()
        # 2. 기어 P 변경
        car_controller.gear_p()
        # 3. 모든 문 잠금해제
        car_controller.unlock_vehicle()
        car_controller.unlock_left_door()
        car_controller.unlock_right_door()
        # 4. 트렁크 열기
        car_controller.open_trunk() 
        # 5. 알람 표시
        car_controller.on_alarm()

# 파일 경로를 입력받는 함수
# -> 가급적 수정하지 마세요.
#    테스트의 완전 자동화 등을 위한 추가 개선시에만 일부 수정이용하시면 됩니다. (성적 반영 X)
def file_input_thread(gui):
    while True:
        file_path = input("Please enter the command file path (or 'exit' to quit): ")

        if file_path.lower() == 'exit':
            print("Exiting program.")
            break

        # 파일 경로를 받은 후 GUI의 mainloop에서 실행할 수 있도록 큐에 넣음
        gui.window.after(0, lambda: gui.process_commands(file_path))

# 메인 실행
# -> 가급적 main login은 수정하지 마세요.
if __name__ == "__main__":
    car = Car()
    car_controller = CarController(car)

    # GUI는 메인 스레드에서 실행
    gui = CarSimulatorGUI(car_controller, lambda command: execute_command_callback(command, car_controller))

    # 파일 입력 스레드는 별도로 실행하여, GUI와 병행 처리
    input_thread = threading.Thread(target=file_input_thread, args=(gui,))
    input_thread.daemon = True  # 메인 스레드가 종료되면 서브 스레드도 종료되도록 설정
    input_thread.start()

    # GUI 시작 (메인 스레드에서 실행)
    gui.start()

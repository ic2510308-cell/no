"""
센서 데이터 로거
드론이나 아두이노 프로젝트에서 센서 데이터를 수집하고 기록하는 유틸리티

Author: 레인
Date: 2024-11-20
"""

import time
from datetime import datetime


class SensorDataLogger:
    """센서 데이터를 로깅하는 클래스"""
    
    def __init__(self, filename="sensor_log.txt"):
        """
        초기화 함수
        
        Args:
            filename (str): 로그를 저장할 파일명
        """
        self.filename = filename
        self.data_buffer = []
        
    def add_data(self, sensor_name, value, unit=""):
        """
        센서 데이터 추가
        
        Args:
            sensor_name (str): 센서 이름 (예: "MPU6050", "VL53L0X")
            value (float): 센서 값
            unit (str): 단위 (예: "cm", "degree", "m/s²")
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        data_entry = {
            "timestamp": timestamp,
            "sensor": sensor_name,
            "value": value,
            "unit": unit
        }
        self.data_buffer.append(data_entry)
        print(f"[{timestamp}] {sensor_name}: {value} {unit}")
        
    def save_to_file(self):
        """버퍼의 데이터를 파일에 저장"""
        if not self.data_buffer:
            print("저장할 데이터가 없습니다.")
            return
            
        with open(self.filename, "a", encoding="utf-8") as f:
            for entry in self.data_buffer:
                line = f"{entry['timestamp']},{entry['sensor']},{entry['value']},{entry['unit']}\n"
                f.write(line)
        
        print(f"{len(self.data_buffer)}개의 데이터를 {self.filename}에 저장했습니다.")
        self.data_buffer.clear()
    
    def get_statistics(self, sensor_name):
        """특정 센서의 통계 정보 반환"""
        values = [entry['value'] for entry in self.data_buffer 
                 if entry['sensor'] == sensor_name]
        
        if not values:
            return None
            
        return {
            "count": len(values),
            "average": sum(values) / len(values),
            "min": min(values),
            "max": max(values)
        }


# 사용 예시
if __name__ == "__main__":
    # 로거 생성
    logger = SensorDataLogger("drone_sensors.csv")
    
    # 시뮬레이션: MPU6050 자이로 데이터
    print("=== 센서 데이터 로깅 시작 ===\n")
    
    for i in range(10):
        # 예시 데이터 (실제로는 센서에서 읽어옴)
        gyro_x = 0.5 + (i * 0.1)
        gyro_y = -0.3 + (i * 0.05)
        distance = 150 - (i * 5)
        
        logger.add_data("MPU6050_GyroX", gyro_x, "deg/s")
        logger.add_data("MPU6050_GyroY", gyro_y, "deg/s")
        logger.add_data("VL53L0X_Distance", distance, "mm")
        
        time.sleep(0.1)  # 100ms 간격
    
    print("\n=== 통계 정보 ===")
    stats = logger.get_statistics("VL53L0X_Distance")
    if stats:
        print(f"거리 센서 - 평균: {stats['average']:.2f}mm, "
              f"최소: {stats['min']}mm, 최대: {stats['max']}mm")
    
    # 파일에 저장
    print("\n=== 데이터 저장 ===")
    logger.save_to_file()
    print("\n완료!")

from src.parking_fee import calculate_parking_fee

def test_motorcycle_base_fee():
    assert calculate_parking_fee('motorcycle', 2, 'weekday', False) == 2
    
def test_car_base_fee():
    assert calculate_parking_fee('car', 2, 'weekday', False) == 5
    
def test_truck_base_fee():
    assert calculate_parking_fee('truck', 2, 'weekday', False) == 10        
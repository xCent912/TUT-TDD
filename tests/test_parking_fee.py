from src.parking_fee import calculate_parking_fee

def test_motorcycle_base_fee():
    assert calculate_parking_fee('motorcycle', 2, 'weekday', False) == 2
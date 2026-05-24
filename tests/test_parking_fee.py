import pytest

from src.parking_fee import calculate_parking_fee


def test_motorcycle_base_fee():
    assert calculate_parking_fee('motorcycle', 2, 'weekday', False) == 2


def test_car_base_fee():
    assert calculate_parking_fee('car', 2, 'weekday', False) == 5


def test_truck_base_fee():
    assert calculate_parking_fee('truck', 2, 'weekday', False) == 10


def test_invalid_vehicle_type_raises_value_error():
    with pytest.raises(ValueError, match="Invalid vehicle type"):
        calculate_parking_fee('bicycle', 2, 'weekday', False)


def test_invalid_day_type_raises_value_error():
    with pytest.raises(ValueError, match="Invalid day type"):
        calculate_parking_fee('car', 2, 'holiday', False)


def test_negative_parking_duration_raises_value_error():
    with pytest.raises(ValueError, match="must not be negative"):
        calculate_parking_fee('car', -1, 'weekday', False)


def test_parking_duration_type_error():
    with pytest.raises(TypeError, match="must be a number"):
        calculate_parking_fee('car', 'two', 'weekday', False)

def test_free_parking_under_one_hour():
    assert calculate_parking_fee('car', 0.5, 'weekday', False) == 0

def test_free_parking_for_motorcycle_under_one_hour():
    assert calculate_parking_fee('motorcycle', 0.99, 'weekday', False) == 0

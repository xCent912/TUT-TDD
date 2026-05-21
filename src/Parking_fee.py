BASE_FEES = {
    'motorcycle': 2,
    'car': 5,
    'truck': 10,
}

VALID_DAY_TYPES = {'weekday', 'weekend'}


def validate_vehicle_type(vehicle_type):
    if vehicle_type not in BASE_FEES:
        valid_types = ', '.join(sorted(BASE_FEES))
        raise ValueError(f"Invalid vehicle type '{vehicle_type}'. Valid types: {valid_types}.")


def validate_parking_duration(parking_duration):
    if not isinstance(parking_duration, (int, float)):
        raise TypeError('Parking duration must be a number.')
    if parking_duration < 0:
        raise ValueError('Parking duration must not be negative.')


def validate_day_type(day_type):
    if day_type not in VALID_DAY_TYPES:
        valid_days = ', '.join(sorted(VALID_DAY_TYPES))
        raise ValueError(f"Invalid day type '{day_type}'. Valid day types: {valid_days}.")


def get_base_fee(vehicle_type):
    return BASE_FEES[vehicle_type]


def calculate_parking_fee(vehicle_type, parking_duration, day_type, is_public_holiday):
    """Calculate the parking fee for a vehicle.

    Currently the parking fee is based on the vehicle type only.
    Validation is performed for all input parameters to keep the function
    safe and maintainable.
    """
    validate_vehicle_type(vehicle_type)
    validate_parking_duration(parking_duration)
    validate_day_type(day_type)

    return get_base_fee(vehicle_type)

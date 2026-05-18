BASE_FEES = {'motorcycle': 2, 'car': 5, 'truck': 10}
def calculate_parking_fee(vehicle_type,parking_duration, day_type,is_public_holiday):
    return BASE_FEES[vehicle_type]
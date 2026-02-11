import time

def calculate_dwell_time(entry_times):
    dwell_data = {}
    current_time = time.time()

    for person_id, entry_time in entry_times.items():
        dwell_time = current_time - entry_time
        dwell_data[person_id] = round(dwell_time, 2)

    return dwell_data

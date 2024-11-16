# main.py
from datetime import datetime
docking_bays = [
    {
        'bay_id': 1,
        'size': 'small',
        'schedule': []  # list of (arrival_time, departure_time, ship_name) tuples
    },
    {
        'bay_id': 2,
        'size': 'small',
        'schedule': []
    },
    {
        'bay_id': 3,
        'size': 'medium',
        'schedule': []
    },
    {
        'bay_id': 4,
        'size': 'medium',
        'schedule': []
    },
    {
        'bay_id': 5,
        'size': 'large',
        'schedule': []
    },
    {
        'bay_id': 6,
        'size': 'large',
        'schedule': []
    }
]

incoming_ships = [
    {
        'ship_name': 'Shuttle Alpha',
        'size': 'small',
        'arrival_time': '12:00',
        'departure_time': '14:00'
    },
    {
        'ship_name': 'Freighter Beta',
        'size': 'medium',
        'arrival_time': '13:00',
        'departure_time': '15:00'
    },
    {
        'ship_name': 'Cruiser Gamma',
        'size': 'large',
        'arrival_time': '14:00',
        'departure_time': '18:00'
    },
    {
        'ship_name': 'Shuttle Delta',
        'size': 'small',
        'arrival_time': '15:00',
        'departure_time': '17:00'
    },
    {
        'ship_name': 'Freighter Epsilon',
        'size': 'medium',
        'arrival_time': '16:00',
        'departure_time': '18:00'
    },
    {
        'ship_name': 'Cruiser Zeta',
        'size': 'large',
        'arrival_time': '10:00',
        'departure_time': '12:00'
    }
]

def size_to_value(size):
    size_map = {'small': 1, 'medium': 2, 'large': 3}
    return size_map[size]

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def print_docking_bays():
    print("Docking Bays:")
    for bay in docking_bays:
        formatted_schedule = ", ".join(
            f"{ship} ({arr.strftime('%H:%M')} to {dep.strftime('%H:%M')})"
            for arr, dep, ship in bay['schedule']
        )
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {formatted_schedule or 'Empty'}")

def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, "
              f"Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

def schedule_ship(ship, bay):
    arrival = parse_time(ship['arrival_time'])
    departure = parse_time(ship['departure_time'])
    bay['schedule'].append((arrival, departure, ship['ship_name']))
    print(f"Scheduled {ship['ship_name']} in Bay {bay['bay_id']} - "
          f"{arrival.strftime('%H:%M')} to {departure.strftime('%H:%M')}")

def main():
    print_docking_bays()
    print_incoming_ships()

    for ship in incoming_ships:
        assigned = False
        for bay in docking_bays:
            if size_to_value(bay['size']) >= size_to_value(ship['size']):  
                arrival = parse_time(ship['arrival_time'])
                departure = parse_time(ship['departure_time'])
                conflict = any(
                    arrival < dep and departure > arr for arr, dep, _ in bay['schedule']
                )
                if not conflict:
                    schedule_ship(ship, bay)
                    assigned = True
                    break
        if not assigned:
            print(f"Ship {ship['ship_name']} could not be scheduled.")

    print("\nFinal Docking Bays Status:")
    print_docking_bays()

if __name__ == "__main__":
    main()
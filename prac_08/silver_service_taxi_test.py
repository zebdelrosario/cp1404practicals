from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print(f"""Silver Service Taxis!""")
    taxi_one = SilverServiceTaxi("Taxi 1", 100, 2)
    taxi_one.start_fare()
    print("Starting Fare!\n")
    taxi_one.drive(18)
    print(f"Fare distance: {taxi_one.current_fare_distance:>8} km")
    print(f"Current fare cost: $ {taxi_one.get_fare():.2f}")
    print(taxi_one)


main()

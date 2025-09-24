# ==== import libraries======
import array


# ====== Function: Generate Solar Output Report ==========
def generate_report(solar_output):
    report = (
        f"\n--- Solar Panel Output Report ---\n"
        f" The report of Solar Panel Output Log is: {solar_output} \n"
        f" The Total Solar Output is: {sum(solar_output)} kWh \n"
        f" The Average Solar Output is: {round(sum(solar_output) / len(solar_output), 2)} kWh \n"
        f" The Minimum Solar Output is: {min(solar_output)} kWh \n"
        f" The Maximum Solar Output is: {max(solar_output)} kWh \n"
    )
    print(report)


# ====== Function: Check Threshold ==========
def check_threshold(solar_output, threshold=125):
    average_output = sum(solar_output) / len(solar_output)
    if average_output > threshold and max(solar_output) > 140:
        print(f" The average output exceeds the threshold: {round(average_output, 2)} → Above Standard")
    else:
        print(f" The average output exceeds the threshold: {round(average_output, 2)} → Below Standard")


# ====== Function: Maintain List ==========
def maintain_list(solar_output, new_output=138):
    solar_output.append(new_output)
    print(f"\n You already appended {new_output} in this array {solar_output} on your Solar Panel Output log.")

    # Remove one entry <= 115
    for output in solar_output:
        if output <= 115:
            solar_output.remove(output)
            print(f" Removed {output} from your Solar Panel Output log.")
            break

    print(f"\nSolar Panel Output log before sort: {solar_output}")
    solar_output.sort()
    print(f" Sorted Solar Panel Output log: {solar_output}")
    return solar_output


# ====== Function: Compare Array vs List ==========
def compare_array_list(solar_output):
    solar_output_array = array.array('i', solar_output[:6])  # First 6 outputs
    array_sum = sum(solar_output_array)
    list_sum = sum(solar_output)

    print(f"\nArray Sum (first 6 Solar Outputs): {array_sum} kWh")
    print(f"List Sum (all Solar Outputs): {list_sum} kWh")

    if array_sum == list_sum:
        print("All Solar Outputs are equal")
    else:
        print("All Solar Outputs are different")


# ====== Function: Manage Records with Dictionaries ==========
def manage_records(solar_output_log):
    for record in solar_output_log:
        print(f"{record} ")
        if record['id'] == 3:
            record['value'] = 145
            print(f"\n Updated Record: {record} \n")

    # Delete one record (id = 2)
    solar_output_log = [record for record in solar_output_log if record['id'] != 2]

    # Compute total value from remaining logs
    total_value = sum(record['value'] for record in solar_output_log)
    print("Total Solar Output from all Panels:", total_value, "kWh")
    return solar_output_log


# ====== Main function ==========
def main():
    solar_output = [120, 135, 150, 110, 145, 130, 125, 140, 155]

    generate_report(solar_output)
    check_threshold(solar_output)
    solar_output = maintain_list(solar_output)
    compare_array_list(solar_output)

    solar_output_log = [
        {'id': 1, 'name': 'Panel A', 'value': 130},
        {'id': 2, 'name': 'Panel B', 'value': 125},
        {'id': 3, 'name': 'Panel C', 'value': 140},
        {'id': 4, 'name': 'Panel D', 'value': 128}
    ]
    manage_records(solar_output_log)


# Run the program
if __name__ == "__main__":
    main()

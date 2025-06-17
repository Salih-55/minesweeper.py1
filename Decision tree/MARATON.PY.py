def read_file(filename):
    results = []
    try:
        with open(filename, 'r') as my_file:
            for line in my_file:
                parts = line.strip().split(',')
                if len(parts) >= 4:
                    entry = {
                        'id': parts[0],
                        'time': parts[1],
                        'firstname': parts[2],
                        'lastname': parts[3]
                    }
                    results.append(entry)
                else:
                    print(f"Skipping invalid line:{line.strip()}")  # skipping lines with wrong data
    except  FileNotFoundError:
        print(f"Error:  The file {filename} was not found.")
    except Exception as e:
        print(str(e))
    if not results:
        print({filename})
    return results


def get_interval_data(start_time, end_time, results):
    totaltime = 0
    count = 0
    for entry in results:  # converting time into total seconds to do comparison (it is easier with this )
        h, m, s = map(int, entry['time'].split(':'))
        time_in_seconds = h * 3600 + m * 60 + s

        if start_time <= time_in_seconds <= end_time:
            totaltime += time_in_seconds
            count += 1
            # calculating mean time
    mean_time = totaltime / count if count > 0 else 0
    return {'count': count, 'mean': mean_time}


# FREEZE CODE BEGIN
def main():
    results = read_file('marathon.txt')
    option = ''
    while option != 'Q':
        menu()
        option = input('Select option: ')
        if option == 'S':
            display_competitor(results)
        elif option == 'I':
            display_nbr_in_interval(results)


def display_competitor(results):
    id_no = input('Enter competitor ID:')
    found = False
    for competitor in results:
        if competitor['id'] == id_no:
            display_competitor_info(competitor)
            found = True
    if not found:
        print('Competitor not found')


def display_competitor_info(competitor):
    print('ID :', competitor['id'])
    print('First Name :', competitor['firstname'])
    print('First Name :', competitor['lastname'])


def display_nbr_in_interval(results):
    start_time = input('Enter start time of interval (hh:mm:ss): ')
    start_secs = get_secs(start_time)
    end_time = input('Enter end time of interval (hh:mm:ss): ')
    end_secs = get_secs(end_time)
    interval_data = get_interval_data(start_secs, end_secs, results)
    print('Number of competitors finishing in this interval = ', interval_data['count'])
    if interval_data['count'] != 0:
        secs = interval_data['mean']
        mins = secs // 60
        secs = secs % 60
        hours = mins // 60
        mins = mins % 60
        print('Mean time in interval is ', int(hours), 'hours', int(mins), 'minutes', 'and ', int(secs), 'seconds')
    else:
        print('No competitors in interval')


def get_secs(time):
    time_split = time.split(':')
    seconds = int(time_split[2]) + 60 * int(time_split[1]) + 60 * 60 * int(time_split[0])
    return seconds


def menu():
    print('Options are:')
    print('S - Show data for a competitor')
    print('I - Show statistics for competitors finishing in a given interval')
    print('Q - Quit the program')


if __name__ == "__main__":
    main()
# FREEZE CODE END
'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly
overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''
'''
Note:
Minimum Number of Platforms Required for a Railway/Bus Station
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

time        type        room_number
0           start           1
30          start           2
50          end             1
60          start           2
75          end             1
150         end             0
'''
def find_min_rooms(time_list):
    '''
    Args:
        time_list(list)
    Returns:
        int
    '''
    start = sorted([num[0] for num in time_list])
    end = sorted([num[1] for num in time_list])

    room_occupied = max_room_num = 0
    i = j = 0
    n = len(time_list)

    while i < n and j < n:
        if start[i] < end[j]:
            room_occupied += 1
            max_room_num = max(room_occupied, max_room_num)
            i += 1
        else:
            room_occupied -= 1
            j += 1

    return max_room_num


def main():
    time_list = [(30, 75), (0, 50), (60, 150)]
    time_list2 = [(90,91), (94, 120), (95, 112), (110, 113), (150, 190), (180, 200)]
    print find_min_rooms(time_list2)

if __name__ == '__main__':
    main()

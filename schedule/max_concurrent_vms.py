"""
Find the maximum number of VMs required for a set of scheduled
jobs. Each job is a tuple containing the requested begin-end time
for a single VM.
"""
SCHEDULE = [(2, 5), (3, 6), (5, 7), (8, 10), (1, 10), (3, 4)]


def max_concurrent(schedule):
    """count the number of slots that overlap by comparing each slot to all others.
    """
    concurrent_slots = []
    next_slot = 1
    for start, stop in schedule:
        concurrent = 1
        for next_start, next_stop in schedule[next_slot:]:
            if next_start < stop and next_stop > start:
                concurrent += 1
        concurrent_slots.append(concurrent)
        next_slot += 1
    return max(concurrent_slots)


if __name__ == '__main__':
    print('schedule:', SCHEDULE)
    print('max concurrent slots:', max_concurrent(SCHEDULE))

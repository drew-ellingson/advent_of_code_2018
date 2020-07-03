import re


class Guard:
    def __init__(self, guard_events, guard_num):
        self.guard_events = guard_events
        self.guard_num = guard_num
        self.total_minutes_asleep = self.get_minutes_asleep()
        self.most_asleep_minute = self.get_most_asleep_minute()[0]
        self.most_asleep_minute_count = self.get_most_asleep_minute()[1]

    def get_minutes_asleep(self):
        minutes_asleep = 0
        for event in self.guard_events:
            if event.name == "falls_asleep":
                asleep_minute = event.minute
            if event.name == "wakes_up":
                awake_minute = event.minute
                minutes_asleep += awake_minute - asleep_minute
        return minutes_asleep

    def get_most_asleep_minute(self):
        sleep_min_counts = {k: 0 for k in range(60)}
        for event in self.guard_events:
            if event.name == "falls_asleep":
                asleep_min = event.minute
            if event.name == "wakes_up":
                awake_min = event.minute
                for i in range(asleep_min, awake_min):
                    sleep_min_counts[i] += 1
        return max(sleep_min_counts.items(), key=lambda x: x[1])


class Event:
    def __init__(self, event_string, guard_num):
        self.raw_event = event_string
        self.guard_num = guard_num
        self.timestamp = event_string[1 : event_string.index("]")]
        self.minute = int(self.timestamp[-2:])

        if "begin" in event_string:
            self.name = "begins_shift"
        elif "wake" in event_string:
            self.name = "wakes_up"
        else:
            self.name = "falls_asleep"


if __name__ == "__main__":
    with open("input.txt") as input_file:
        raw_events = [event.strip() for event in input_file.readlines()]
        raw_events = sorted(raw_events)

    events = []
    guard_regex = re.compile(r"#[0-9]*")
    for event in raw_events:
        if "begins" in event:
            guard_num = int(guard_regex.search(event).group()[1:])
        events.append(Event(event, guard_num))

    guard_nums = list(set([event.guard_num for event in events]))

    guards = []
    for guard in guard_nums:
        guard_events = list(filter(lambda x: x.guard_num == guard, events))
        guards.append(Guard(guard_events, guard))

    sleepiest_guard = max(guards, key=lambda x: x.total_minutes_asleep)

    print(
        f"P1 Answer: {sleepiest_guard.most_asleep_minute * sleepiest_guard.guard_num}"
    )

    consistentest_guard = max(guards, key=lambda x: x.most_asleep_minute_count)

    print(
        f"P2 Answer: {consistentest_guard.most_asleep_minute * consistentest_guard.guard_num}"
    )

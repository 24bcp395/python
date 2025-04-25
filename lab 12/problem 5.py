class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Convert excess seconds to minutes and minutes to hours
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60

        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds
        return Time(total_hours, total_minutes, total_seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_sec):
        self.hours = total_sec // 3600
        total_sec %= 3600
        self.minutes = total_sec // 60
        self.seconds = total_sec % 60



t1 = Time(1, 40, 30)
t2 = Time(2, 35, 50)

print("Time 1:")
t1.display()

print("Time 2:")
t2.display()

t3 = t1 + t2
print("Time after addition:")
t3.display()

print("Total seconds in Time 3:")
print(t3.to_seconds())

# Convert from seconds to time again
print("Converting 3671 seconds to time:")
t4 = Time()
t4.from_seconds(3671)
t4.display()


"""class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        """Ensure that time is properly formatted (e.g. 70s → 1m 10s)."""
        total_seconds = self.to_seconds()
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def to_seconds(self):
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        """Create Time object from total seconds."""
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def add_time(self, other):
        """Add two Time objects."""
        total_seconds = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_seconds)

    def subtract_time(self, other):
        """Subtract one Time object from another. Returns absolute value."""
        total_seconds = abs(self.to_seconds() - other.to_seconds())
        return Time.from_seconds(total_seconds)

    def __str__(self):
        """Return time in HH:MM:SS format."""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


# === Test the Time class ===
if __name__ == "__main__":
    t1 = Time(2, 45, 50)
    t2 = Time(1, 20, 30)

    print("Time 1:", t1)
    print("Time 2:", t2)

    sum_time = t1.add_time(t2)
    print("Sum:", sum_time)

    diff_time = t1.subtract_time(t2)
    print("Difference:", diff_time)

    # Create time from seconds
    seconds_input = 5000
    from_seconds = Time.from_seconds(seconds_input)
    print(f"{seconds_input} seconds is:", from_seconds)

    # Convert time to seconds
    print("Time 1 in seconds:", t1.to_seconds())
"""
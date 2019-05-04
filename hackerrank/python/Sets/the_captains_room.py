from collections import Counter

# Parse string as Counter: 'room_numbers'
_ = input()
room_numbers = Counter(input().split())

# Print key where value equals 1
for k, v in room_numbers.items():
    if v == 1:
        print(k)
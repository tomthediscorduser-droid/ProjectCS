#EXERCISE 1
'''
a) syntax | shot = {"elbow_angle": 92, "knee_angle": 140 | never closed {}
b) logic | print(frames[2]["elbow_angle"]) | i = 2 is out of frame as previous code only has 0 and 1
c) logic | print(frame["elbow"]) | variable elbow doesnt exist, its called "elbow_angle"
d) logic | average = sum(angles) / 3 | it should be  /4 as there are 4 values not 3
'''

'''
#A bunch of indentation problems
shot_frames = [
{"frame": 0, "wrist_y": 410, "elbow_angle": 70},
{"frame": 1, "wrist_y": 380, "elbow_angle": 85},
{"frame": 2, "wrist_y": 300, "elbow_angle": 110},
{"frame": 3, "wrist_y": 230, "elbow_angle": 150},
{"frame": 4, "wrist_y": 190, "elbow_angle": 172},
{"frame": 5, "wrist_y": 210, "elbow_angle": 165},
]

def average_elbow(frames):
    total = 0
    for f in frames:
        total += f["elbow_angle"]
    return total / len(frames)

def find_release_frame(frames):
    best = frames[0]
    for f in frames:
        if f["wrist_y"] < best["wrist_y"]:
            best = f
    return best["frame"]

def count_bent_frames(frames, limit):
    count = 0
    for f in frames:
        if f["elbow_angle"] < limit:
            count += 1
    return count

print("Average elbow angle:", round(average_elbow(shot_frames), 1))
print("Release frame:", find_release_frame(shot_frames))
print("Bent frames (< 100):", count_bent_frames(shot_frames, 100))
'''



#EXERCISE 2
'''
a) syntax | if queues["north"] > 5 | missing :
b) runtime | print(queues["North"]) | key is "north" not "North"
c) runtime | average_wait = total_wait / cars_served | cars_served = 0 so it divides by 0
d) logic | busiest = min(queues, key=queues.get) | should use max() as we need the longest queue
'''

'''
1. Runtime | TypeError | cant add a string to an integer
2. queues[direction] += arrivals[direction] | inside update_queues function
3. <module> -> run_step() -> update_queues()
4. queues[direction] += int(arrivals[direction]) | converts the string into an integer before adding

Predicted output: {'north': 6, 'south': 8, 'east': 5, 'west': 5}
'''

'''
queues = {"north": 4, "south": 7, "east": 2, "west": 5}
arrivals = {"north": "2", "south": "1", "east": "3", "west": "0"}

def update_queues(queues, arrivals):
    for direction in queues:
        queues[direction] += int(arrivals[direction])

def run_step(queues, arrivals):
    update_queues(queues, arrivals)
    return queues

print(run_step(queues, arrivals))
'''

'''
1. logic | return min(queues, key=queues.get) | should use max() because the longest queue gets green, confirmed when south was chosen instead of east
2. logic | queues[direction] = queues[direction] - cars_per_step | queues can become negative, fixed using max(0, queues[direction] - cars_per_step)
3. logic | return total // len(history) | should use / instead of // because // rounds down, confirmed when average became 10.5 instead of 10
'''

'''
queues = {"north": 4, "south": 7, "east": 2, "west": 5}

def choose_green(queues):
    return max(queues, key=queues.get)

def serve(queues, direction, cars_per_step=3):
    queues[direction] = max(0, queues[direction] - cars_per_step)

def average_queue(history):
    total = 0
    for length in history:
        total = total + length
    return total / len(history)

history = []
for step in range(4):
    green = choose_green(queues)
    serve(queues, green)
    history.append(sum(queues.values()))
    print("Step", step, "| green:", green, "| queues:", queues)

print("Average total queue:", average_queue(history))
'''

'''
1. I would notice the average waiting time being too high because the program serves the shortest queue instead of the longest one

2. Negative queues are impossible because you cant have fewer than 0 cars waiting, even though Python allows negative numbers

3. print(queues) | wanted to check the queues after each step, showed that east became negative because more cars were removed than existed
'''

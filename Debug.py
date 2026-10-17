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
a) Syntax | if queues["north"] > 5 | Missing ":" 
b) Syntax | print(queues["North"]) | variable is north not North
c) Runtime | cars_served = 0 | this would make the next line divide by 0
d) Logic | busiest = min(queues, key=queues.get) | it should busiest = max.... as we need to serve place with highest queue

1. Runtime error as you cant add a string to an integer
2. queues[direction] += arrivals[direction] inside the update_queues funcntion
3. 
4. queues[direction] += int(arrivals[direction]), reads the assigned integer value to the arrival instead of using the string
'''

'''
def update_queues(queues, arrivals):
    for direction in queues:
        queues[direction] += int(arrivals[direction])

def run_step(queues, arrivals):
    update_queues(queues, arrivals)
    return queues

print(run_step(queues, arrivals))
'''

queues = {"north": 4, "south": 7, "east": 2, "west": 5}

def choose_green(queues):
    return min(queues, key=queues.get)

def serve(queues, direction, cars_per_step=3):
    queues[direction] = queues[direction] - cars_per_step

def average_queue(history):
    total = 0
    for length in history:
        total = total + length
    return total // len(history)

history = []
for step in range(4):
    green = choose_green(queues)
    serve(queues, green)
    history.append(sum(queues.values()))
    print("Step", step, "| green:", green, "| queues:", queues)
    print("Average total queue:", average_queue(history))
shots = [
{'id': 1, 'status': 'made', 'elbow_angle': 88, 'knee_angle': 121,
'release_frame': 42, 'conf': 0.93},
{'id': 2, 'status': 'missed', 'elbow_angle': 104, 'knee_angle': 135,
'release_frame': 39, 'conf': 0.88},
{'id': 3, 'status': 'made', 'elbow_angle': 91, 'knee_angle': 118,
'release_frame': 43, 'conf': 0.95},
{'id': 4, 'status': 'missed', 'elbow_angle': None, 'knee_angle': 126,
'release_frame': 40, 'conf': 0.81},
{'id': 5, 'status': 'made', 'elbow_angle': 86, 'knee_angle': 115,
'release_frame': 44, 'conf': 0.52},
{'id': 6, 'status': 'undetermined', 'elbow_angle': 97, 'knee_angle': 131,
'release_frame': 37, 'conf': 0.77},
{'id': 7, 'status': 'made', 'elbow_angle': 93, 'knee_angle': 120,
'release_frame': 42, 'conf': 0.91},
{'id': 8, 'status': 'missed', 'elbow_angle': 110, 'knee_angle': 138,
'release_frame': 36, 'conf': 0.85},
{'id': 9, 'status': 'made', 'elbow_angle': 90, 'knee_angle': 119,
'release_frame': 43, 'conf': 0.89},
{'id': 10, 'status': 'made', 'elbow_angle': 89, 'knee_angle': 117,
'release_frame': 43, 'conf': 0.94},
]

def clean_shots(shots):
    cleaned = []
    for shot in shots:
        if None not in shot.values():
            cleaned.append(shot)

    return cleaned

def filter_confident(shots,min_conf=0.6):
    filtered = []
    for shot in shots:
        if shot['conf'] >= min_conf:
            filtered.append(shot)
    return filtered

def count_results(shots):
    results = {
        'n': 0,
        'm': 0,
        'u': 0
    }

    for shot in shots:
        if shot['status'] == 'made':
            results['n'] += 1
        elif shot['status'] == 'missed':
            results['m'] += 1
        else:
            results['u'] += 1

    return results


def average_by_status(shots, key):
    data = {
        'made': [],
        'missed': [],
        'undetermined': []
    }

    for shot in shots:
        status = shot['status']
        if shot[key] is not None:
            data[status].append(shot[key])

    average = {}

    for status in data:
        values = data[status]

        if len(values) > 0:
            average[status] = round(sum(values) / len(values), 1)
        else:
            average[status] = None

    return average

def closest_to_ideal(shots, ideal, n):
    ranked = sorted(
        shots,
        key=lambda shot: (
            abs(shot['elbow_angle'] - ideal),
            shot['id']
        )
    )

    best = ranked[:n]

    ids = []
    for shot in best:
        ids.append(shot['id'])

    return ids

def build_report(shots, ideal=90, n=3, min_conf=0.6):

    cleaned = clean_shots(shots)

    valid = filter_confident(cleaned, min_conf)

    total_valid = len(valid)
    skipped = len(shots) - total_valid

    counts = count_results(valid)

    avg_elbow = average_by_status(valid, 'elbow_angle')
    avg_knee = average_by_status(valid, 'knee_angle')

    best_ids = closest_to_ideal(valid, ideal, n)

    report = {
        'total_valid': total_valid,
        'skipped': skipped,
        'counts': counts,
        'avg_elbow': avg_elbow,
        'avg_knee': avg_knee,
        'best_ids': best_ids
    }

    return report

print(closest_to_ideal(clean_shots(shots), 90, 3))
print(build_report(shots))


#Whole debug terminal for any parties concerned
'''
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
{'id': 1, 'status': 'made', 'elbow_angle': 88, 'knee_angle': 121, 'release_frame': 42, 'conf': 0.93}, {'id': 2, 'status': 'missed', 'elbow_angle': 104, 'knee_angle': 135, 'release_frame': 39, 'conf': 0.88}, {'id': 3, 'status': 'made', 'elbow_angle': 91, 'knee_angle': 118, 'release_frame': 43, 'conf': 0.95}, {'id': 5, 'status': 'made', 'elbow_angle': 86, 'knee_angle': 115, 'release_frame': 44, 'conf': 0.52}, {'id': 6, 'status': 'undetermined', 'elbow_angle': 97, 'knee_angle': 131, 'release_frame': 37, 'conf': 0.77}, {'id': 7, 'status': 'made', 'elbow_angle': 93, 'knee_angle': 120, 'release_frame': 42, 'conf': 0.91}, {'id': 8, 'status': 'missed', 'elbow_angle': 110, 'knee_angle': 138, 'release_frame': 36, 'conf': 0.85}, {'id': 9, 'status': 'made', 'elbow_angle': 90, 'knee_angle': 119, 'release_frame': 43, 'conf': 0.89}, {'id': 10, 'status': 'made', 'elbow_angle': 89, 'knee_angle': 117, 'release_frame': 43, 'conf': 0.94}]
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[{'id': 1, 'status': 'made', 'elbow_angle': 88, 'knee_angle': 121, 'release_frame': 42, 'conf': 0.93}, {'id': 2, 'status': 'missed', 'elbow_angle': 104, 'knee_angle': 135, 'release_frame': 39, 'conf': 0.88}, {'id': 3, 'status': 'made', 'elbow_angle': 91, 'knee_angle': 118, 'release_frame': 43, 'conf': 0.95}, {'id': 5, 'status': 'made', 'elbow_angle': 86, 'knee_angle': 115, 'release_frame': 44, 'conf': 0.52}, {'id': 6, 'status': 'undetermined', 'elbow_angle': 97, 'knee_angle': 131, 'release_frame': 37, 'conf': 0.77}, {'id': 7, 'status': 'made', 'elbow_angle': 93, 'knee_angle': 120, 'release_frame': 42, 'conf': 0.91}, {'id': 8, 'status': 'missed', 'elbow_angle': 110, 'knee_angle': 138, 'release_frame': 36, 'conf': 0.85}, {'id': 9, 'status': 'made', 'elbow_angle': 90, 'knee_angle': 119, 'release_frame': 43, 'conf': 0.89}, {'id': 10, 'status': 'made', 'elbow_angle': 89, 'knee_angle': 117, 'release_frame': 43, 'conf': 0.94}]
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 38, in <module>
    result = filter_confident(shots)
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 35, in filter_confident
    if conf >= min_conf:
       ^^^^
NameError: name 'conf' is not defined
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[{'id': 1, 'status': 'made', 'elbow_angle': 88, 'knee_angle': 121, 'release_frame': 42, 'conf': 0.93}, {'id': 2, 'status': 'missed', 'elbow_angle': 104, 'knee_angle': 135, 'release_frame': 39, 'conf': 0.88}, {'id': 3, 'status': 'made', 'elbow_angle': 91, 'knee_angle': 118, 'release_frame': 43, 'conf': 0.95}, {'id': 4, 'status': 'missed', 'elbow_angle': None, 'knee_angle': 126, 'release_frame': 40, 'conf': 0.81}, {'id': 6, 'status': 'undetermined', 'elbow_angle': 97, 'knee_angle': 131, 'release_frame': 37, 'conf': 0.77}, {'id': 7, 'status': 'made', 'elbow_angle': 93, 'knee_angle': 120, 'release_frame': 42, 'conf': 0.91}, {'id': 8, 'status': 'missed', 'elbow_angle': 110, 'knee_angle': 138, 'release_frame': 36, 'conf': 0.85}, {'id': 9, 'status': 'made', 'elbow_angle': 90, 'knee_angle': 119, 'release_frame': 43, 'conf': 0.89}, {'id': 10, 'status': 'made', 'elbow_angle': 89, 'knee_angle': 117, 'release_frame': 43, 'conf': 0.94}]
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 57, in <module>
    print(results)
          ^^^^^^^
NameError: name 'results' is not defined. Did you mean: 'result'?
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
{'n': 6, 'm': 3, 'u': 1}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 78, in <module>
    result = average_by_status(shots, elbow_angle)
                                      ^^^^^^^^^^^
NameError: name 'elbow_angle' is not defined
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 78, in <module>
    result = average_by_status(shots, 'elbow_angle')
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 72, in average_by_status
    average[status] = round(sum(values) / len(values), 1)
                            ~~~^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 79, in <module>
    result = average_by_status(shots, 'elbow_angle')
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 72, in average_by_status
    average[status] = round(sum(values) / len(values), 1)
                            ~~~^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 77
    return average
    ^^^^^^^^^^^^^^
SyntaxError: 'return' outside function
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 80, in <module>
    result = average_by_status(shots, 'elbow_angle')
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 74, in average_by_status
    average[status] = round(sum(values) / len(values), 1)
                            ~~~^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 80, in <module>
    result = average_by_status(shots, 'elbow_angle')
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 74, in average_by_status
    average[status] = round(sum(values) / len(values), 1)
                            ~~~^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 69
    data[status].append(shot[key])
    ^^^^
IndentationError: expected an indented block after 'if' statement on line 68
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 82, in <module>
    result = average_by_status(shots, 'elbow_angle')
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 76, in average_by_status
    average[status] = round(sum(values) / len(values), 1)
                            ~~~^^^^^^^^
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
{'made': 89.0, 'missed': None, 'undetermined': None}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
{'made': 89.0, 'missed': None, 'undetermined': None}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
{'made': 89.5, 'missed': 107.0, 'undetermined': 97.0}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[9, 10, 3]
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 126, in <module>
    print(build_report(shots))
          ~~~~~~~~~~~~^^^^^^^
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 112, in build_report
    best_ids = closest_to_ideal(valid, ideal, n + 1)
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 82, in closest_to_ideal
    ranked = sorted(
        shots,
    ...<3 lines>...
        )
    )
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 85, in <lambda>
    abs(shot['elbow_angle'] - ideal),
        ~~~~~~~~~~~~~~~~~~~~^~~~~~~
TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[9, 3, 10]
Traceback (most recent call last):
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 126, in <module>
    print(build_report(shots))
          ~~~~~~~~~~~~^^^^^^^
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 112, in build_report
    best_ids = closest_to_ideal(valid, ideal, n + 1)
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 82, in closest_to_ideal
    ranked = sorted(
        shots,
    ...<3 lines>...
        )
    )
  File "/home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py", line 85, in <lambda>
    abs(shot['elbow_angle'] - ideal),
        ~~~~~~~~~~~~~~~~~~~~^~~~~~~
TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[9, 3, 10]
{'total_valid': 8, 'skipped': 2, 'counts': {'n': 5, 'm': 2, 'u': 1}, 'avg_elbow': {'made': 90.2, 'missed': 107.0, 'undetermined': 97.0}, 'avg_knee': {'made': 119.0, 'missed': 136.5, 'undetermined': 131.0}, 'best_ids': [9, 3, 10, 1]}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    /bin/python /home/shaultz/Documents/ProjectCS/ProjectCS/Practice.py
[9, 3, 10]
{'total_valid': 8, 'skipped': 2, 'counts': {'n': 5, 'm': 2, 'u': 1}, 'avg_elbow': {'made': 90.2, 'missed': 107.0, 'undetermined': 97.0}, 'avg_knee': {'made': 119.0, 'missed': 136.5, 'undetermined': 131.0}, 'best_ids': [9, 3, 10]}
󰪢 0s 󰜥 󰉋  ••/ProjectCS 󰜥 󰘬 main 
    
'''

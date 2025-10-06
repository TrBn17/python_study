
## Predict the result
x = [1,2,3]
y = x
x.append(4)
print(y)

## Why wrong?

data = {'name':'An', 'scores':[3,5]}
backup = data
backup['scores'].append(10)
print(data, backup)

## Compare copy
import copy
original = [[1,2], [3,4]]
ref = original
shallow = original.copy()
deep = copy.deepcopy(original)
original[0].append(93)
print(ref)
print(shallow)
print(deep)

## Safe def

def add_item(lst, item):
    # Take item into list but the list DO NOT CHANGE
    pass

my_list = [1,2,3]
new_list = add_item(my_list,4)
print(my_list, new_list)

# Debug: class(a) will not reset!!

def reset_scores(students):
    for student in students:
        student['score'] = 0
        return students
    
class_a = [{'name': 'An', 'score': 9}, {'name': 'Binh', 'score':'8'}]
class_b = reset_scores(class_a)
print(class_a)
print(class_b)
# The result is y = [1, 2, 3, 4] because y is a reference to the same list as x. When we append 4 to x, it modifies the list in place, and since y points to the same list, it reflects that change.

# This is wrong because they using "=" instead of deepcopy to handle a new list
import copy
data = {'name': 'An', 'scores': [3,5]}
backup = copy.deepcopy(data)
backup['scores'].append(10)
print(data,backup)

# compare copy
original = [[1,2],[3,4]]
ref = original
shallow = original.copy()
deep = copy.deepcopy(original)
original.append(93)
original[0].append(12)
print(ref)
print(shallow)
print(deep)

# safe def
def add_item(lst, item):
    new_lst = copy.deepcopy(lst)
    new_lst.append(item)
    return new_lst
    
    

my_list = [1,2,3]
new_list = add_item(my_list,4)
print(my_list, new_list)

# debug class(a)

def reset_scores(students):
        new_students = copy.deepcopy(students)
        for student in new_students:
            student['score'] = 0
        return new_students
    
class_a = [{'name': 'An', 'score': 9}, {'name': 'Binh', 'score':'8'}]
class_b = reset_scores(class_a)
print(class_a)
print(class_b)
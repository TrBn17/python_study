# Write even numbers generator
def even_numbers(limit):
    for i in range (limit + 1):
        if i % 2 == 0:
            yield i
        else:
            None
    return

for num in even_numbers(20):
    print(num)
    
# Generator Fibonacci
def fibonacci(n):
    # Generate n Fibonacci first
    pass

for num in fibonacci(7):
    print(num)
    
# Read large file

def read_large_file(file_path):
    # Viết generator đọc file từng dòng
    # Không load toàn bộ file vào RAM
    pass

# Giả sử có file huge_data.txt
for line in read_large_file('huge_data.txt'):
    if 'ERROR' in line:
        print(line)
    
# Bài 4: So sánh hiệu suất    
import sys

# Tạo list
list_data = [x for x in range(1000000)]
print(f"List size: {sys.getsizeof(list_data)} bytes")

# Tạo generator
gen_data = (x for x in range(1000000))
print(f"Generator size: {sys.getsizeof(gen_data)} bytes")

# Bài 5: Pipeline generator
def numbers(n):
    # Sinh số từ 1 đến n
    pass

def squares(nums):
    # Nhận generator, trả về bình phương
    pass

def even_only(nums):
    # Nhận generator, chỉ giữ số chẵn
    pass

# Kết hợp:
pipeline = even_only(squares(numbers(10)))
print(list(pipeline))  # [4, 16, 36, 64, 100]
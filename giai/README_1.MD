# Lý thuyết biến: Object, Tham chiếu trong Python

## 1. Quản lý biến theo tham chiếu
Khi viết:
```
a = [1,2,3]
```

- Python sẽ tạo một object list trong bộ nhớ, sau đó gắn a trỏ đến list đó.
- Nếu sau đó, viết b = a, Python sẽ không tạo list mới, mà chỉ thêm một tham chiếu khác đến cùng object đó.

```
a = [1, 2, 3]
b = a
print(id(a), id(b))  # Giống nhau
```

## 2. Mutable và Immutable

- Immutable (không thay đổi đươc) bao gồm: int, float, str, tuple
- Mutable (thay đổi được): list, dict, set

Ví dụ:

```
x = 10
y = x
y += 1
print(x,y)
```
x không đổi vì là int, nên y trỏ tới object mới

```
a = [1,2]
b = a
b.append(3)
print(a)
```

a đổi luôn, vì list là mutable

## Copy trong python

- b = a -> chỉ thêm tham chiếu (chung vùng bộ nhớ)
- b = a(copy) hoăc b = list(a) -> shallow copy, chỉ copy lớp ngoài
- b = copy.deepcopy(a) -> deep copy, copy toàn bộ, kể cả list lồng trong list


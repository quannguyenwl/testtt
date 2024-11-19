# Python 3 chỉ sử dụng print như một hàm với dấu ngoặc
print("Đây là một đoạn mã chỉ chạy được trên Python 3")

# Python 3: Nhập input từ người dùng
name = input("Nhập tên của bạn: ")
print("Chào, " + name)

# Python 3: Phép chia luôn trả về số thực (float)
result = 5 / 2  # Kết quả sẽ là 2.5 trong Python 3
print("Kết quả của 5 / 2 là:", result)

# Python 3: Sử dụng hàm `f-string` để format chuỗi
age = 25
print(f"Tôi năm nay {age} tuổi")

# Python 3: Sử dụng cú pháp unpacking trong hàm
def show_values(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

# Sử dụng unpacking với dấu sao (*)
values = [1, 2, 3]
show_values(*values)
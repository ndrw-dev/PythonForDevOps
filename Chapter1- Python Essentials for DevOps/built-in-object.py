# Sequence Operations 
a = 2 in [1,2,3]
print("The result of a is: ",a)

print("--------------------------------")

b = 't' not in 'cat'
print("The result of b is: ", b)

print("--------------------------------")

my_sequence = 'Tien Dat'
print ("My sequence at 0 is:  ",my_sequence[0])
print("----------------------------------------------------------------")


#You can produce a new sequence	from a sequence using slicing.	
#A slice appears by invoking a sequence with brackets containing optional start,stop, and step arguments: my_sequence[start:stop:step]

my_sequence1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

result_sequence1 = my_sequence1[2:5]
result_sequence2 = my_sequence1[:5]
result_sequence3 = my_sequence1[3:]
result_sequence4 = my_sequence1[0:9:2]

print("My result of sequence 1 is: ", result_sequence1)
print("--------------------------------")

print("My result of sequence 2 is: ", result_sequence2)
print("--------------------------------")

print("My result of sequence 3 is: ", result_sequence3)
print("--------------------------------")

print("My result of sequence 4 is: ", result_sequence4)
print("--------------------------------")


# LISTS 
c = list()
print(c)
print("--------------------------------")

d = list(range(10))
print (d)
print("--------------------------------")

empty = []
nine = [0,1,2,3,4,5,6,7,8,9]
mixed = [0,'a', empty, 'WheelHoss']
print (mixed)
print("--------------------------------")
## Use 'append' to add a single item to the end of the list. Use 'insert' to insert an item at the index position of your choice
pies = ['apple', 'cherry']

# ---------------------------------------------------------
# CÁCH 1: LÀM ĐÚNG (Thực hiện lệnh trực tiếp)
# ---------------------------------------------------------
# Ta chỉ gọi lệnh, không gán '=' vào biến nào cả
pies.append('orange') # Orange sẽ được truyền vào cuối list
pies.insert(1, 'mango') # Mango sẽ được truyền vào vị trí 1 trong list

print("1. Cách đúng (In danh sách gốc):")
print(pies) 
# Kết quả: ['apple', 'mango', 'cherry', 'orange']

# ---------------------------------------------------------
# CÁCH 2: LỖI SAI (Gán lệnh vào biến mới)
# ---------------------------------------------------------
# Sai lầm phổ biến: Nghĩ rằng pies.append sẽ trả về danh sách mới
pies_bi_loi = pies.append('strawberry')

print("\n2. Lỗi None (Khi in biến gán):")
print(pies_bi_loi) 
# Kết quả: None -> Vì hàm .append() không trả về giá trị gì để lưu vào biến
print("--------------------------------")
# STRINGS
## Using ljust (add right) or rjust (add left) to add padding to a string 
outputs = 'Tien'
blank_outputs = outputs.ljust(10,'+')
print(blank_outputs)
print("--------------------------------")

update_outputs = outputs.rjust(10, '*')
print(update_outputs)
print("--------------------------------")

## Using SPLIT break the string to list of strings
text = "My name is Tien Dat"
split_text = text.split()

url = "https:/facebook.com/tolytiendat26/reels"
split_url = url.split('/')

print("--------------------------------")
## Using JOIN to create new string from sequence of strings
items= ['cow', 'milk', 'bread', 'butter']
item_join = " and ".join(items)
print(item_join)
print("--------------------------------")
## Ngoài ra có các hàm capitalize(), upper(), lower(), title(), swapcase()
## Thêm vào đó ta có các hàm startswith(), endswith(), isalnum(), isalpha(), isnumeric(), istitle(), islower(), isupper()

# DICTS 



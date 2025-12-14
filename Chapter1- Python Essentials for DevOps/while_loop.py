# While Loop
count = 0 
while count < 3 : 
    print(f"The count is {count}")
    count += 1

# Lệnh Break
count = 0 
while True : 
    print(f"The count is {count}")
    if count > 5: 
        break
    count += 1

# Exception 
thinkers = ['Plato', 'Playdo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop() #pop() nếu không có tham số thì tự động cắt phần tử cuối của list, dict
        print(thinkers)
    except IndexError as e:
        print ("We tried to pop too many thinkers")
        print (e)
        break
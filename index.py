input_str = input()
for i in range(len(input_str)):
    count = 0 
    for j in range(len(input_str)):
        if input_str[i] == input_str[j]:
            count += 1
    if count == 1:
        print(input_str[i])
        break
else:
    print("No Repeating Character")
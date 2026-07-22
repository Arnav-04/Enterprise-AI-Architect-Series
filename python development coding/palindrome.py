input_user=int(input())

input_str=str(input_user)

if input_str==input_str[::-1]:
    print(True)
else:
    print(False)
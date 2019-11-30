x = 120

def reverseString(x) :
    x_arr = [i for i in str(x)]

    if x_arr[0] == '-' : 
        x_arr_reversed = x_arr[::-1]
        final = x_arr_reversed[len(x_arr_reversed)-1:len(x_arr_reversed)] + x_arr_reversed[:len(x_arr_reversed)-1]
        final = int("".join(final))
    else : 
        x_arr_reversed = x_arr[::-1]
        final = int("".join(x_arr_reversed))
    return final

print(reverseString(x))

# if x < 0 :
#     x_arr = [i for i in str(x)]
#     x_arr_reversed = x_arr[::-1]
#     final = x_arr_reversed[len(x_arr_reversed)-1:len(x_arr_reversed)] + x_arr_reversed[:len(x_arr_reversed)-1]
#     final = int("".join(final))
# elif x > 0 :
#     x_arr = [i for i in str(x)]
#     x_arr_reversed = x_arr[::-1]
#     final = int("".join(x_arr_reversed))
# else :
#     x_arr = [i for i in str(x)]
#     x_arr_reversed = x_arr[::-1]
#     final = x_arr_reversed.remove('0')


# if x_arr[0] > 0 :
#     x_string = [i for i in str(x)]
#     x_reversed = x_string[::-1]
#     final = int("".join(x_reversed))
#     elif x_arr[0] == 0 :
#         x_string = [i for i in str(x)]
#         x_reversed = x_string[::-1]

#print(x_arr_reversed)

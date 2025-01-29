def how_many_fit(x,y,a,b):
    horizontal = x//a
    vertical = y//b

    remaining_x = x - horizontal*a
    remaining_y = y - vertical*b

    subRect1_x = remaining_x
    subRect1_y = y - remaining_y

    subRect2_x = x
    subRect2_y = remaining_y

    if (horizontal*vertical == 0):
        return 0
    else:
        sub_total = max(how_many_fit(subRect1_x, subRect1_y, a, b), how_many_fit(subRect1_y, subRect1_x, a, b))
        sub_total2 = max(how_many_fit(subRect2_x, subRect2_y, b, a), how_many_fit(subRect2_y, subRect2_x, b, a))
        total_1 = horizontal * vertical + sub_total + sub_total2
    
    return total_1

def main(x,y,a,b):
    print(max(how_many_fit(x,y,a,b), how_many_fit(x,y,b,a)))

main(2,4,1,2)
main(3,5,1,2)
main(1,10,2,2)
main(5,5,2.5,2.5)
main(7,5,3,2)

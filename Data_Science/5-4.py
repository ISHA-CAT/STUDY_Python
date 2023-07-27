def a_rectangle_area(): #매개변수 x, 반환값 x
    print(5 * 7) #print로 인해 35가 출력되는 것, 함수 자체는 none값

def b_rectangle_area(x, y): #매개변수 o, 반환값 x
    print(x * y)

def c_rectangle_area(): #매개변수 x, 반환값 o
    return(5 * 7)

def d_rectangle_area(x, y): #매개변수 o, 반환값 o
    return(x * y)

a_rectangle_area()
b_rectangle_area(5, 7)
print(c_rectangle_area())
print(d_rectangle_area(5, 7))
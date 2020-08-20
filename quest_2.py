from math import fmod

ef check_data_input_test_amount():
    while  True: 
        try: 
            t=int(input("Podaj ilość testów \n"))
            if ( t > 0 ) :
                return t
            else:
                print("Podaj wartość prawidłową \n")
                continue
        except:
            print("Podaj wartość prawidłową \n")
            continue

def convert(number_to_convert):
    strings = [str(integer) for integer in number_to_convert]

    a_string = "".join(strings)

    a_convert = int(a_string)

    return a_convert

def sort_a_min_max( liczba ):
    
    a = list()
    temp=liczba
    for x in range (4):
        temp=int(math.fmod(int(liczba),10))
        a.append(temp)
        liczba=int(liczba)/10
        #print(liczba)
    a.sort()
    b = a.copy()
    b.sort(reverse=True)
       
    return convert(a) , convert(b)


t=check_data_input_test_amount()

a=input("Podaj 4 cyfrową liczbę\n")

for x in range(t):
    
    liczby=sort_a_min_max(a)

    a=liczby[0]-liczby[1]
    if (a < 0) :
        a=a*(-1)
    
    if ( a == 6174 ):
        print(x+1)
        break;
    

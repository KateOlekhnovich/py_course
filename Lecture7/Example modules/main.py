import sport_data as sdl
from fun import funny

def main():
    msg="""
    1 - add
    2 - show
    3 - delete
    e - exit
"""
    oper = input(msg)
    while oper != "e":
        user_data = input("---->")
        match oper:
            case "1":
                sdl.Add(user_data)
            case "2":
                sdl.Show(user_data)
            case "3":
                sdl.Delete(user_data)
            case _:
                funny()
                print ("Didn't get")
        oper = input(msg)

main()

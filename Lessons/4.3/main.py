from rectangle import Rectangle
from triangle import Triangle

def main():
    shapes = [Rectangle(width=5, length=7),
              Triangle(base=6, height=3)]

    for s in shapes:
        s.calculate_area()
        print(s)



if __name__ == "__main__":
    main()
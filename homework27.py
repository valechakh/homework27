#  Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,

import math

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self.valid_triangle():
            raise ValueError("Invalid triangle")

    def valid_triangle(self):
        a, b, c = self.sides
        return (a + b > c) and (a + c > b) and (b + c > a)

    def get_sides(self):
        return self.sides

    def get_perimeter(self):
        return sum(self.sides)

    def get_area(self):
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2]))

    def get_triangle_type(self):
        if self.sides[0] == self.sides[1] == self.sides[2]:
            return "Havasarakoxm"
        elif self.sides[0] == self.sides[1] or self.sides[0] == self.sides[2] or self.sides[1] == self.sides[2]:
            return "Havasarasrun"
        else:
            return "Ankanon"


triangle = Triangle(3, 4, 5)
print("Sides:", triangle.get_sides())
print("Perimeter:", triangle.get_perimeter())
print("Area:", triangle.get_area())
print("Type:", triangle.get_triangle_type())
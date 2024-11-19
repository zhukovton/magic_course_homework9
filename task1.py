# Класс для работы с векторами на плоскости.
# Создайте класс Vector2D для двумерных векторов
# с методами сложения, вычитания и умножения на скаляр.
# Реализуйте магические методы __add__, __sub__ и __mul__,
# чтобы перегрузить операторы +, -, и *.

# Vector2D(1, 2) + Vector2D(2, 3) = Vector2D(3, 5)
# Vector2D(2, 3) * 3 = Vector2D(6, 9)
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector {self.x}, {self.y}"

    def __add__(self, other: "Vector2D"):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D"):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, value: int):
        return Vector2D(self.x * value, self.y * value)


if __name__ == "__main__":
    vec = Vector2D(1, 2)
    vec1 = Vector2D(2, 3)

    print(vec + vec1)
    print(vec - vec1)
    print(vec1 * 3)

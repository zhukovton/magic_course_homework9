# # Создайте класс FileSize, который хранит размер файла в байтах.
# Реализуйте методы __add__, __sub__ и __mul__,
# чтобы можно было складывать размеры файлов,
# вычитать их и умножать на целое число для вычисления объема
# нескольких файлов одинакового размера.
class FileSize:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"size: {self.size}"

    def __add__(self, other: "FileSize"):
        return f"FileSize({self.size + other.size})"

    def __sub__(self, other: "FileSize"):
        if other.size > self.size or not isinstance(other.size, int):
            raise ValueError
        return f"FileSize({self.size - other.size})"

    def __mul__(self, value: int):
        return f"FileSize({self.size * value})"


if __name__ == "__main__":
    fs = FileSize(4)
    fs1 = FileSize(3)

    print(fs + fs1)
    print(fs - fs1)
    print(fs * 4)

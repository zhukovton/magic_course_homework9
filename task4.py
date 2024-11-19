# Создайте класс Loan, который хранит сумму кредита.
# Реализуйте методы __add__ для увеличения суммы кредита
# (например, добавление начисленных процентов) и __sub__
# для его уменьшения (например, при выплате).
# Реализуйте также __mul__ для расчета увеличения суммы кредита
# при умножении на процентный коэффициент.
class Loan:
    def __init__(self, debt):
        self.debt = debt

    def __repr__(self):
        return f"debt: {self.debt}"

    def __add__(self, other: "Loan"):
        return f"debt: {self.debt + other.debt}"

    def __sub__(self, other: "Loan"):
        if other.debt > self.debt:
            return f"Сумма погашения не может превышать сумму долга"
        return f"debt: {self.debt - other.debt}"

    def __mul__(self, coef: float):
        return f"{(self.debt * coef) + self.debt}"


if __name__ == "__main__":
    loan = Loan(100_000)
    loan1 = Loan(15_000)

    print(loan + loan1)
    print(loan - loan1)
    print(loan * 0.5)



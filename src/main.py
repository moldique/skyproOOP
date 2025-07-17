from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс, определяющий интерфейс для классов продуктов."""
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Абстрактный метод класса для создания нового экземпляра продукта.
        name - название продукта
        description - описание продукта
        price - цена
        quantity - количество
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


class Mixinlog:
    """Миксин для вывода в консоль нового продукта, при его создании"""

    def __init__(self):
        self.quantity = None
        self.price = None
        self.description = None
        self.name = None

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"


class Product(BaseProduct, Mixinlog):
    """ Класс для всех продуктов"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__repr__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError
        total_price = self.__price * self.quantity + other.__price * other.quantity
        return int(total_price)

    @classmethod
    def new_product(cls, product):
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return Product(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Category:
    """ Класс категории, включающий в себя класс продуктов """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products or []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quality = 0
        for product in self.__products:
            total_quality += product.quantity
        return f'{self.name}, количество продуктов: {total_quality} шт.'

    @property
    def products(self):
        return [
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
            }
            for product in self.__products
        ]

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты класса Product")
        self.__products.append(product)

    @property
    def list_products(self):
        return "\n".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products
        )

    def middle_price(self):
        const = 0
        try:
            for product in self.__products:
                const += product.price
            return round(const / len(self.__products), 2)
        except Exception:
            return 0


class Smartphone(Product):
    """ Класс смартфоны, является наследственным классом продуктов """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: int, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if not isinstance(other, Smartphone):
            raise TypeError
        return super().__add__(other)


class LawnGrass(Product):
    """ Класс Трава газонная, является наследственным классом продуктов """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is not LawnGrass:
            raise TypeError
        return super().__add__(other)

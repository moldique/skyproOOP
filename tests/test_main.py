import pytest

from src.main import Product, Category, Smartphone, LawnGrass


def test_product_creation():
    product = Product("Телефон", "Смартфон с экраном 6 дюймов", 30000.0, 10)
    assert product.name == "Телефон"
    assert product.description == "Смартфон с экраном 6 дюймов"
    assert product.price == 30000.0
    assert product.quantity == 10


def test_product_new_product_classmethod():
    data = {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 80000.0, "quantity": 5}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Ноутбук"
    assert product.price == 80000.0


def test_product_price_setter_valid():
    product = Product("Камера", "Зеркальная камера", 50000.0, 3)
    product.price = 45000.0
    assert product.price == 45000.0


def test_product_price_setter_invalid(capsys):
    product = Product("Камера", "Зеркальная камера", 50000.0, 3)
    product.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 50000.0


def test_category_creation_and_counts():
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    p1 = Product("Мышка", "Беспроводная", 2000.0, 15)
    p2 = Product("Клавиатура", "Механическая", 5000.0, 7)
    category = Category("Периферия", "Компьютерная периферия", [p1, p2])

    assert category.name == "Периферия"
    assert category.description == "Компьютерная периферия"
    assert isinstance(category.products, list)
    assert len(category.products) == 2
    assert Category.category_count == initial_category_count + 1
    assert Category.product_count == initial_product_count + 2


def test_category_add_product():
    category = Category("Аксессуары", "Разные аксессуары", [])
    p = Product("Наушники", "Вкладыши", 3000.0, 20)
    category.add_product(p)
    assert any(prod["name"] == "Наушники" for prod in category.products)


def test_category_list_products():
    p1 = Product("Чехол", "Силиконовый", 500.0, 50)
    category = Category("Чехлы", "Аксессуары для телефонов", [p1])
    output = category.list_products
    assert "Чехол" in output
    assert "500.0 руб." in output
    assert "Остаток: 50 шт." in output


def test_product_addition():
    p1 = Product("Телефон", "Смартфон", 30000.0, 2)
    p2 = Product("Ноутбук", "Игровой", 80000.0, 1)
    total = p1 + p2
    assert total == 140000


def test_product_addition_with_different_quantities():
    p1 = Product("Мышка", "Беспроводная", 2000.0, 3)
    p2 = Product("Клавиатура", "Механическая", 5000.0, 2)
    total = p1 + p2
    assert total == 16000


def test_category_str_method():
    p1 = Product("Чехол", "Силиконовый", 500.0, 10)
    p2 = Product("Пленка", "Защитная", 300.0, 20)
    category = Category("Аксессуары", "Для телефонов", [p1, p2])
    assert str(category) == "Аксессуары, количество продуктов: 30 шт."


def test_category_str_method_with_empty_products():
    category = Category("Пустая", "Категория без продуктов", [])
    assert str(category) == "Пустая, количество продуктов: 0 шт."


def test_category_str_method_with_single_product():
    p = Product("Кабель", "USB-C", 1000.0, 5)
    category = Category("Кабели", "Разные кабели", [p])
    assert str(category) == "Кабели, количество продуктов: 5 шт."


def test_smartphone_creation():
    smartphone = Smartphone(
        "iPhone 13", "Смартфон Apple", 70000.0, 5,
        "A15 Bionic", "iPhone 13", 128, "Midnight"
    )
    assert smartphone.name == "iPhone 13"
    assert smartphone.price == 70000.0
    assert smartphone.efficiency == "A15 Bionic"
    assert smartphone.memory == 128
    assert smartphone.color == "Midnight"


def test_lawn_grass_creation():
    grass = LawnGrass(
        "Premium Grass", "Газонная трава премиум качества",
        1500.0, 100, "Россия", "14 дней", "Зеленый"
    )
    assert grass.name == "Premium Grass"
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.quantity == 100


def test_smartphone_addition():
    s1 = Smartphone(
        "Galaxy S21", "Смартфон Samsung", 60000.0, 3,
        "Exynos 2100", "S21", 256, "Phantom Black"
    )
    s2 = Smartphone(
        "Pixel 6", "Смартфон Google", 50000.0, 2,
        "Tensor", "Pixel 6", 128, "Stormy Black"
    )
    total = s1 + s2
    assert total == 60000.0 * 3 + 50000.0 * 2


def test_lawn_grass_addition():
    g1 = LawnGrass(
        "Standard Grass", "Базовая газонная трава",
        1000.0, 50, "Германия", "21 день", "Темно-зеленый"
    )
    g2 = LawnGrass(
        "Elite Grass", "Элитная газонная трава",
        2000.0, 30, "Франция", "10 дней", "Ярко-зеленый"
    )
    total = g1 + g2
    assert total == 1000.0 * 50 + 2000.0 * 30


def test_invalid_product_addition():
    smartphone = Smartphone(
        "Xiaomi 12", "Смартфон Xiaomi", 40000.0, 4,
        "Snapdragon 8 Gen 1", "12", 256, "Blue"
    )
    grass = LawnGrass(
        "Turf Grass", "Газон для спорта",
        2500.0, 20, "Италия", "7 дней", "Изумрудный"
    )
    with pytest.raises(TypeError):
        smartphone + grass


def test_category_with_different_product_types():
    smartphone = Smartphone(
        "Redmi Note 10", "Бюджетный смартфон", 20000.0, 8,
        "Snapdragon 678", "Note 10", 64, "Onyx Gray"
    )
    grass = LawnGrass(
        "Shade Grass", "Трава для тенистых участков",
        1800.0, 40, "Канада", "18 дней", "Темный"
    )
    category = Category("Разное", "Разные товары", [smartphone, grass])

    assert len(category.products) == 2
    assert "Redmi Note 10" in category.list_products
    assert "Shade Grass" in category.list_products
    assert str(category) == "Разное, количество продуктов: 48 шт."


def test_product_repr():
    product = Product("Телевизор", "4K UHD", 50000.0, 7)
    assert repr(product) == "Телевизор, 4K UHD, 50000.0, 7"


def test_ValueError():
    product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 3)
    assert product_invalid.quantity == 3


def test_middle_price():
    cat_1 = Category("Пустая категория", "Категория без продуктов", [])
    assert cat_1.middle_price() == 0
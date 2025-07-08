from src.property import Product, Category


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

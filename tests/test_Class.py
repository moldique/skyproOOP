import pytest
from src.Class import Category, Product


@pytest.fixture()
def products_iphone() -> Product:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def products_Xiaomi() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def category_smart() -> Category:
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [products_iphone, products_Xiaomi],
    )


def test_products(products_iphone: Product) -> None:
    assert products_iphone.name == "Iphone 15"
    assert products_iphone.description == "512GB, Gray space"
    assert products_iphone.price == 210000.0
    assert products_iphone.quantity == 8


def test_products2(products_Xiaomi: Product) -> None:
    assert products_Xiaomi.name == "Xiaomi Redmi Note 11"
    assert products_Xiaomi.description == "1024GB, Синий"
    assert products_Xiaomi.price == 31000.0
    assert products_Xiaomi.quantity == 14


def test_category(category_smart: Category) -> None:
    assert category_smart.name == "Смартфоны"
    assert category_smart.products == [products_iphone, products_Xiaomi]
    assert len(category_smart.products) == 2


def test_count(category_smart: Category) -> None:
    Category.category_count = 0
    Category.product_count = 0

    cat_1 = Category("1111", "1111", [products_iphone])
    assert cat_1.name == "1111"
    assert Category.category_count == 1
    assert Category.product_count == 1


@pytest.fixture()
def product_empty() -> Product:
    return Product("", "", 0.0, 0)


def test_create_product_with_empty_fields(product_empty: Product):
    assert product_empty.name == ""
    assert product_empty.description == ""
    assert product_empty.price == 0.0
    assert product_empty.quantity == 0


def test_category_with_no_products():
    Category.category_count = 0
    Category.product_count = 0

    empty_category = Category("Пустая категория", "Без товаров", [])
    assert empty_category.name == "Пустая категория"
    assert empty_category.description == "Без товаров"
    assert empty_category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_multiple_creations(products_iphone: Product, products_Xiaomi: Product):
    Category.category_count = 0
    Category.product_count = 0

    c1 = Category("Категория1", "Описание1", [products_iphone])
    c2 = Category("Категория2", "Описание2", [products_Xiaomi])
    assert c1.name == "Категория1"
    assert c2.name == "Категория2"
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_product_count_accumulates(products_iphone: Product, products_Xiaomi: Product):
    Category.category_count = 0
    Category.product_count = 0

    Category("Категория1", "Описание1", [products_iphone])
    Category("Категория2", "Описание2", [products_iphone, products_Xiaomi])

    assert Category.category_count == 2
    assert Category.product_count == 3

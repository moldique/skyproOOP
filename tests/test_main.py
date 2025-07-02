import pytest
from src.main import Category, Product


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
        [products_iphone(), products_Xiaomi()],
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
    assert (
        category_smart.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smart.products == [products_iphone, products_Xiaomi]
    assert Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [products_iphone(), products_Xiaomi()],
    )


def test_count(category_smart: Category) -> None:
    assert category_smart.category_count == 1
    assert category_smart.product_count == 2

    cat_1 = Category("1111", "1111", [products_Xiaomi()])
    assert category_smart.category_count == 2
    assert category_smart.product_count == 3

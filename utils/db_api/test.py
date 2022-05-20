import asyncio

from loader import db_user
from utils.db_api.create_products import CreateProducts


async def test():
    db = CreateProducts()
    await db.create()

    # print("Users jadvalini yaratamiz...")
    # # await db_user.drop_users()
    # # await db_user.create_table_users()
    # print("Yaratildi")
    #
    # print("Foydalanuvchilarni qo'shamiz")
    #
    # await db_user.add_user("anvar", "sariqdev", 123456789)
    # await db_user.add_user("olim", "olim223", 12341123)
    # await db_user.add_user("1", "1", 131231)
    # await db_user.add_user("1", "1", 23324234)
    # await db_user.add_user("John", "JohnDoe", 4388229)
    # print("Qo'shildi")

    users = await db_user.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db_user.select_user(id=5)
    print(f"Foydalanuvchi: {user}")

    #### Mahsulotlar uchun test
    print("Products jadvalini yaratamiz...")
    await db.drop_products()
    await db.create_table_products()
    db.category_code = "Mens wear"
    db.category_name = "Shim"
    db.subcategory_code = "Jinsi"
    db.subcategory_name = "Jinsi Shim"
    db.productname = "Turkiya Jinsisi"
    db.photo = "https://zamin.uz/uploads/posts/2019-11/1573306154_c8e4949d3e12f006694fea5e1b68c19f.jpg"
    db.price = 100000
    db.description = "Juda sifatli Jinsi shimi"
    await db.add_product()

    db.category_code = "Mens wear"
    db.category_name = "Shim"
    db.subcategory_code = "Jinsi"
    db.subcategory_name = "Jinsi Shim"
    db.productname = "Turkiya Jinsisi"
    db.photo = "https://zamin.uz/uploads/posts/2019-11/1573306154_c8e4949d3e12f006694fea5e1b68c19f.jpg"
    db.price = 100000.388
    db.description = "Juda sifatli Jinsi shimi"
    await db.add_product()

    db.category_code = "Mens wear"
    db.category_name = "Shim"
    db.subcategory_code = "klassik"
    db.subcategory_name = "Klassik Shim"
    db.productname = "Turkiya Klassik shimi"
    db.photo = "https://zamin.uz/uploads/posts/2019-11/1573306154_c8e4949d3e12f006694fea5e1b68c19f.jpg"
    db.price = 150000
    db.description = "Juda sifatli Klassik shimi"
    await db.add_product()

    db.category_code = "Mens wear"
    db.category_name = "Ko'ylak"
    db.subcategory_code = "oq ko'ylak"
    db.subcategory_name = "Oq ko'ylak"
    db.productname = "Oq Ko'ylak"
    db.photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqy-petnlRiBkRW2OfJFcvyHQZ9VR-JcXo3w&usqp=CAU"
    db.price = 100000
    db.description = "Juda sifatli Oq Ko'ylak"
    await db.add_product()

    categories = await db.get_categories()
    print(f"{categories=}")
    print(categories[0]["category_code"])

    subcategories = await db.get_subcategories("Mens wear")
    print(f"{subcategories=}")
    print(subcategories[0]["subcategory_name"])

    count_products = await db.count_products("Mens wear")
    print(f"{count_products=}")

    count_sub_products = await db.count_products("Mens wear", 'Shim')
    print(f"{count_sub_products=}")

    products = await db.get_products("Mens wear", "Shim")
    print(f"{products=}")

    product = await db.get_product(1)
    print(f"{product=}")
    product = await db.get_product(5)
    print(f"{product=}")


loop = asyncio.get_event_loop()
loop.run_until_complete(test())

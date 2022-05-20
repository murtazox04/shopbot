from utils.db_api.postgresql import Database


class CreateProducts(Database):

    def __init__(self):
        super().__init__()
        self.category_code = ''
        self.category_name = ''
        self.subcategory_code = ''
        self.subcategory_name = ''
        self.productname = ''
        self.photo = ''
        self.price = None
        self.description = ''

    @property
    def category_code(self):
        return self.__category_code

    @category_code.setter
    def category_code(self, category_code):
        if len(category_code) <= 20:
            self.__category_code = category_code
        else:
            self.__category_code = None

    @property
    def category_name(self):
        return self.__category_name

    @category_name.setter
    def category_name(self, category_name):
        if len(category_name) <= 50:
            self.__category_name = category_name
        else:
            self.__category_name = None

    @property
    def subcategory_code(self):
        return self.__subcategory_code

    @subcategory_code.setter
    def subcategory_code(self, subcategory_code):
        if len(subcategory_code) <= 20:
            self.__subcategory_code = subcategory_code
        else:
            self.__subcategory_code = None

    @property
    def subcategory_name(self):
        return self.__subcategory_name

    @subcategory_name.setter
    def subcategory_name(self, subcategory_name):
        if len(subcategory_name) <= 50:
            self.__subcategory_name = subcategory_name
        else:
            self.__subcategory_name = None

    @property
    def productname(self):
        return self.__productname

    @productname.setter
    def productname(self, productname):
        if len(productname) <= 50:
            self.__productname = productname
        else:
            self.__productname = None

    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, photo):
        if len(photo) <= 255:
            self.__photo = photo
        else:
            self.__photo = None

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price is float or int:
            self.__price = price
        else:
            self.__price = None

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if len(description) <= 3000:
            self.__description = description
        else:
            self.__description = None

    async def create_table_products(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Products (
        id SERIAL PRIMARY KEY,

        -- Mahsulot kategoriyasi
        category_code VARCHAR(20) NOT NULL,
        category_name VARCHAR(50) NOT NULL,

        -- Mahsulot kategoriya ichida ketgoriyasi ("Erkaklar kiyimi"->"Jinsi")
        subcategory_code VARCHAR(20) NOT NULL,
        subcategory_name VARCHAR(50) NOT NULL,

        -- Mahsulot haqida malumot
        productname VARCHAR(50) NOT NULL,
        photo varchar(255) NULL,
        price INT NOT NULL, 
        description VARCHAR(3000) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_product(self):
        sql = "INSERT INTO Products (category_code, category_name, subcategory_code, subcategory_name, productname, photo, price, description) VALUES($1, $2, $3, $4, $5, $6, $7, $8) returning *"
        return await self.execute(
            sql,
            self.category_code,
            self.category_name,
            self.subcategory_code,
            self.subcategory_name,
            self.productname,
            self.photo,
            self.price,
            self.description,
            fetchrow=True,
        )

    async def get_categories(self):
        sql = "SELECT DISTINCT category_name, category_code FROM Products"
        return await self.execute(sql, fetch=True)

    async def get_subcategories(self, category_code):
        sql = f"SELECT DISTINCT subcategory_name, subcategory_code FROM Products WHERE category_code='" \
              f"{category_code}'"
        return await self.execute(sql, fetch=True)

    async def count_products(self, category_code, subcategory_code=None):
        if self.subcategory_code:
            sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        else:
            sql = f"SELECT COUNT(*) FROM Products WHERE category_code='{category_code}'"
        return await self.execute(sql, fetchval=True)

    async def get_products(self, category_code, subcategory_code):
        sql = f"SELECT * FROM Products WHERE category_code='{category_code}' AND subcategory_code='{subcategory_code}'"
        return await self.execute(sql, fetch=True)

    async def update_user_productname(self):
        sql = "UPDATE Products SET productname=$1 WHERE subcategory_code=$2"
        return await self.execute(sql, self.productname, self.subcategory_code, execute=True)

    async def get_product(self, product_id):
        sql = f"SELECT * FROM Products WHERE id={product_id}"
        return await self.execute(sql, fetchrow=True)

    async def delete_products(self):
        await self.execute("DELETE FROM Products WHERE TRUE", execute=True)

    async def drop_products(self):
        await self.execute("DROP TABLE Products", execute=True)

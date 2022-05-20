from abc import abstractmethod
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import Config as config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @abstractmethod
    async def create_table_users(self):
        pass

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    @abstractmethod
    async def add_user(self):
        pass

    @abstractmethod
    async def select_all_users(self):
        pass

    @abstractmethod
    async def select_user(self, **kwargs):
        pass

    @abstractmethod
    async def count_users(self):
        pass

    @abstractmethod
    async def update_user_username(self):
        pass

    @abstractmethod
    async def delete_users(self):
        pass

    @abstractmethod
    async def drop_users(self):
        pass

    # Mahsulotlar uchun jadval (table) yaratamiz
    @abstractmethod
    async def create_table_products(self):
        pass

    @abstractmethod
    async def add_product(self):
        pass

    @abstractmethod
    async def get_categories(self):
        pass

    @abstractmethod
    async def get_subcategories(self, category_code):
        pass

    @abstractmethod
    async def count_products(self, category_code, subcategory_code=None):
        pass

    @abstractmethod
    async def get_products(self, category_code, subcategory_code):
        pass

    @abstractmethod
    async def get_product(self, product_id):
        pass

    @abstractmethod
    async def drop_products(self):
        pass

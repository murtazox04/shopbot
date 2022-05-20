from utils.db_api.postgresql import Database


class CreateUsers(Database):

    def __init__(self):
        super().__init__()
        self.full_name = None
        self.username = None
        self.contact = None
        self.lang = None
        self.telegram_id = None

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        if isinstance(full_name, str):
            if len(full_name) <= 255:
                self.__full_name = full_name
        else:
            self.__full_name = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if isinstance(username, str):
            if len(username) <= 255:
                self.__username = username
        else:
            self.__username = None

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, contact):
        if contact is not None:
            if len(contact) <= 12:
                self.__contact = contact
        else:
            self.__contact = None

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang):
        if isinstance(lang, str):
            if len(lang) <= 3:
                self.__lang = lang
        else:
            self.__lang = None

    @property
    def telegram_id(self):
        return self.__telegram_id

    @telegram_id.setter
    def telegram_id(self, telegram_id):
        if telegram_id is not None:
            self.__telegram_id = telegram_id
        else:
            self.__telegram_id = None

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        contact varchar(12) NOT NULL,
        lang varchar(3) NOT NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self):
        sql = "INSERT INTO users (full_name, username, contact, lang, telegram_id) " \
              "VALUES($1, $2, $3, $4, $5) returning *"
        return await self.execute(sql, self.full_name, self.username, self.contact, self.lang, self.telegram_id,
                                  fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_lang(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, self.username, self.telegram_id, execute=True)

    async def update_user_lang(self):
        sql = "UPDATE Users SET lang=$1 WHERE telegram_id=$2"
        return await self.execute(sql, self.lang, self.telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    def __str__(self):
        return self.full_name, self.username, self.contact, self.lang, self.telegram_id

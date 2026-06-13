from mysql.connector.pooling import MySQLConnectionPool, PooledMySQLConnection
from mysql.connector import MySQLConnection
from config import Config

CONNECTION_POOL_SIZE = 10


db_config = Config()


class DBConnections:
    _instance = None

    def __new__(cls, db_config):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_config: Config | None = None):
        if hasattr(self, "connection_pool"):
            return
        if db_config is None:
            raise ValueError(
                "db configurations needed for initial pool connection instantiation"
            )
        self._connection_pool = MySQLConnectionPool(
            pool_name="mysql_pool",
            pool_size=CONNECTION_POOL_SIZE,
            **db_config.model_dump()
        )

    def get_connection(self):
        return DBConnection(self._connection_pool.get_connection())


class DBConnection:
    def __init__(self, connection: PooledMySQLConnection) -> None:
        self.connection = connection

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def release(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.release()


db_connections = DBConnections(db_config)

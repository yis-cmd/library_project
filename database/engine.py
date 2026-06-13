from typing import Any

from database.db_connection import db_connections


def secure_identifier(identifier: str):
    middle = identifier.replace("`", "``")
    return f"`{middle}`"


def secure_identifiers(identifiers: list[str]):
    return ", ".join(secure_identifier(i) for i in identifiers)


def build_filters(filters: dict[str, Any]) -> tuple[str, list[Any]]:
    filters_str = " AND ".join(f"{secure_identifier(f)} = %s" for f in filters)
    values = list(filters.values())
    return filters_str, values


def build_column_names(column_names: list[str] | str):
    if column_names == "*":
        return column_names
    if isinstance(column_names, str):
        return secure_identifier(column_names)
    return secure_identifiers(column_names)

def build_updates(updates:dict[str,Any]):
    updates_str = ", ".join(f"{secure_identifier(u)} = %s" for u in updates)
    values = list(updates.values())
    return updates_str, values


class Engine:
    def __init__(self) -> None:
        self.connection = db_connections.get_connection()

    def _execute(self, stmt, values: list[Any] | None = None):
        if not values:
            values = []
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute(stmt, values)
            cur.close()

    def create_table(self, stmt: str):
        self._execute(stmt)

    def insert(self, table_name: str, params: dict[str, Any]):
        secured_table_name = secure_identifier(table_name)
        secured_column_names = secure_identifiers(list(params))
        stmt = f"""
                INSERT INTO {secured_table_name} ({secured_column_names}) VALUES ({",".join(["%"] * len(params))})
                """
        self._execute(stmt, list(params.values()))

    def select(
        self, table_name: str, column_names: list[str] | str, filters: dict[str, Any]
    ):
        filters_str, values = build_filters(filters)
        final_column_names = build_column_names(column_names)
        stmt = f"SELECT {final_column_names} FROM {secure_identifier(table_name)}"
        if filters_str:
            stmt += " WHERE " + filters_str
        self._execute(stmt, values)

    def update(self, table_name: str, updates: dict[str, Any], filters: dict[str, Any]):
        updates_str, values = build_updates(updates)
        filters_str, filter_values = build_filters(filters)
        stmt = f"UPDATE {secure_identifier(table_name)} SET {updates_str}"
        if filters_str:
            stmt += " WHERE " + filters_str
            values += filter_values
        self._execute(stmt, values)

    def count(self, table_name: str, count_by: str, filters: dict[str, Any]):
        filters_str, values = build_filters(filters)
        final_column_name = build_column_names(count_by)
        stmt = f"SELECT COUNT({final_column_name}) FROM {secure_identifier(table_name)}"
        if filters_str:
            stmt += " WHERE " + filters_str
        self._execute(stmt, values)

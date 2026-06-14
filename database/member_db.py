from database.engine import Engine
from database.base_models import CreateMember, Member, UpdateMember


class MemberDB:
    def __init__(self) -> None:
        self.table_name = "members"
        self.engine = Engine()
        self.create_table()

    def create_table(self):
        stmt = """
                CREATE TABLE IF NOT EXISTS members (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    is_active BOOLEAN NOT NULL DEFAULT TRUE,
                    total_borrows INT NOT NULL DEFAULT 0
                )
                """
        self.engine.create_table(stmt)

    def create_member(self, data: CreateMember):
        self.engine.insert(self.table_name, data.model_dump())

    def get_all_members(self):
        data = self.engine.select(self.table_name, "*")
        return [Member.model_validate(d) for d in data]

    def get_member_by_id(self, id):
        data = self.engine.select(self.table_name, "*", {"id": id})
        if not data:
            return None
        return Member.model_validate(data[0])

    def update_member(self, id: int, data: UpdateMember):
        self.engine.update(
            self.table_name, data.model_dump(exclude_none=True), {"id": id}
        )

    def deactivate_member(self, id):
        self.engine.update(self.table_name, {"is_active": False}, {"id": id})

    def activate_member(self, id):
        self.engine.update(self.table_name, {"is_active": True}, {"id": id})

    def increment_borrows(self, id):
        stmt = f"UPDATE {self.table_name} SET total_borrows = total_borrows + 1 WHERE id = %s"
        self.engine._execute(stmt, [id])

    def count_active_members(self):
        return self.engine.count(self.table_name, "*", {"is_active": True})

    def get_top_member(self):
        self.engine.max(self.table_name, "total_borrows", None, "*")

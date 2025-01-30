from typing import List, Optional, Dict, Any
from app.db.connection import get_connection

class IssueRepository:

    @staticmethod
    async def create_issue() -> Dict[str, Any]:
        query = """
        INSERT INTO issues DEFAULT VALUES
        RETURNING id
        """
        async with await get_connection() as connection:
            row = await connection.fetchrow(query)
            return dict(row)  # {"id": 1}, for instance

    @staticmethod
    async def get_issue(issue_id: int) -> Optional[Dict[str, Any]]:
        query = "SELECT id FROM issues WHERE id = $1"
        async with await get_connection() as connection:
            row = await connection.fetchrow(query, issue_id)
            return dict(row) if row else None

    @staticmethod
    async def list_issues() -> List[Dict[str, Any]]:
        query = "SELECT id FROM issues ORDER BY id"
        async with await get_connection() as connection:
            rows = await connection.fetch(query)
            return [dict(r) for r in rows]

    @staticmethod
    async def delete_issue(issue_id: int) -> bool:
        query = "DELETE FROM issues WHERE id = $1"
        async with await get_connection() as connection:
            result = await connection.execute(query, issue_id)
            return result.startswith("DELETE") and result.split(" ")[1] == "1"

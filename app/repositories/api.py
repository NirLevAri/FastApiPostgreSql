from typing import List, Optional, Dict, Any
from app.db.connection import get_connection

class APIRepository:

    @staticmethod
    async def create_api(data: Dict[str, Any]) -> Dict[str, Any]:
        query = """
        INSERT INTO apis (path, host, method)
        VALUES ($1, $2, $3)
        RETURNING id, path, host, method
        """
        async with await get_connection() as connection:
            row = await connection.fetchrow(query, data["path"], data["host"], data["method"])
            return dict(row)

    @staticmethod
    async def get_api(api_id: int) -> Optional[Dict[str, Any]]:
        query = """
        SELECT id, path, host, method
        FROM apis
        WHERE id = $1
        """
        async with await get_connection() as connection:
            row = await connection.fetchrow(query, api_id)
            return dict(row) if row else None

    @staticmethod
    async def list_apis() -> List[Dict[str, Any]]:
        query = "SELECT id, path, host, method FROM apis ORDER BY id"
        async with await get_connection() as connection:
            rows = await connection.fetch(query)
            return [dict(r) for r in rows]

    @staticmethod
    async def update_api(api_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not data:
            return None

        # Build the SET clause dynamically
        set_clauses = []
        values = []
        i = 1
        for field, val in data.items():
            set_clauses.append(f"{field} = ${i}")
            values.append(val)
            i += 1

        set_str = ", ".join(set_clauses)
        query = f"""
        UPDATE apis
        SET {set_str}
        WHERE id = ${i}
        RETURNING id, path, host, method
        """

        values.append(api_id)

        async with await get_connection() as connection:
            row = await connection.fetchrow(query, *values)
            return dict(row) if row else None

    @staticmethod
    async def delete_api(api_id: int) -> bool:
        query = "DELETE FROM apis WHERE id = $1"
        async with await get_connection() as connection:
            result = await connection.execute(query, api_id)
            # asyncpg returns something like 'DELETE <rowcount>'
            return result.startswith("DELETE") and result.split(" ")[1] == "1"

    @staticmethod
    async def list_apis_with_issues() -> List[Dict[str, Any]]:
        query = """
        SELECT a.id as api_id, a.path, a.host, a.method,
               i.id as issue_id
        FROM apis a
        LEFT JOIN api_issues_association ai ON a.id = ai.api_id
        LEFT JOIN issues i ON i.id = ai.issue_id
        ORDER BY a.id, i.id
        """
        async with await get_connection() as connection:
            rows = await connection.fetch(query)

        grouped = {}
        for row in rows:
            row_dict = dict(row)
            api_id = row_dict["api_id"]
            if api_id not in grouped:
                grouped[api_id] = {
                    "api_id": api_id,
                    "path": row_dict["path"],
                    "host": row_dict["host"],
                    "method": row_dict["method"],
                    "issues": []
                }
            if row_dict["issue_id"] is not None:
                grouped[api_id]["issues"].append({"id": row_dict["issue_id"]})

        return list(grouped.values())

from app.db.connection import get_connection

class AssociationRepository:

    @staticmethod
    async def add_association(api_id: int, issue_id: int) -> bool:
        query = """
        INSERT INTO api_issues_association (api_id, issue_id)
        VALUES ($1, $2)
        ON CONFLICT DO NOTHING
        """
        async with await get_connection() as connection:
            result = await connection.execute(query, api_id, issue_id)
            # If it inserted a row, result might be "INSERT 0 1"
            return result.startswith("INSERT") and result.split(" ")[2] == "1"

    @staticmethod
    async def remove_association(api_id: int, issue_id: int) -> bool:
        query = """
        DELETE FROM api_issues_association
        WHERE api_id = $1 AND issue_id = $2
        """
        async with await get_connection() as connection:
            result = await connection.execute(query, api_id, issue_id)
            return result.startswith("DELETE") and result.split(" ")[1] == "1"

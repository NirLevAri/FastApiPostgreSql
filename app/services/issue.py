from typing import Optional, List, Dict, Any
from app.repositories.issue import IssueRepository

class IssueService:

    @staticmethod
    async def create_issue() -> Dict[str, Any]:
        return await IssueRepository.create_issue()

    @staticmethod
    async def get_issue(issue_id: int) -> Optional[Dict[str, Any]]:
        return await IssueRepository.get_issue(issue_id)

    @staticmethod
    async def list_issues() -> List[Dict[str, Any]]:
        return await IssueRepository.list_issues()

    @staticmethod
    async def delete_issue(issue_id: int) -> bool:
        return await IssueRepository.delete_issue(issue_id)

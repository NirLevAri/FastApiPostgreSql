# app/services/association_service.py
from app.repositories.apis_issues_association import AssociationRepository

class AssociationService:

    @staticmethod
    async def add_association(api_id: int, issue_id: int) -> bool:
        return await AssociationRepository.add_association(api_id, issue_id)

    @staticmethod
    async def remove_association(api_id: int, issue_id: int) -> bool:
        return await AssociationRepository.remove_association(api_id, issue_id)

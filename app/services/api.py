from typing import Optional, List, Dict, Any
from app.repositories.api import APIRepository

class APIService:

    @staticmethod
    async def create_api(data: Dict[str, Any]) -> Dict[str, Any]:
        return await APIRepository.create_api(data)

    @staticmethod
    async def get_api(api_id: int) -> Optional[Dict[str, Any]]:
        return await APIRepository.get_api(api_id)

    @staticmethod
    async def list_apis() -> List[Dict[str, Any]]:
        return await APIRepository.list_apis()

    @staticmethod
    async def update_api(api_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        return await APIRepository.update_api(api_id, data)

    @staticmethod
    async def delete_api(api_id: int) -> bool:
        return await APIRepository.delete_api(api_id)

    @staticmethod
    async def list_apis_with_issues() -> List[Dict[str, Any]]:
        return await APIRepository.list_apis_with_issues()

from src.api.v1.inventory.domain.repositories.inventory_repository import InventoryRepository
from src.api.v1.inventory.application.delete.delete_item_dto import DeleteItemDTO

class DeleteItem:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository

    def execute(self, dto: DeleteItemDTO):
        inventory_item = self.repository.find_by_id(dto.inventory_id)
        if not inventory_item:
            raise ValueError('Item not found')
        
        self.repository.delete(inventory_item)
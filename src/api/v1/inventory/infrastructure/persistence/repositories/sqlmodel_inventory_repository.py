from src.api.v1.shared.domain.value_objects import Uuid
from typing import List, Optional
from sqlmodel import Session, select
from src.api.v1.inventory.domain.repositories.inventory_repository import (
    InventoryRepository,
)
from src.api.v1.inventory.domain.entities.inventory import Inventory
from src.api.v1.inventory.infrastructure.persistence.models.sqlmodel_inventory_model import (  # noqa: E501
    SqlModelInventoryModel,
)


class SQLModelInventoryRepository(InventoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> List[Inventory]:
        statement = select(SqlModelInventoryModel)
        items = self.session.exec(statement).all()
        return [item.to_entity() for item in items]

    def find_by_id(self, id: Uuid) -> Optional[Inventory]:
        item = self.session.get(SqlModelInventoryModel, str(id))
        return item.to_entity() if item else None

    def save(self, item: Inventory) -> bool:
        print("DEBUG - Entered save method")
        item_model = SqlModelInventoryModel.from_entity(item)
        self.session.add(item_model)
        self.session.commit()
        return True

    def update(self, item: Inventory) -> bool:
        existing_item = self.session.get(SqlModelInventoryModel, str(item.id))
        if existing_item:
            for key, value in SqlModelInventoryModel.from_entity(item).dict().items():
                setattr(existing_item, key, value)
            self.session.commit()
            return True
        return False

    def delete(self, item: Inventory) -> bool:
        existing_item = self.session.get(SqlModelInventoryModel, str(item.id))
        if existing_item:
            self.session.delete(existing_item)
            self.session.commit()
            return True
        return False

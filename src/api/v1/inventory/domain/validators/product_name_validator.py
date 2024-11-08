from src.api.v1.inventory.domain.errors.inventoryItem_error import (
    InventoryItemError,
    InventoryItemTypeError,
)


class ProductNameValidator:
    @staticmethod
    def validate(name: str) -> str:
        if not name:
            raise InventoryItemError(InventoryItemTypeError.INVALID_PRODUCT_NAME)
        return name

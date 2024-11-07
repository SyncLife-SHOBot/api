from src.api.v1.inventory.domain.errors.inventoryItem_error import InventoryItemError, InventoryItemTypeError

class AmountValidator:
    @staticmethod
    def validate(amount: int) -> int:
        if amount < 0:
            raise InventoryItemError(InventoryItemTypeError.INVALID_AMOUNT)
        return amount

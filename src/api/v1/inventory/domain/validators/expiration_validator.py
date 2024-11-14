from datetime import date
from src.api.v1.inventory.domain.errors import (
    InventoryItemError,
    InventoryItemTypeError,
)


class ExpirationDateValidator:
    @staticmethod
    def validate(expiration_date: date) -> date:
        if expiration_date < date.today():
            raise InventoryItemError(InventoryItemTypeError.EXPIRED_ITEM)
        return expiration_date

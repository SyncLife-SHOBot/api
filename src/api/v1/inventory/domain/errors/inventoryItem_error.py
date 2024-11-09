from enum import Enum
from src.api.v1.inventory.domain.errors.inventoryError import InventoryError


class InventoryItemTypeError(Enum):
    INVALID_PRODUCT_NAME = "El nombre del producto no puede estar vacio."
    INVALID_AMOUNT = "La cantidad del producto debe ser mayor a 0."
    EXPIRED_ITEM = "La fecha de expiracion del producto es invalida o ya expiro."
    ITEM_NOT_FOUND = "No se encontro el producto"


class InventoryItemError(InventoryError):
    def __init__(self, error_type: InventoryItemTypeError):
        super().__init__(error_type.value)

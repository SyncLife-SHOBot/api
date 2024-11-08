class InventoryError(Exception):
    def __init__(self, error_message: str):
        super().__init__(f"Error de Inventory: {error_message}")

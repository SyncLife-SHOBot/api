from src.api.v1.shared.domain.value_objects import Uuid


class ViewAllInventoryItemsDTO:
    def __init__(self, user_id: Uuid):
        self.user_id = user_id

from api.v1.shared.domain.errors import UuidError, UuidTypeError
import uuid


class UuidValidator:
    @staticmethod
    def validate(id: str) -> str:
        try:
            return str(uuid.UUID(id))
        except ValueError:
            raise UuidError(UuidTypeError.INVALID_UUID)

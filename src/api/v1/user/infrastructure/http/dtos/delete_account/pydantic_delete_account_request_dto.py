from pydantic import BaseModel

from src.api.v1.user.application.account_management.delete_account.delete_account_dto import (  # noqa: E501
    DeleteAccountDto,
)


class PydanticDeleteAccountRequestDto(BaseModel):
    uuid: str

    def to_application(self) -> DeleteAccountDto:
        return DeleteAccountDto(
            uuid=self.uuid,
        )

    @classmethod
    def from_application(
        cls, app_dto: DeleteAccountDto
    ) -> "PydanticDeleteAccountRequestDto":
        return cls(
            uuid=app_dto.uuid,
        )

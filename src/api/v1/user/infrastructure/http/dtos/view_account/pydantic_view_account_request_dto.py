from pydantic import BaseModel

from src.api.v1.user.application.account_management.view_account.view_account_dto import (  # noqa: E501
    ViewAccountDto,
)


class PydanticViewAccountRequestDto(BaseModel):
    uuid: str

    def to_application(self) -> ViewAccountDto:
        return ViewAccountDto(
            uuid=self.uuid,
        )

    @classmethod
    def from_application(
        cls, app_dto: ViewAccountDto
    ) -> "PydanticViewAccountRequestDto":
        return cls(
            uuid=app_dto.uuid,
        )

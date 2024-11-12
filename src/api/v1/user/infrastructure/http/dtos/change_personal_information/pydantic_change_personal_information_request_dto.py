from datetime import date
from pydantic import BaseModel, EmailStr
from src.api.v1.user.application.account_management.modify_user.change_personal_information.change_personal_information_dto import (  # noqa: E501
    ChangePersonalInformationDto,
)


class PydanticChangePersonalInformationRequestDto(BaseModel):
    uuid: str
    email: EmailStr
    first_name: str
    last_name: str
    birth_date: date
    phone: str

    def to_application(self) -> ChangePersonalInformationDto:
        return ChangePersonalInformationDto(
            uuid=self.uuid,
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            birth_date=self.birth_date,
            phone=self.phone,
        )

    @classmethod
    def from_application(
        cls, app_dto: ChangePersonalInformationDto
    ) -> "PydanticChangePersonalInformationRequestDto":
        return cls(
            uuid=app_dto.uuid,
            email=app_dto.email,
            first_name=app_dto.first_name,
            last_name=app_dto.last_name,
            birth_date=app_dto.birth_date,
            phone=app_dto.phone,
        )

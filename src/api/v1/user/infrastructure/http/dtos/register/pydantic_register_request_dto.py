from pydantic import BaseModel, EmailStr
from datetime import date
from src.api.v1.user.application.authentication.register.register_dto import RegisterDto


class PydanticRegisterRequestDto(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str
    password: str
    birth_date: date

    def to_application(self) -> RegisterDto:
        return RegisterDto(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone,
            password=self.password,
            birth_date=self.birth_date,
        )

    @classmethod
    def from_application(
        cls, register_dto: RegisterDto
    ) -> "PydanticRegisterRequestDto":
        return cls(
            email=register_dto.email,
            first_name=register_dto.first_name,
            last_name=register_dto.last_name,
            phone=register_dto.phone,
            password=register_dto.password,
            birth_date=register_dto.birth_date,
        )

from app.database.core import Base
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, ConfigDict, model_validator
from sqlalchemy import ForeignKey, text
from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN, ENUM, TEXT, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional


class Status(int, Enum):
    ACTIVE = 1
    BANNED = 2


STATUS = ENUM(Status, name="status")


class UserAccount(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    email: Mapped[Optional[str]] = mapped_column(VARCHAR(50), nullable=True, unique=True)
    status: Mapped[Status] = mapped_column(STATUS, server_default="ACTIVE", nullable=False)
    subscribed: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, server_default=text("FALSE"))
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )


class UserProfile(Base):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    bio: Mapped[str] = mapped_column(TEXT, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("NOW()")
    )

    user_account_id: Mapped[int] = mapped_column(ForeignKey(UserAccount.id, ondelete="CASCADE"))


class UserAccountBase(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)


class UserAccountCreate(UserAccountBase):
    username: str
    password: str
    email: Optional[str]


class UserAccountRead(UserAccountBase):
    id: int
    username: str
    password: str
    email: Optional[str]
    status: Status
    subscribed: bool
    created_at: datetime


class UserAccountUpdate(UserAccountBase):
    password: Optional[str] = None
    email: Optional[str] = None
    status: Optional[Status] = None
    subscribed: Optional[bool] = None

    @model_validator(mode="before")
    def check_null_fields(cls, values):
        if "password" in values and values["password"] is None:
            raise ValueError("Password cannot be explicitly set to null.")
        if "status" in values and values["status"] is None:
            raise ValueError("Status cannot be explicitly set to null.")
        if "subscribed" in values and values["subscribed"] is None:
            raise ValueError("Subscribed cannot be explicitly set to null.")
        return values

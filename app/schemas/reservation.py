from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Extra, Field, UUID4, root_validator, validator

# Представить объект datetime в виде строки с точностью до минут.
FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).isoformat(timespec='minutes')

TO_TIME = (
    datetime.now() + timedelta(hours=1)
).isoformat(timespec='minutes')


class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        extra = Extra.forbid

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования '
                'не может быть больше времени окончания'
            )
        return values


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Время начала бронирования '
                'не может быть меньше текущего времени'
            )
        return value


# Этот класс наследуем от ReservationUpdate с валидатором.
class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


# Класс ReservationDB нельзя наследовать от ReservationCreate,
# потому что будет срабатывать валидатор check_from_reserve_later_than_now
# для тех объектов бронирования, которые были созданы ранее.
class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
    user_id: Optional[UUID4]

    class Config:
        orm_mode = True

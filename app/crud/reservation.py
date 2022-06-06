from datetime import datetime
from typing import Optional

from sqlalchemy import and_, between, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation
from app.schemas.user import UserDB


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(
            self,
            *,
            from_reserve: datetime,
            to_reserve: datetime,
            meetingroom_id: int,
            reservation_id: Optional[int] = None,
            session: AsyncSession,
    ) -> list[Reservation]:
        select_stmt = select(Reservation).where(
                Reservation.meetingroom_id == meetingroom_id,
                or_(
                    between(
                        from_reserve,
                        Reservation.from_reserve,
                        Reservation.to_reserve
                    ),
                    between(
                        to_reserve,
                        Reservation.from_reserve,
                        Reservation.to_reserve
                    ),
                    and_(
                        from_reserve <= Reservation.from_reserve,
                        to_reserve >= Reservation.to_reserve
                    )
                )
        )
        # Если передан id бронирования...
        if reservation_id is not None:
            # ... то к выражению нужно добавить новое условие.
            select_stmt = select_stmt.where(
                # id искомых объектов не равны id обновляемого объекта.
                Reservation.id != reservation_id
            )
        # Выполняем запрос.
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    async def get_future_reservations_for_room(
            self,
            room_id: int,
            session: AsyncSession,
    ):
        reservations = await session.execute(
            # Получить все объекты Reservation.
            select(Reservation).where(
                # Где внешний ключ meetingroom_id
                # равен id запрашиваемой переговорки.
                Reservation.meetingroom_id == room_id,
                # А время конца бронирования больше текущего времени.
                Reservation.to_reserve > datetime.now()
            )
        )
        reservations = reservations.scalars().all()
        return reservations

    async def get_by_user(
            self, session: AsyncSession, user: UserDB
    ):
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.user_id == user.id
            )
        )
        return reservations.scalars().all()


# Создаём объекта класса CRUDReservation.
reservation_crud = CRUDReservation(Reservation)

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import get_db_session
from orders.logic import OrderLogic


def get_orders_logic(db_session: AsyncSession = Depends(get_db_session)):
    return OrderLogic(db_session=db_session)
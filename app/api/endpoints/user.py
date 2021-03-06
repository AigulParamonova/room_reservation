from fastapi import APIRouter, HTTPException

from app.core.user import auth_backend, fastapi_users

router = APIRouter()

router.include_router(
    # В роутер аутентификации
    # передается объект бекэнда аутентификации.
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(),
    prefix='/auth',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_users_router(),
    prefix='/users',
    tags=['users'],
)


# В самом конце файла допишите свой эндпоинт.
@router.delete(
    # Путь и тег ниже полностью копируют параметры эндпоинта по умолчанию.
    '/users/{id}',
    tags=['users'],
    # Параметр, который показывает, что метод устарел.
    deprecated=True
)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""
    raise HTTPException(
        # 405 ошибка - метод не разрешен.
        status_code=405,
        detail="Удаление пользователей запрещено!"
    )

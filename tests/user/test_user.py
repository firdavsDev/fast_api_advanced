import pytest  # pip install pytest-asyncio
from httpx import AsyncClient  # pip install httpx

from ecommerce.auth.jwt import create_access_token
from conf_test_db import app


@pytest.mark.asyncio
async def test_all_users():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})
        response = await ac.get("/user/list", headers={'Authorization': f'Bearer {user_access_token}'})
    assert response.status_code == 200

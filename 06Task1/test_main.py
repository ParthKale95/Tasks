import pytest
from httpx import AsyncClient
from main import app
pytestmark = pytest.mark.asyncio


@pytest.mark.asyncio
async def test_create_member():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/members",
            json={
                "name": "Test User",
                "age": 25,
                "membership_type": "Gold",
                "phone": "1234567890"
            }
        )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test User"
    assert data["age"] == 25
    assert "id" in data


@pytest.mark.asyncio
async def test_get_members():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/members")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

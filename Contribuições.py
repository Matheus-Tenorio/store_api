import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products", json={"name": "Product 1", "price": 6000})
    assert response.status_code == 201
    assert response.json() == {"name": "Product 1", "price": 6000, "id": 1}

@pytest.mark.asyncio
async def test_patch_product_not_found():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.patch("/products/999", json={"price": 7000})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}

@pytest.mark.asyncio
async def test_filter_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products", params={"min_price": 5000, "max_price": 8000})
    assert response.status_code == 200
    assert all(5000 <= product["price"] <= 8000 for product in response.json())

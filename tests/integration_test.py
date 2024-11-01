import pytest
from httpx import AsyncClient
import os
import sys
sys.path.append(os.getcwd())
from bookstore.main import app  # Import your FastAPI instance
import allure
from logger import log_info


@allure.title("User Signup")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for user signup functionality.")
@pytest.mark.asyncio
async def test_signup() -> None:
    async with AsyncClient(app=app, base_url="http://") as client :
        response = await client.post("/signup", json={
            "email": "testuser@example.com",
            "password": "securepassword"
        })
        assert response.status_code == 200
        assert response.json() == {"message": "User created successfully"}
        log_info(f"Server response : {response.text}")

@allure.title("User Login")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for user login functionality.")
@pytest.mark.asyncio
async def test_login()  -> str:
    async with AsyncClient(app=app, base_url="http://") as client:
        response = await client.post("/login", json={
            "email": "testuser@example.com",
            "password": "securepassword"
        })
        assert response.status_code == 200
        assert "access_token" in response.json()
        log_info("User logged in with email: testuser@example.com")
        return response.json()["access_token"]

@allure.title("Create Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test case for creating a new book.")
@pytest.mark.asyncio
async def test_create_book()  -> str:
    access_token = await test_login()  # Use login to get a token
    async with AsyncClient(app=app, base_url="http://") as client:
        response  = await client.post("/books/", json={
            "name": "Sample Book",
            "author": "Author Name",
            "published_year": 2023,
            "book_summary": "This is a test book."
        }, headers={"Authorization": f"Bearer {access_token}"})
        assert response.status_code == 200
        assert response.json()["name"] == "Sample Book"
        log_info(f"Server response : {response.text}")

        log_info(f"Book created with name: {response.json()['name']}")
        return access_token,response.json()["id"] 

@allure.title("Update Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test case for updating a book's details.")
@pytest.mark.asyncio
async def test_update_book()  -> None :
    access_token , book_id = await test_create_book()
    async with AsyncClient(app=app, base_url="http://") as client:
        response = await client.put(f"/books/{book_id}", json={
            "name": "Updated Book Name",
            "author": "Updated Author"
        }, headers={"Authorization": f"Bearer {access_token}"})
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Book Name"
        log_info(f"Server response : {response.text}")
        log_info(f"Book updated with ID: {book_id}")

@allure.title("Get Book by ID")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for retrieving a book by its ID.")
@pytest.mark.asyncio
async def test_get_book_by_id() -> None :
    access_token , book_id = await test_create_book()
    async with AsyncClient(app=app, base_url="http://") as client:
        response = await client.get(f"/books/{book_id}", headers={"Authorization": f"Bearer {access_token}"})
        assert response.status_code == 200
        assert response.json()["id"] == book_id
        log_info(f"Server response : {response.text}")
        log_info(f"Retrieved book with ID: {book_id}")

@allure.title("Get All Books")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for retrieving all books.")
@pytest.mark.asyncio
async def test_get_all_books() -> None :
    access_token = await test_login()
    async with AsyncClient(app=app, base_url="http://") as client:
        response = await client.get("/books/", headers={"Authorization": f"Bearer {access_token}"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        log_info(f"Server response : {response.text}")
        log_info("Retrieved all books.")

@allure.title("Delete Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test case for deleting a book.")
@pytest.mark.asyncio
async def test_delete_book() -> None :
    access_token , book_id = await test_create_book()
    async with AsyncClient(app=app, base_url="http://") as client:
        response = await client.delete(f"/books/{book_id}", headers={"Authorization": f"Bearer {access_token}"})
        assert response.status_code == 200
        assert response.json() == {"message": "Book deleted successfully"}
        log_info(f"Server response : {response.text}")
        log_info(f"Deleted book with ID: {book_id}")

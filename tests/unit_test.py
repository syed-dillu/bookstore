import pytest
import os
import sys
import time
from datetime import timedelta
from fastapi.testclient import TestClient
from unittest.mock import MagicMock
sys.path.append(os.getcwd())
from bookstore.main import app, pwd_context, create_access_token
from bookstore.database import UserCredentials
import allure
from logger import log_info
from jwt import ExpiredSignatureError
from bookstore.constants import ALGORITHM, SECRET_KEY
import jwt

client = TestClient(app)

@allure.title("User Signup - Successful Creation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for successfully creating a new user during signup.")
@pytest.mark.asyncio
async def test_create_user_signup() -> None:
    response = client.post("/signup", json={"email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}
    log_info(f"Server response : {response.text}")
    log_info(f"User created with email: test@example.com")



@allure.title("User Signup - Email Already Exists")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for attempting to create a user with an existing email.")
@pytest.mark.asyncio
async def test_create_user_signup_email_exists() -> None:
    response = client.post("/signup", json={"email": "test@example.com", "password": "testpass"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}
    log_info(f"Server response : {response.text}")
    log_info("Attempted signup with existing email: test@example.com")



@allure.title("User Login - Get Access Token")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for logging in a user to obtain an access token.")
@pytest.mark.asyncio
async def test_login_for_access_token() -> None:
    client.post("/signup", json={"email": "loginuser@example.com", "password": "loginpass"})
    
    mock_db_session = MagicMock()
    hashed_password = pwd_context.hash("loginpass")
    mock_user = UserCredentials(email="loginuser@example.com", password=hashed_password)
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = mock_user

    response = client.post("/login", json={"email": "loginuser@example.com", "password": "loginpass"})
    assert response.status_code == 200, response.text
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
    log_info(f"Access token obtained for user: loginuser@example.com")



@allure.title("User Login - Invalid Password")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test case for logging in a user with an incorrect password.")
@pytest.mark.asyncio
async def test_login_for_access_token_invalid_password() -> None:
    client.post("/signup", json={"email": "loginuser@example.com", "password": "loginpass"})
    
    mock_db_session = MagicMock()
    hashed_password = pwd_context.hash("loginpass")
    mock_user = UserCredentials(email="loginuser@example.com", password=hashed_password)
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = mock_user

    response = client.post("/login", json={"email": "loginuser@example.com", "password": "wrongpass"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Incorrect email or password"}
    log_info(f"Server response : {response.text}")
    log_info("Attempted login with invalid password for user: loginuser@example.com")



@allure.title("Access Token Expiration Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test case for ensuring the access token expires after a specified time.")
@pytest.mark.asyncio
async def test_access_token_expiration() -> None:
    expires_delta = timedelta(seconds=1)
    data = {"sub": "testuser@example.com"}
    token = create_access_token(data, expires_delta)

    time.sleep(2)

    with pytest.raises(ExpiredSignatureError):
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    log_info("Access token expired correctly after the specified time.")




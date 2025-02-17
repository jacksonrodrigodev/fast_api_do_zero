from http import HTTPStatus


def test_read_root_deve_retornar_ok_hello_world(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "test_user",
            "email": "user@example.com",
            "password": "password",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "test_user",
        "email": "user@example.com",
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "test_user",
                "email": "user@example.com",
            }
        ]
    }


def test_read_user_id(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "test_user",
        "email": "user@example.com",
    }


def test_read_user_id_not_found(client):
    response = client.get("/users/2")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "new_password",
            "username": "test_user_2",
            "email": "test2@test2.com",
            "id": 1,
        },
    )

    assert response.json() == {
        "username": "test_user_2",
        "email": "test2@test2.com",
        "id": 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        "/users/2",
        json={
            "password": "new_password",
            "username": "test_user_2",
            "email": "test2@test2.com",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.json() == {"message": "User deleted"}
    assert response.status_code == HTTPStatus.OK
    response = client.get("/users/")
    assert response.json() == {"users": []}


def test_delete_user_not_found(client):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}

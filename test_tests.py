import pytest
from flask import url_for
from app import app
from gotrue.errors import AuthApiError

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Verifica la página de inicio (index)"""
    rv = client.get("/")
    assert rv.status_code == 200


def test_login(client):
    """Verifica el inicio de sesión"""
    rv = client.post(
        "/login",
        data=dict(email="test@example.com", password="password"),
        follow_redirects=True,
    )
    assert rv.status_code == 200


def test_register(client):
    """Verifica el registro de usuario"""
    try:
        rv = client.post('/register', data=dict(
            email='test@example.com',  # Utiliza un correo electrónico existente
            password='password'
        ), follow_redirects=True)
        assert rv.status_code == 200
    except AuthApiError:
        pass  # Capturamos la excepción si el usuario ya está registrado


def test_logout(client):
    """Verifica el cierre de sesión"""
    client.post("/login", data=dict(email="test@example.com", password="password"))
    rv = client.get("/logout", follow_redirects=True)
    assert rv.status_code == 200


def test_upload_experience(client):
    """Verifica la subida de experiencias"""
    client.post("/login", data=dict(email="test@example.com", password="password"))
    data = {
        "experience_name": "Test Experience",
        "gltf_file": (open("static/models/1/1.gltf", "rb"), "1.gltf"),
    }
    rv = client.post(
        "/upload_experience",
        data=data,
        content_type="multipart/form-data",
        follow_redirects=True,
    )
    assert rv.status_code == 200


def test_experiencias(client):
    """Verifica la lista de experiencias"""
    client.post("/login", data=dict(email="test@example.com", password="password"))
    rv = client.get("/experiencias")
    assert rv.status_code == 200
    assert b"Test Experience" in rv.data


def test_encuesta(client):
    """Verifica la encuesta de satisfacción"""
    client.post("/login", data=dict(email="test@example.com", password="password"))
    data = {"puntuacion": "5", "comentarios": "Excelente servicio"}
    rv = client.post("/encuesta", data=data, follow_redirects=True)
    assert rv.status_code == 201
    assert b"Survey submitted successfully!" in rv.data


if __name__ == "__main__":
    pytest.main()

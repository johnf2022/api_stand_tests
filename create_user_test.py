import data
import sender_stand_request


# Función auxiliar para modificar el nombre en el cuerpo del request
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Función helper para verificar respuesta positiva
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprobar el código de estado HTTP 201
    assert user_response.status_code == 201
    # Comprobar que el token de la respuesta no esté vacío
    assert user_response.json()["authToken"] != ""


# Prueba 2: Creación de usuario con 15 caracteres en firstName
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

from rest_framework.views import exception_handler

def core_exception_handler(exc, context):
    # Llama al exception handler por defecto de DRF primero,
    # para obtener la respuesta estandar.
    response = exception_handler(exc, context)

    # Ahora añade la información extra a la respuesta.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

def hello_world(request):
    request_args = request.args
    request_body = request.get_json(silent=True)
    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
        name = f'{name} {lastname}'
    else:
        name = 'World'
    dni = request_body['dni']
    return f'Hello {name}, with dni: {dni}!'
def file_handler(file):
    with open('restaurant/static/upload/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

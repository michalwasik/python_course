def describe_data(request):
    dict_data = request.json()
    print(*dict_data.items(), sep='\n')

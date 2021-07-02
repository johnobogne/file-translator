def client_keys(request) :
    if request == 'client_id' :
        return 'PLACE YOUR CLIENT_ID HERE'
    elif request == 'client_secret' :
        return 'PLACE YOUR CLIENT SECRET HERE'
    else :
        return None

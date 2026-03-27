# API REPONSE PATTERNS

def error_response(err, status_code:int=400):
    return {
        "success": False,
        "error": err.__repr__(),
        "status_code":status_code
    }

def success_reponse(data, status_code:int=200):
    return {
        "success":True,
        "data": data,
        "status_code":status_code
    }

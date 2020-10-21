from flask import redirect

def pingRedirect():
    return redirect('/ping')
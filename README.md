# URL-shortner
A python-Django web-app to shorten any long url

This is a webapp written in `python` using `Django` Framework.
This is hosted on heroku and can be visited at http://short-ner.herokuapp.com/

Features:

 1. It willcreate a random short text and bind it with your long URL
 2. If supplied, it will bind the long URL with custom text
 3. It checks all the previous records before binding so that:
    - it can reuse previously created short URLS
    - it should bind two long URL to same shoert custom text

Frontend is created using `HTML` and `CSS`.
Backend created using `Django 3.0`.

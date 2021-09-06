# !/usr/bin/env python 3
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTF_COORIE"))
name = cookie.get("name")
if name is None:
    print("Set-cookies: name=value")
    print("Content-type: text/html\n")
    print("Cookies!!!\n")
else:
    print("Content-type: text/html\n")
    print("Cookies:")
    print(name.value)
import urllib.request
r = urllib.request.urlopen('https://paypal.com/')
print(r.read())

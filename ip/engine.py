import requests

def ip():
    ip = input("Enter IP")
    print("Searching for IP...")
    ip_api = ("http://ip-api.com/json/"+ip)
    data = request.get(ip_api)
    ip_data = data.json()
    try:
        data = {"country": ip_data["country"], "isp": ip_data["isp"]}
    except KeyError:
         data = {"country": None, "isp": None}
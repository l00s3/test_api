from ip.engine import  ip_function as get_ip

def ask(query):
    if query == 1:
        return get_ip()
    else:
        return print(None)
    return None

query = int(input("What can I do for you? "))
ask(query)
import sys
from urllib import request

option = sys.argv[1]

if not option == "list":
    argument = sys.argv[2]

else:
    argument = None

if option == "upload":
    load = open(argument, "rb")
    load_read = load.read()

    print("Reading file.")

    req = request.Request(f"http://storagerequests.herokuapp.com/{input('Filename: ')}", data=load_read)

    print("POST Request is formed.")
    response = request.urlopen(req)

    print("Process completed. Response received from the server.")

    response_read = response.read()
    print(response_read.decode("utf-8"))

elif option == "download":
    save_path = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/filereturn/{argument}")
    read_response = response.read()
    save = open(save_path, "wb")
    save.write(read_response)
    save.close()
    print("File Successfully downloaded")


elif option == "search":
    password = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/search/{password}/{argument}")
    read_response = response.read()
    print(read_response.decode("utf-8"))

elif option == "list":
    password = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/list")
    read_response = response.read()
    print(read_response.decode("utf-8"))

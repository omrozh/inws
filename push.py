import sys
from urllib import request

option = sys.argv[1]

if not option == "list":
    argument = sys.argv[2]

else:
    argument = None

if option == "upload":
    password = sys.argv[5]
    username = sys.argv[4]

    load = open(argument, "rb")
    load_read = load.read()

    print("Reading file.")

    req = request.Request(f"http://storagerequests.herokuapp.com/"
                          f"{input('Filename: ')}/{password}/{username}", data=load_read)

    print("POST Request is formed.")
    response = request.urlopen(req)

    print("Process completed. Response received from the server.")

    response_read = response.read()
    print(response_read.decode("utf-8"))

elif option == "download":
    save_path = sys.argv[3]
    password = sys.argv[5]
    username = sys.argv[4]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/filereturn/{argument}/{password}/{username}")
    read_response = response.read()

    save = open(save_path, "wb")
    save.write(read_response)
    save.close()
    print("File Successfully downloaded")


elif option == "search":
    password = sys.argv[4]
    username = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/search/{argument}/{password}/{username}")
    read_response = response.read()
    print(read_response.decode("utf-8"))

elif option == "list":
    password = sys.argv[3]
    username = sys.argv[2]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/list/{password}/{username}")
    read_response = response.read()
    print(read_response.decode("utf-8"))

elif option == "delete":
    password = sys.argv[4]
    username = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/delete/{argument}/{password}/{username}")
    read_response = response.read()
    print(read_response.decode("utf-8"))

elif option == "createAccount":
    username = argument
    password = sys.argv[3]

    print(request.urlopen(f"http://storagerequests.herokuapp.com/create/account/{password}/{username}").read())

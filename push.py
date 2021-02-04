import sys
from urllib import request

option = sys.argv[1]
argument = sys.argv[2]

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
    response = request.urlopen(f"http://storagerequests.herokuapp.com/search?query={argument}")
    read_response = response.read()
    print(read_response)

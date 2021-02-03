import sys
from urllib import request

option = sys.argv[1]
argument = sys.argv[2]

if option == "upload":
    load = open(argument, "rb")
    load_read = load.read()

    req = request.Request(f"http://storagerequests.herokuapp.com/{input('Filename: ')}", data=load_read)
    response = request.urlopen(req)

    response_read = response.read()
    print(response_read.decode("utf-8"))

elif option == "download":
    save_path = sys.argv[3]
    response = request.urlopen(f"http://storagerequests.herokuapp.com/filereturn/{argument}")
    save = open(save_path, "wb")
    save.write(response.read())
    save.close()
    print("File Successfully downloaded")

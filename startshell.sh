password=""
username=""

instore(){
    if [ "$1" = "download" ]
        then echo "Download"
        python3 instore download $2 $3 $username $password
    fi
    if [ "$1" = "upload" ]
        then echo "Upload"
        python3 instore upload $2 $username $password
    fi
    if [ "$1" = "list" ]
        then clear
        python3 instore list $username $password
    fi
    if [ "$1" = "search" ]
        then clear
        python3 instore search $2 $username $password
    fi
    if [ "$1" = "delete" ]
        then clear
        python3 instore delete $2 $username $password
    fi
    if [ "$1" = "createAccount" ]
        then clear
        python3 instore createAccount $2 $3
    fi
    if [ "$1" = "createAccount" ]
        then clear
        instore login $2 $3
    fi
    if [ "$1" = "login" ]
        then clear

        password=$3
        username=$2

        echo "Logged in as $username"
    fi
    if [ "$1" = "addOwner" ]
        then clear
        python3 instore addOwner $2 $3 $username $password
        echo "Adding new owner"
    fi
}

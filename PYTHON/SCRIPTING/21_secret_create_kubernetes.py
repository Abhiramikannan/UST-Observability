#Create Python Script to create a Kubernetes secret inside Rancher using the Rancher API.

import argparse #Read command-line arguments
import requests
import sys#Exit program on errors


def parse_key_values(pairs): #Parsing key=value inputs(see the input command there pair we are passing)
#y key value inputs? You pass secrets like this:
    #--key username=admin --key password=secret
#kubernetes excepts like this
    # {
    #   "username": "admin",
    #   "password": "secret"
    # }
#How this works?

    data = {}#Creates an empty dictionary.
    for item in pairs:#Loops over all --key arguments.
        if "=" not in item:
            raise SystemExit(f"Invalid key format: {item}")
        k, v = item.split("=", 1)#Ensures the format is key=value.
        data[k] = v#Splits and stores in a dictionary.
    return data


def main():#command line arguments
    parser = argparse.ArgumentParser(#argparse.ArgumentParser() → creates a tool that reads command-line inputs for your script.
        description="Create Kubernetes Secret via Kubernetes API (kubectl proxy)"#description → just a message that shows if you run --help.
    )#python create_secret.py --help


    parser.add_argument("--api-url", required=True, help="Kubernetes API URL (via kubectl proxy)")#--api-url → the input name you type in the command line,required=True → you must provide it, otherwise the program stops,help → text shown if you use --help,URL of Kubernetes API,eg:http://localhost:8001
    parser.add_argument("--namespace", required=True, help="Kubernetes namespace")#Namespace where the secret will be created
    parser.add_argument("--name", required=True, help="Secret name")#Name of the secret
    parser.add_argument("--key", action="append", required=True, help="key=value")#--key → this is for each key/value pair of the secret.,action="append" → allows multiple --key arguments, and collects all of them into a list,required=True → you must give at least one --key..eg:--key username=admin --key password=secret,   args.key        # ["username=admin", "password=secret"]
#inside python it will look like: args.key == ["username=admin", "password=secret"]

    args = parser.parse_args() #this line actually reads what you typed on the command line,After this line runs, Python stores all your inputs in the args object:

    secret_data = parse_key_values(args.key)#Convert key=value pairs into a dictionary(Go to above function)
#These are required Kubernetes fields.
    secret_payload = { #This is a dictionary in Python, which will become JSON when sent to Kubernetes.
        "apiVersion": "v1",
        "kind": "Secret",
        "metadata": {
            "name": args.name,
            "namespace": args.namespace,
        },
        "type": "Opaque",
        "stringData": secret_data,
    }

    url = f"{args.api_url}/api/v1/namespaces/{args.namespace}/secrets" #he endpoint in Kubernetes API to create a secret
# eg: args.api_url = "http://localhost:8001"
# args.namespace = "default"
# url = "http://localhost:8001/api/v1/namespaces/default/secrets"


    headers = {
        "Content-Type": "application/json", #Tells Kubernetes we are sending JSON data.
    }

    resp = requests.post(url, json=secret_payload, headers=headers) #converts the Python dictionary into JSON automatically

    if resp.status_code >= 300:
        print(f"ERROR {resp.status_code}: {resp.text}")
        sys.exit(1)#stops the program because something went wrong

    print(f"Secret '{args.name}' created successfully in namespace '{args.namespace}'")


if __name__ == "__main__":
    main()


#input: --key username=admin --key password=secret

# python create_secret.py \
#   --api-url http://localhost:8001 \
#   --namespace default \
#   --name my-secret \
#   --key username=admin \
#   --key password=secret



# aim:
# “Create a secret called my-secret in default namespace
# and store username=admin and password=secret inside it.”

# steps:(without kubernetes and python)
# So the logic is just receive the inputs from the user(i.e, secretname,namespace,key-value pairs(secretname and password)),
# Then convert the secret to json/dictionary....Then prepare a req(telling kubernetes what i want to create, 
# Then sent the req using kubernetes API, If result is success-> done, Fail-> shows error..


#how the program works logic without python still:
        #  # python3 secret.py \
        #   --api-url http://localhost:8001 \
        #   --namespace default \
        #   --name my-secret \
        #   --key username=admin \
        #   --key password=secret
#we passes the command along with url,namesspace,and keys..
#  so program seperates names from values and group all key together, 
# program prepares a msg.. create a secret "secret-name" in namespace "default" with this data and 
# sents the msg to that url


#programmic logic

#action="append" → collects all --key arguments into a list
#def parse_key_values(pairs):

# input: pairs = ["username=admin", "password=secret"]
# data = {} #empty dictionary
# Loop over each pairs

#     1. First iteration:
            # item = "username=admin"
            # Check if = is in the string → yes ✅
            # Split by =:
            # k, v = item.split("=", 1) #So 1 means split only once at the first =.
            # # k = "username", v = "admin"
            # add to dictionary
            # data["username"] = "admin"
            # this will be data: {"username": "admin"}




# #while running in kubernetes

# sudo apt update
# sudo apt install python3-pip
# pip3 --version
# pip3 install requests --user  #install requests using pip

# #run the program
# python3 secret.py \
#           --api-url http://localhost:8001 \
#           --namespace default \
#           --name my-secret \
#           --key username=admin \
#           --key password=secret


# #start the kubeproxy
# kubectl proxy

# #take a new terminal and run your program -> success

# #to test the api which is reachable:
# curl http://localhost:8001/api/v1/namespaces/default



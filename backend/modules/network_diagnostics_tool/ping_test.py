import os
def ping_options(user_response):
    match user_response:
        case "1":
            print("Running Ping Test...")
            os.system("ping -c 4 google.com")
        case "2":
            print("Running Traceroute...")
            os.system("traceroute google.com")
        


if __name__ == "__main__":
    ping_options()
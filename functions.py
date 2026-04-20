# Basic Functions

def formatting_dictionary_to_list(servers):
    server_list = []
    for server in servers.values():
        server_list.append(server)
    return(server_list)



def summary_of_servers(servers):
    for server in servers:
        print(server.get("hostname"), server.get("region"), server.get("datacenter"), server.get("status"), sep = "---------")
        


def region_filter(servers):
    user_input_region = input("Enter a region to get info (eu-central, eu-west, us-east, or ap-southeast): ")
    for server in servers:
        if user_input_region == server.get("region"):
            print(server.get("hostname"), server.get("status"), sep = "---------")



def down_services(servers):
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        services = server.get("services")
        for i, j in services.items():
            service_name = i
            service_status = j.get("status")
            if not (server_status == "online" and service_status == "online"):
                print(server_name, server_status, service_name, service_status, sep = "---------")

            

        

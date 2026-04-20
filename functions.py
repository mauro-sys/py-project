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



def status_problems(servers):
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        services = server.get("services")
        for i, j in services.items():
            service_name = i
            service_status = j.get("status")
            if not (server_status == "online" and service_status == "online"):
                print(server_name, server_status, service_name, service_status, sep = "---------")

            

def resourse_problems(servers):
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        server_cpu = server.get("cpu_usage_percent")
        server_ram = server.get("ram_usage_percent")
        server_storage = server.get("disk_usage_percent")
        uptime = server.get("uptime_hours")
        support = server.get("on_call_team")
        if server_cpu > 85 or server_ram > 85 or server_storage > 90:
            print(server_name, server_status, "CPU",  server_cpu, "RAM",server_ram, "Storage", server_storage, "Uptime", uptime, "Please contact team", support, sep = " : ")
            
            

def tag_filter(servers):
    tag_search = input("What tag do you want to search: ")
    server_name = server.get("hostname")
    server_status = server.get("status")
    for server in servers:
        for tag in server.values():
            if tag_search == tag:
                print(server_name, server_status)
                 
            

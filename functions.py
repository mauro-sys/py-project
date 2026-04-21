import time


# Basic Functions

def formatting_dictionary_to_list(servers):
    server_list = []
    for server in servers.values():
        server_list.append(server)
    return(server_list)


def server_summary(servers):
    print(f'''
             server name  :  server region  :  server datacenter  :  status''')
    for server in servers:
        server_name = server.get("hostname")
        server_region = server.get("region")
        server_datacenter = server.get("datacenter")
        server_status = server.get("status")
        print(f'''---------------------------------------------------------------------------
             {server_name}  :  {server_region}  :  {server_datacenter}  :  {server_status}
            ''')
        time.sleep(0.5)


def region_filter(servers):
    user_input_region = input("Enter a region to get info (eu-central, eu-west, us-east, or ap-southeast): ")

    print(f'''
             server name  :  status''')
    for server in servers:
        server_name = server.get("hostname")
        server_region = server.get("region")
        server_status = server.get("status")
        if user_input_region == server_region:
            print(f'''------------------------------------------------------
             {server_name}  :  {server_status}''')


def team_alert():
    try:
        ask = input("\nDo you want to alert the respective support team? Y or N: ").lower()
        if ask == "y":
            # fucion alert to support team
            print("\nRespective support team has been alerted about the problems and will get back to you.\n")
        elif ask == "n":
            print("\nNo alert was sent.\n")
        else:
            print("\nWrong Input! Try again.")
            team_alert()
    except KeyboardInterrupt:
        print("Can't interrupt this part!")
        team_alert()


def status_problems(servers):
    print(f'''
             server name  :  server status  :  service name  :  service status''')
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        services = server.get("services")
        for i, j in services.items():
            service_name = i
            service_status = j.get("status")
            if not (server_status == "online" and service_status == "online"):
                print(f'''-------------------------------------------------------------------------------
                {server_name}  :  {server_status}  :  {service_name}  :  {service_status}''')
    team_alert()


def resourse_problems(servers):
    print(f'''
             server name  :  status  :  CPU  :  RAM  :  Storage  :  Uptime (H)  :  Support Team''')
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        server_cpu = server.get("cpu_usage_percent")
        server_ram = server.get("ram_usage_percent")
        server_storage = server.get("disk_usage_percent")
        uptime = server.get("uptime_hours")
        support = server.get("on_call_team")
        if server_cpu > 85 or server_ram > 85 or server_storage > 90:
                    print(f'''------------------------------------------------------------------------------------------------------
             {server_name}  :  {server_status}  :  {server_cpu}  :  {server_ram}  :  {server_storage}  :  {uptime}  :  {support}''')
    team_alert()
            

def tag_filter(servers):
    tag_search = input("What tag do you want to search: ").lower()
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        for tag in server.get("tags"):
            if tag_search == tag:
                print(server_name, server_status, sep=" : ")
                
                    
def restart(servers):
    for server in servers:
        server_name = server.get("hostname")
        server_status = server.get("status")
        services = server.get("services")
        if server.get("status") != "online":
            print(server_name, server_status, "Physical Server Problem. Can only be fixed manually.", sep="----")
            team_alert()
        else:
            for i, j in services.items():
                service_name = i
                service_status = j.get("status")
                depends = j.get("depends_on")
                auto_restart = j.get("auto_restart")
                max_attempts = j.get("max_restart_attempts")
                restart_attempts = j.get("restart_attempts")
                if server_status == "online" and service_status != "online":
                    if depends == "" and auto_restart == True and max_attempts > restart_attempts:
                        print(server_name, server_status, service_name, service_status, "Starting Service. Please wait...", sep="----")
                        # fuction to start service
                    else:
                        auto_restart == True
                        max_attempts = 5
                        restart_attempts = 0
                        print(server_name, server_status, service_name, service_status, "Fixing Dependencies and Starting Service. Please wait", sep="----")
                        # fuction to start service
                            
                            

                    


from functions import formatting_dictionary_to_list, summary_of_servers, region_filter, down_services


infrastructure = {
    "srv-eu-01": {
        "hostname": "nova-frankfurt-01",
        "region": "eu-central",
        "datacenter": "Frankfurt",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 340,
        "cpu_usage_percent": 92,
        "ram_usage_percent": 87,
        "disk_usage_percent": 45,
        "tags": ["production", "web", "high-traffic"],
        "on_call_team": "team-alpha",
        "services": {
            "nginx": {
                "status": "down",
                "port": 80,
                "auto_restart": True,
                "restart_attempts": 3,
                "max_restart_attempts": 3,
                "depends_on": [],
                "last_error": "worker process exited unexpectedly"
            },
            "app_server": {
                "status": "down",
                "port": 3000,
                "auto_restart": True,
                "restart_attempts": 1,
                "max_restart_attempts": 5,
                "depends_on": ["nginx"],
                "last_error": "cannot bind to port 3000"
            },
            "postgres": {
                "status": "online",
                "port": 5432,
                "auto_restart": False,
                "restart_attempts": 0,
                "max_restart_attempts": 3,
                "depends_on": [],
                "last_error": None
            }
        }
    },
    "srv-eu-02": {
        "hostname": "nova-frankfurt-02",
        "region": "eu-central",
        "datacenter": "Frankfurt",
        "status": "down",
        "os": "Ubuntu 20.04",
        "uptime_hours": 0,
        "cpu_usage_percent": 0,
        "ram_usage_percent": 0,
        "disk_usage_percent": 78,
        "tags": ["production", "database"],
        "on_call_team": "team-alpha",
        "services": {
            "mysql": {
                "status": "down",
                "port": 3306,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": "host unreachable"
            },
            "redis": {
                "status": "down",
                "port": 6379,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": "host unreachable"
            }
        }
    },
    "srv-eu-03": {
        "hostname": "nova-amsterdam-01",
        "region": "eu-west",
        "datacenter": "Amsterdam",
        "status": "degraded",
        "os": "Ubuntu 22.04",
        "uptime_hours": 12,
        "cpu_usage_percent": 55,
        "ram_usage_percent": 91,
        "disk_usage_percent": 97,
        "tags": ["staging", "storage"],
        "on_call_team": "team-beta",
        "services": {
            "minio": {
                "status": "down",
                "port": 9000,
                "auto_restart": True,
                "restart_attempts": 2,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": "no space left on device"
            },
            "prometheus": {
                "status": "online",
                "port": 9090,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": None
            }
        }
    },
    "srv-us-01": {
        "hostname": "nova-virginia-01",
        "region": "us-east",
        "datacenter": "Virginia",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 720,
        "cpu_usage_percent": 20,
        "ram_usage_percent": 40,
        "disk_usage_percent": 55,
        "tags": ["production", "api"],
        "on_call_team": "team-gamma",
        "services": {
            "api_gateway": {
                "status": "online",
                "port": 8080,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": None
            },
            "celery_worker": {
                "status": "down",
                "port": None,
                "auto_restart": True,
                "restart_attempts": 4,
                "max_restart_attempts": 5,
                "depends_on": ["redis"],
                "last_error": "connection to redis refused"
            },
            "redis": {
                "status": "down",
                "port": 6379,
                "auto_restart": False,
                "restart_attempts": 0,
                "max_restart_attempts": 3,
                "depends_on": [],
                "last_error": "OOM: out of memory"
            }
        }
    },
    "srv-us-02": {
        "hostname": "nova-virginia-02",
        "region": "us-east",
        "datacenter": "Virginia",
        "status": "online",
        "os": "Ubuntu 20.04",
        "uptime_hours": 5,
        "cpu_usage_percent": 78,
        "ram_usage_percent": 82,
        "disk_usage_percent": 60,
        "tags": ["production", "web", "high-traffic"],
        "on_call_team": "team-gamma",
        "services": {
            "nginx": {
                "status": "online",
                "port": 80,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": None
            },
            "docker_daemon": {
                "status": "down",
                "port": None,
                "auto_restart": False,
                "restart_attempts": 0,
                "max_restart_attempts": 0,
                "depends_on": [],
                "last_error": "failed to start containerd"
            }
        }
    },
    "srv-ap-01": {
        "hostname": "nova-singapore-01",
        "region": "ap-southeast",
        "datacenter": "Singapore",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 200,
        "cpu_usage_percent": 35,
        "ram_usage_percent": 50,
        "disk_usage_percent": 70,
        "tags": ["production", "cdn"],
        "on_call_team": "team-delta",
        "services": {
            "varnish": {
                "status": "down",
                "port": 6081,
                "auto_restart": True,
                "restart_attempts": 2,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": "VCL compilation error"
            },
            "haproxy": {
                "status": "online",
                "port": 443,
                "auto_restart": True,
                "restart_attempts": 0,
                "max_restart_attempts": 5,
                "depends_on": [],
                "last_error": None
            }
        }
    }
}



# --------------------------   STEP 1: FORMATTING   -----------------------

# formatted_server_list = formatting_dictionary_to_list(infrastructure)

# RESULT of above function  for reference

formatted_server_list = [
    {
        "hostname": "nova-frankfurt-01",
        "region": "eu-central",
        "datacenter": "Frankfurt",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 340,
        "cpu_usage_percent": 92,
        "ram_usage_percent": 87,
        "disk_usage_percent": 45,
        "tags": ["production", "web", "high-traffic"],
        "on_call_team": "team-alpha",
        "services": {
            "nginx": {"status": "down", "port": 80, "auto_restart": True, "restart_attempts": 3, "max_restart_attempts": 3, "depends_on": [], "last_error": "worker process exited unexpectedly"},
            "app_server": {"status": "down", "port": 3000, "auto_restart": True, "restart_attempts": 1, "max_restart_attempts": 5, "depends_on": ["nginx"], "last_error": "cannot bind to port 3000"},
            "postgres": {"status": "online", "port": 5432, "auto_restart": False, "restart_attempts": 0, "max_restart_attempts": 3, "depends_on": [], "last_error": None}
        }
    },
    {
        "hostname": "nova-frankfurt-02",
        "region": "eu-central",
        "datacenter": "Frankfurt",
        "status": "down",
        "os": "Ubuntu 20.04",
        "uptime_hours": 0,
        "cpu_usage_percent": 0,
        "ram_usage_percent": 0,
        "disk_usage_percent": 78,
        "tags": ["production", "database"],
        "on_call_team": "team-alpha",
        "services": {
            "mysql": {"status": "down", "port": 3306, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": "host unreachable"},
            "redis": {"status": "down", "port": 6379, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": "host unreachable"}
        }
    },
    {
        "hostname": "nova-amsterdam-01",
        "region": "eu-west",
        "datacenter": "Amsterdam",
        "status": "degraded",
        "os": "Ubuntu 22.04",
        "uptime_hours": 12,
        "cpu_usage_percent": 55,
        "ram_usage_percent": 91,
        "disk_usage_percent": 97,
        "tags": ["staging", "storage"],
        "on_call_team": "team-beta",
        "services": {
            "minio": {"status": "down", "port": 9000, "auto_restart": True, "restart_attempts": 2, "max_restart_attempts": 5, "depends_on": [], "last_error": "no space left on device"},
            "prometheus": {"status": "online", "port": 9090, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": None}
        }
    },
    {
        "hostname": "nova-virginia-01",
        "region": "us-east",
        "datacenter": "Virginia",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 720,
        "cpu_usage_percent": 20,
        "ram_usage_percent": 40,
        "disk_usage_percent": 55,
        "tags": ["production", "api"],
        "on_call_team": "team-gamma",
        "services": {
            "api_gateway": {"status": "online", "port": 8080, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": None},
            "celery_worker": {"status": "down", "port": None, "auto_restart": True, "restart_attempts": 4, "max_restart_attempts": 5, "depends_on": ["redis"], "last_error": "connection to redis refused"},
            "redis": {"status": "down", "port": 6379, "auto_restart": False, "restart_attempts": 0, "max_restart_attempts": 3, "depends_on": [], "last_error": "OOM: out of memory"}
        }
    },
    {
        "hostname": "nova-virginia-02",
        "region": "us-east",
        "datacenter": "Virginia",
        "status": "online",
        "os": "Ubuntu 20.04",
        "uptime_hours": 5,
        "cpu_usage_percent": 78,
        "ram_usage_percent": 82,
        "disk_usage_percent": 60,
        "tags": ["production", "web", "high-traffic"],
        "on_call_team": "team-gamma",
        "services": {
            "nginx": {"status": "online", "port": 80, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": None},
            "docker_daemon": {"status": "down", "port": None, "auto_restart": False, "restart_attempts": 0, "max_restart_attempts": 0, "depends_on": [], "last_error": "failed to start containerd"}
        }
    },
    {
        "hostname": "nova-singapore-01",
        "region": "ap-southeast",
        "datacenter": "Singapore",
        "status": "online",
        "os": "Ubuntu 22.04",
        "uptime_hours": 200,
        "cpu_usage_percent": 35,
        "ram_usage_percent": 50,
        "disk_usage_percent": 70,
        "tags": ["production", "cdn"],
        "on_call_team": "team-delta",
        "services": {
            "varnish": {"status": "down", "port": 6081, "auto_restart": True, "restart_attempts": 2, "max_restart_attempts": 5, "depends_on": [], "last_error": "VCL compilation error"},
            "haproxy": {"status": "online", "port": 443, "auto_restart": True, "restart_attempts": 0, "max_restart_attempts": 5, "depends_on": [], "last_error": None}
        }
    }
]

# ---------------------------   STEP 2: SUMMARY   ------------------------

# summary_of_servers(formatted_server_list)

# ----------------------------   STEP 3: REGION   -------------------------

# region_filter(formatted_server_list)

# ---------------------------   STEP 4: PROBLEMS   ------------------------

# down_services(formatted_server_list)

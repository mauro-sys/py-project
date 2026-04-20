Python practice challenge

The 2 AM NOC Incident Problem
You are a DevOps engineer at a company called NovaCloud. Several Ubuntu VPS servers and the services running on them are going down for 
different reasons. Monitoring is noisy, alerts are piling up, and your task is to build a Python program that can inspect a large nested 
dictionary, filter useful information, identify what is broken, and decide what actions are valid.


-------------------------------------------------------


USE:

rules.py to read the rules
main.py to read the server infos and solution
functions.py to read the functions
index.html for a summary of the problem

-------------------------------------------------------


My prompt:

lets say there is a scenario that some services go down for different reasons, in some servers like ubuntu vps and I am a devops. I want 
to create a python problem with these, starting from big populated with infos dictionary, so that I can filter and find problems and 
solve them. give me also some rules, like I cant turn on this service is the server is down or some other valid reason. dont give me 
solution, just give me a very elaborated problem so I can solve. I have learnt python up to dictionaries and tuples. I want to create 
also filters for like filter only the region eu-central servers or like this on top of the service problems. be creative.
also add the quesiton to create a script that tries to turn on the services if it checks them and they are down. in any time, dont give
me solutions please

-------------------------------------------------------


Rules

# Rule 1: If the server is down, you cannot act on its services at all.
# Rule 2: A service with a dependency cannot start until all required dependencies on the same server are online.
# Rule 3: If auto_restart is false, the service requires manual intervention.
# Rule 4: If max_restart_attempts is 0, the service is not configured for restart attempts.
# Rule 5: If restart attempts already reached the maximum, no more attempts are allowed.
# Rule 6: A degraded server is reachable but unstable. Treat it as a warning, not as a full blocker.
# Rule 7: If port is None, that does not automatically mean the service is broken. It may be a worker or daemon.
# Rule 8: Very high disk usage may explain storage errors such as no space left on device.
# Rule 9: Very high RAM usage may help explain memory-related service failures such as OOM errors.
# Rule 10: One server can have multiple different problems at the same time. Your logic should not stop at the first issue.







to fix -- ctrl c and other inputs


Cannot restart if the server itself is down.
    check server status:
        if server_status != online
        Solved: physical start

Cannot restart if auto_restart is False.
    set auto_restart to TRUE 
        start

Cannot restart if restart_attempts is equal to max_restart_attempts.
    check restart_attempts:
        if restart_attempts = max_restart_attempts:
            restart_attempts = 0

Cannot restart if max_restart_attempts is 0.
    check max_restart_attempts:
        if max_restart_attempts = 0:
            max_restart_attempts = 5

Cannot restart if any service listed in depends_on is also down on the same server.
    check services:
        if service = down:
            check depends_on:
                if depends_on on:
                    start
                else:
                    depends_on = on
                
Can restart only if none of the blockers above exist.






main fuction
step 1 from 0-6
step 2 go back 1 step
or 
alert the support
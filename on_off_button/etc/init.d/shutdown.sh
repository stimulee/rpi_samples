#!/bin/bash

### BEGIN INIT INFO
# Provides:          shutdownBtn
# Required-Start:    $all
# Required-Stop:    
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Script to add the capability to shutdown the Raspberry Pi with a button
# Description:       Script to add the capability to shutdown the Raspberry Pi with a button
### END INIT INFO

case "$1" in
    start)
	/usr/bin/python /etc/init.d/shutdown.py &
	echo $! > /tmp/.shutdown-pid
        ;;
    stop)
	kill `cat /tmp/.shutdown-pid`
        ;;
    reload|restart)
        $0 stop
        $0 start
        ;;

    *)
        echo "Usage: $0 start|stop|restart|reload"
        exit 1
esac
exit 0

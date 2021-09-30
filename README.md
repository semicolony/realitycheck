Simple reachability monitoring - realitycheck

Baseline functions:
    Either run as minimalistic python3 http websocket, serving the index.html,
    or checking this server function via a list of IPs with subset of labels.

Idea:

    To monitor the reachability of a system, ping is not the most reliable way.
    Using a full tcp connection give a more solid way of monitoring reachability.

    For that, realitycheck can be used either as the server side, via a systemd
    unit providing a listening http socket, serving a basic index.html file; or
    it can be used as the probing side, sending the request to the listener and
    processing the response.

    Developed as a lightweight software which works in tandem with check_mk, the
    index.html file can provide any output.

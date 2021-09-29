# Either loop over all IPs or loop only over a certain set
# defined by the label argument passed from commandline.
#
# The loop runs a http request and the exit code is used to
# decide if the host is reachable or not.
#
# The list if IPs is hardcoded in dict style with each matching
# label as a value to the IP.

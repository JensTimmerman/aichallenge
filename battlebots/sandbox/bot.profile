name run_bot

# Only current user is available
noroot
# No priviliges whatsoever
caps.drop all
seccomp

# Log when someone tries to access a blacklisted file
tracelog

# Make a shadow fs for /dev, /etc and /tmp
private-dev
private-etc hostname  # Needs at least one file/dir argument
private-tmp
# Disable system management commands
include /etc/firejail/disable-mgmt.inc

# Allow restricted network access for compilation
netfilter

# Maximum file size (in bytes)
rlimit-fsize 100000000  # 100MB
# Maximum number of processes
rlimit-nproc 100
# Maximum number of file descriptors
rlimit-nofile 50
# Maximum number of pending signals
rlimit-sigpending 20

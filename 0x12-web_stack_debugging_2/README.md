0x12. Web stack debugging #2

- 0. Run software as another user - 0-iamsomeoneelse
	- Requirements:
		- write a Bash script that accepts one argument
		- the script should run the whoami command under the user passed as an argument
		- make sure to try your script by passing different users

- 1. Run Nginx as Nginx - 1-run_nginx_as_nginx
	- Requirements:
		- nginx must be running as nginx user
		- nginx must be listening on all active IPs on port 8080
		- You cannot use apt-get remove
		- Write a Bash script that configures the container to fit the above requirements


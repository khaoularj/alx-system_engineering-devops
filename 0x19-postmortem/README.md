POSTMERTEM
While i was working on the 0x0E. Web stack debugging #1 project, on the 2nd January approximately on 3:00 PM (UTC), an issue was keeping Ubuntu container’s Nginx installation from listening on port 80.
This conflict led to Nginx's failure to listen on the specified port.

Debugging Process:
to check the issue, i follow these steps:
	Navigate to the Nginx configuration directory: /etc/nginx/ located in sites-available.
	Open the nginx.conf file.
	Check the listen directive to ensure Nginx is configured to listen on the desired port (port 80 or an alternative port like 8080).

	Navigate to the Apache configuration directory: /etc/apache2/ located in sites-available.
	Open the httpd.conf or relevant configuration file.
	Verify that Apache is configured to listen on a different port than Nginx (e.g., port 80).

	Check for Port Binding Conflicts using the command "netstat" to ensure that only one service (either Nginx or Apache) is bound to port 80
	After making configuration changes, i restarted both Nginx and Apache services to apply the updates using these commands: sudo systemctl restart nginx and sudo systemctl restart apache2.

Summation:
In short, the configurations for Nginx and Apache were adjusted. Specifically, Nginx's nginx.conf file located in /etc/nginx/ was updated to listen on an alternative port (8080), while Apache's httpd.conf file located in /etc/apache2/ was modified to bind to port 80. 
The issue was resolved by adjusting the configurations of both Nginx and Apache to ensure they each listened on separate ports, thereby resolving the conflict.

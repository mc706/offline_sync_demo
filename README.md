Offline Sync Demo
=================

This is a demo piece of code to test the usability of writing an offline web application that syncs with the server.


Instead of writing data to the server via an API, this Single Page Web application writes its data to an IndexedDB in the
browser. A background polling task then syncs the IndexedDB database to the django database using UUID's and modified
timestamps to resolve conflicts. 


This is just a proof of concept demo.
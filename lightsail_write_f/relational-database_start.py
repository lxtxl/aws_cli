#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html
	delete-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database.html
	get-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html
	get-relational-databases : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-databases.html
	reboot-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-relational-database.html
	stop-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-relational-database.html
	update-relational-database : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/update-relational-database.html
    """

    write_parameter("lightsail", "start-relational-database")
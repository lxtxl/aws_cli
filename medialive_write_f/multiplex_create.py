#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex.html
	describe-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex.html
	list-multiplexes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplexes.html
	start-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/start-multiplex.html
	stop-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/stop-multiplex.html
	update-multiplex : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex.html
    """

    write_parameter("medialive", "create-multiplex")
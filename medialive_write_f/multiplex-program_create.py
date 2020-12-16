#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/delete-multiplex-program.html
	describe-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-multiplex-program.html
	list-multiplex-programs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-multiplex-programs.html
	update-multiplex-program : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/update-multiplex-program.html
    """

    write_parameter("medialive", "create-multiplex-program")
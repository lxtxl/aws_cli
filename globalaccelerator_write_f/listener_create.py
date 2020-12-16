#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/delete-listener.html
	describe-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-listener.html
	list-listeners : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-listeners.html
	update-listener : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-listener.html
    """

    write_parameter("globalaccelerator", "create-listener")
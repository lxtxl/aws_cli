#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/delete-preset.html
	list-presets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-presets.html
	read-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/read-preset.html
    """

    write_parameter("elastictranscoder", "create-preset")
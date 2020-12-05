#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-preset.html
	get-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-preset.html
	list-presets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-presets.html
	update-preset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-preset.html
    """

    write_parameter("mediaconvert", "delete-preset")
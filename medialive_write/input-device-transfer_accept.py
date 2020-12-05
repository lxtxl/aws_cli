#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	cancel-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/cancel-input-device-transfer.html
	list-input-device-transfers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-input-device-transfers.html
	reject-input-device-transfer : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/reject-input-device-transfer.html
    """

    write_parameter("medialive", "accept-input-device-transfer")
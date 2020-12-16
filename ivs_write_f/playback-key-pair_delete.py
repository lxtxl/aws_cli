#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-key-pair.html
	import-playback-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/import-playback-key-pair.html
	list-playback-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-key-pairs.html
    """

    write_parameter("ivs", "delete-playback-key-pair")
#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opsworks-cm/describe-node-association-status.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # node-association-status-token : The token returned in either the AssociateNodeResponse or the DisassociateNodeResponse.
    # server-name : The name of the server from which to disassociate the node.
    """

    execute_two_parameter("opsworks-cm", "describe-node-association-status", "node-association-status-token", "server-name", parameter_display_string)
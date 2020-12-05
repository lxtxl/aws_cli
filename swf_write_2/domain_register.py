#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/register-domain.html
if __name__ == '__main__':
    """
	deprecate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/deprecate-domain.html
	describe-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/describe-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/list-domains.html
	undeprecate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/swf/undeprecate-domain.html
    """

    parameter_display_string = """
    # name : Name of the domain to register. The name must be unique in the region that the domain is registered in.
The specified string must not start or end with whitespace. It must not contain a : (colon), / (slash), | (vertical bar), or any control characters (\u0000-\u001f | \u007f-\u009f ). Also, it must not be the literal string arn .
    # workflow-execution-retention-period-in-days : The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution isnât available in the results of visibility calls.
If you pass the value NONE or 0 (zero), then the workflow execution history isnât retained. As soon as the workflow execution completes, the execution record and its history are deleted.
The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: Amazon SWF Service Limits in the Amazon SWF Developer Guide .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("swf", "register-domain", "name", "workflow-execution-retention-period-in-days", add_option_dict)

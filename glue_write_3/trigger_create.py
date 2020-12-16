#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-trigger.html
if __name__ == '__main__':
    """
	delete-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-trigger.html
	get-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-trigger.html
	get-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-triggers.html
	list-triggers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-triggers.html
	start-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-trigger.html
	stop-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/stop-trigger.html
	update-trigger : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-trigger.html
    """

    parameter_display_string = """
    # name : The name of the trigger.
    # type : The type of the new trigger.
Possible values:

SCHEDULED
CONDITIONAL
ON_DEMAND
    # actions : The actions initiated by this trigger when it fires.
(structure)

Defines an action to be initiated by a trigger.
JobName -> (string)

The name of a job to be executed.

Arguments -> (map)

The job arguments used when this trigger fires. For this job run, they replace the default arguments set in the job definition itself.
You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.
For information about how to specify and consume your own Job arguments, see the Calling AWS Glue APIs in Python topic in the developer guide.
For information about the key-value pairs that AWS Glue consumes to set up your job, see the Special Parameters Used by AWS Glue topic in the developer guide.
key -> (string)
value -> (string)

Timeout -> (integer)

The JobRun timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters TIMEOUT status. The default is 2,880 minutes (48 hours). This overrides the timeout value set in the parent job.

SecurityConfiguration -> (string)

The name of the SecurityConfiguration structure to be used with this action.

NotificationProperty -> (structure)

Specifies configuration properties of a job run notification.
NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.


CrawlerName -> (string)

The name of the crawler to be used with this action.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("glue", "create-trigger", "name", "type", "actions", add_option_dict)

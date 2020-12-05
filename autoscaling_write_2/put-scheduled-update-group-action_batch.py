#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/batch-put-scheduled-update-group-action.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # auto-scaling-group-name : The name of the Auto Scaling group.
    # scheduled-update-group-actions : One or more scheduled actions. The maximum number allowed is 50.
(structure)

Describes information used for one or more scheduled scaling action updates in a  BatchPutScheduledUpdateGroupAction operation.
When updating a scheduled scaling action, all optional parameters are left unchanged if not specified.
ScheduledActionName -> (string)

The name of the scaling action.

StartTime -> (timestamp)

The date and time for the action to start, in YYYY-MM-DDThh:mm:ssZ format in UTC/GMT only and in quotes (for example, "2019-06-01T00:00:00Z" ).
If you specify Recurrence and StartTime , Amazon EC2 Auto Scaling performs the action at this time, and then performs the action based on the specified recurrence.
If you try to schedule the action in the past, Amazon EC2 Auto Scaling returns an error message.

EndTime -> (timestamp)

The date and time for the recurring schedule to end. Amazon EC2 Auto Scaling does not perform the action after this time.

Recurrence -> (string)

The recurring schedule for the action, in Unix cron syntax format. This format consists of five fields separated by white spaces: [Minute] [Hour] [Day_of_Month] [Month_of_Year] [Day_of_Week]. The value must be in quotes (for example, "30 0 1 1,6,12 *" ). For more information about this format, see Crontab .
When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.

MinSize -> (integer)

The minimum size of the Auto Scaling group.

MaxSize -> (integer)

The maximum size of the Auto Scaling group.

DesiredCapacity -> (integer)

The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("autoscaling", "batch-put-scheduled-update-group-action", "auto-scaling-group-name", "scheduled-update-group-actions", add_option_dict)

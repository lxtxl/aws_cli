#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/create-dataset.html
if __name__ == '__main__':
    """
	delete-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/delete-dataset.html
	describe-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/describe-dataset.html
	list-datasets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/list-datasets.html
	update-dataset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/update-dataset.html
    """

    parameter_display_string = """
    # dataset-name : The name of the data set.
    # actions : A list of actions that create the data set contents.
(structure)

A DatasetAction object that specifies how data set contents are automatically created.
actionName -> (string)

The name of the data set action by which data set contents are automatically created.

queryAction -> (structure)

An SqlQueryDatasetAction object that uses an SQL query to automatically create data set contents.
sqlQuery -> (string)

A SQL query string.

filters -> (list)

Prefilters applied to message data.
(structure)

Information that is used to filter message data, to segregate it according to the timeframe in which it arrives.
deltaTime -> (structure)

Used to limit data to that which has arrived since the last execution of the action.
offsetSeconds -> (integer)

The number of seconds of estimated in-flight lag time of message data. When you create dataset contents using message data from a specified timeframe, some message data might still be in flight when processing begins, and so do not arrive in time to be processed. Use this field to make allowances for the in flight time of your message data, so that data not processed from a previous timeframe is included with the next timeframe. Otherwise, missed message data would be excluded from processing during the next timeframe too, because its timestamp places it within the previous timeframe.

timeExpression -> (string)

An expression by which the time of the message data might be determined. This can be the name of a timestamp field or a SQL expression that is used to derive the time the message data was generated.





containerAction -> (structure)

Information that allows the system to run a containerized application to create the dataset contents. The application must be in a Docker container along with any required support libraries.
image -> (string)

The ARN of the Docker container stored in your account. The Docker container contains an application and required support libraries and is used to generate dataset contents.

executionRoleArn -> (string)

The ARN of the role that gives permission to the system to access required resources to run the containerAction . This includes, at minimum, permission to retrieve the dataset contents that are the input to the containerized application.

resourceConfiguration -> (structure)

Configuration of the resource that executes the containerAction .
computeType -> (string)

The type of the compute resource used to execute the containerAction . Possible values are: ACU_1 (vCPU=4, memory=16 GiB) or ACU_2 (vCPU=8, memory=32 GiB).

volumeSizeInGB -> (integer)

The size, in GB, of the persistent storage available to the resource instance used to execute the containerAction (min: 1, max: 50).


variables -> (list)

The values of variables used in the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of stringValue , datasetContentVersionValue , or outputFileUriValue .
(structure)

An instance of a variable to be passed to the containerAction execution. Each variable must have a name and a value given by one of stringValue , datasetContentVersionValue , or outputFileUriValue .
name -> (string)

The name of the variable.

stringValue -> (string)

The value of the variable as a string.

doubleValue -> (double)

The value of the variable as a double (numeric).

datasetContentVersionValue -> (structure)

The value of the variable as a structure that specifies a dataset content version.
datasetName -> (string)

The name of the dataset whose latest contents are used as input to the notebook or application.


outputFileUriValue -> (structure)

The value of the variable as a structure that specifies an output file URI.
fileName -> (string)

The URI of the location where dataset contents are stored, usually the URI of a file in an S3 bucket.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotanalytics", "create-dataset", "dataset-name", "actions", add_option_dict)

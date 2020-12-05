#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/start-simulation-job-batch.html
if __name__ == '__main__':
    """
	cancel-simulation-job-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/cancel-simulation-job-batch.html
	describe-simulation-job-batch : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-simulation-job-batch.html
	list-simulation-job-batches : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-simulation-job-batches.html
    """

    parameter_display_string = """
    # create-simulation-job-requests : A list of simulation job requests to create in the batch.
(structure)

Information about a simulation job request.
outputLocation -> (structure)

The output location.
s3Bucket -> (string)

The S3 bucket for output.

s3Prefix -> (string)

The S3 folder in the s3Bucket where output files will be placed.


loggingConfig -> (structure)

The logging configuration.
recordAllRosTopics -> (boolean)

A boolean indicating whether to record all ROS topics.


maxJobDurationInSeconds -> (long)

The maximum simulation job duration in seconds. The value must be 8 days (691,200 seconds) or less.

iamRole -> (string)

The IAM role name that allows the simulation instance to call the AWS APIs that are specified in its associated policies on your behalf. This is how credentials are passed in to your simulation job.

failureBehavior -> (string)

The failure behavior the simulation job.

Continue

Restart the simulation job in the same host instance.

Fail

Stop the simulation job and terminate the instance.

useDefaultApplications -> (boolean)

Boolean indicating whether to use default simulation tool applications.

robotApplications -> (list)

The robot applications to use in the simulation job.
(structure)

Application configuration information for a robot.
application -> (string)

The application information for the robot application.

applicationVersion -> (string)

The version of the robot application.

launchConfig -> (structure)

The launch configuration for the robot application.
packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.
key -> (string)
value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.
portMappings -> (list)

The port mappings for the configuration.
(structure)

An object representing a port mapping.
jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.




streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.




simulationApplications -> (list)

The simulation applications to use in the simulation job.
(structure)

Information about a simulation application configuration.
application -> (string)

The application information for the simulation application.

applicationVersion -> (string)

The version of the simulation application.

launchConfig -> (structure)

The launch configuration for the simulation application.
packageName -> (string)

The package name.

launchFile -> (string)

The launch file name.

environmentVariables -> (map)

The environment variables for the application launch.
key -> (string)
value -> (string)

portForwardingConfig -> (structure)

The port forwarding configuration.
portMappings -> (list)

The port mappings for the configuration.
(structure)

An object representing a port mapping.
jobPort -> (integer)

The port number on the simulation job instance to use as a remote connection point.

applicationPort -> (integer)

The port number on the application.

enableOnPublicIp -> (boolean)

A Boolean indicating whether to enable this port mapping on public IP.




streamUI -> (boolean)

Boolean indicating whether a streaming session will be configured for the application. If True , AWS RoboMaker will configure a connection so you can interact with your application as it is running in the simulation. You must configure and luanch the component. It must have a graphical user interface.


worldConfigs -> (list)

A list of world configurations.
(structure)

Configuration information for a world.
world -> (string)

The world generated by Simulation WorldForge.





dataSources -> (list)

Specify data sources to mount read-only files from S3 into your simulation. These files are available under /opt/robomaker/datasources/data_source_name .

Note
There is a limit of 100 files and a combined size of 25GB for all DataSourceConfig objects.

(structure)

Information about a data source.
name -> (string)

The name of the data source.

s3Bucket -> (string)

The S3 bucket where the data files are located.

s3Keys -> (list)

The list of S3 keys identifying the data source files.
(string)



vpcConfig -> (structure)

If your simulation job accesses resources in a VPC, you provide this parameter identifying the list of security group IDs and subnet IDs. These must belong to the same VPC. You must provide at least one security group and two subnet IDs.
subnets -> (list)

A list of one or more subnet IDs in your VPC.
(string)

securityGroups -> (list)

A list of one or more security groups IDs in your VPC.
(string)

assignPublicIp -> (boolean)

A boolean indicating whether to assign a public IP address.


compute -> (structure)

Compute information for the simulation job
simulationUnitLimit -> (integer)

The simulation unit limit. Your simulation is allocated CPU and memory proportional to the supplied simulation unit limit. A simulation unit is 1 vcpu and 2GB of memory. You are only billed for the SU utilization you consume up to the maximim value provided. The default is 15.


tags -> (map)

A map that contains tag keys and tag values that are attached to the simulation job request.
key -> (string)
value -> (string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("robomaker", "start-simulation-job-batch", "create-simulation-job-requests", add_option_dict)





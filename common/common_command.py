#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import subprocess
import shlex
from common.config_util import read_work_profile_file, read_setting_file
from common.MakeTextFile import MakeTextFile
from datetime import datetime


def subprocess_open_when_shell_false_with_shelx(command):
    my_env = os.environ
    popen = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, env=my_env)
    (stdoutdata,stderrdata) = popen.communicate()
    return stdoutdata, stderrdata

def setting_default_generate(settings):
    """
    generate용 parameter 설정하기
    """
    common_parameter_list = []
    if settings['is_proxy']:
        os.environ['HTTP_PROXY'] = "http://{}:{}".format(settings['proxy_ip'], settings['proxy_port'])
        os.environ['HTTPS_PROXY'] = "http://{}:{}".format(settings['proxy_ip'], settings['proxy_port'])
        common_parameter_list.append("--no-verify-ssl")
    return common_parameter_list

def setting_default_command_parameter(settings):
    """
    기본 parameter 설정하기
    """
    common_parameter_list = setting_default_generate(settings)
    common_parameter_list.append('--profile')
    common_parameter_list.append(settings['profile'])
    common_parameter_list.append('--region')
    common_parameter_list.append(settings['region'])

    common_parameter_value = " ".join(common_parameter_list)

    return common_parameter_value

def execute_process(profile_name, service_name, command_name, add_parameter_list):
    settings = read_setting_file()
    profile_config = read_work_profile_file(profile_name)

    settings.update(profile_config)
    common_parameter_value = setting_default_command_parameter(settings)

    aws_command_list = ["aws", service_name, command_name]

    if "--output" not in add_parameter_list:
        aws_command_list.append("--output")
        aws_command_list.append(settings["output"])
    aws_command_list = aws_command_list + add_parameter_list
    aws_command_list.append(common_parameter_value)
    execute_command = " ".join(aws_command_list)

    result_path = settings['result_path']
    current_now = datetime.now()
    current_string = current_now.strftime("%Y%m%d")
    current_time_string = current_now.strftime("%H%M%S")
    change_result_path = result_path.replace("YYYYMMDD", current_string)

    save_file_name = None

    if not os.path.isdir(change_result_path):
        os.mkdir(change_result_path)
    if save_file_name is None:
        file_name=f"{change_result_path}/{current_time_string}_{profile_name}_{service_name}_{command_name}.text"
    else:
        file_name = save_file_name

    if os.path.isfile(file_name):
        os.remove(file_name)

    return excute_save_file(execute_command, file_name)



def execute_generate(service_name, command_name):
    settings = read_setting_file()

    common_parameter_list = setting_default_generate(settings)
    common_parameter_value = " ".join(common_parameter_list)
    aws_command_list = ["aws", service_name, command_name]

    aws_command_list.append(common_parameter_value)
    aws_command_list.append("--generate-cli-skeleton")
    execute_command = " ".join(aws_command_list)

    current_now = datetime.now()
    current_string = current_now.strftime("%Y%m%d")
    current_time_string = current_now.strftime("%H%M%S")

    file_name = f"{current_time_string}_{service_name}_{command_name}.json"

    excute_save_file(execute_command, file_name)


def excute_save_file(execute_command, file_name):
    print("make_file_name: ", file_name)
    result_savefilename = MakeTextFile(file_name)
    print(execute_command)
    stdoutdata, stderrdata = subprocess_open_when_shell_false_with_shelx(execute_command)
    if stdoutdata:
        print("result ==> ", "*" * 20)
        print(stdoutdata)
        result_savefilename.writeMultiSave(stdoutdata)
        print("*" * 40)
    if stderrdata:
        for line in stderrdata.strip().split("\n"):
            if line.find("connectionpool.py:1004") == -1 and line.find("InsecureRequestWarning") == -1:
                print(line)
    result_savefilename.closeFile()
    return stdoutdata


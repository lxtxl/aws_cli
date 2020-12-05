#!/usr/bin/python
# -*- codding: utf-8 -*-
import sys
import os
from common.common_command import execute_process, execute_generate
from common.config_util import read_work_profile_file, read_setting_file
from common.common_util import lprint

def read_one_parameter(service_name, command_name, unique_name, add_option_dict, is_custom_check = False):
    parameter_num = len(sys.argv)

    no_value_parameter_list, parameter_display_string, output_string, query_string = find_add_options(add_option_dict)
    if not is_custom_check:
        if parameter_num != 3:
            print("config value is not exist")
            print("Usage: python {} <config> <{}>".format(sys.argv[0]), unique_name)
            sys.exit(1)

    profile_name = sys.argv[1]
    unique_value = sys.argv[2]

    add_parameter_list = []
    if profile_name == "gen":
        return execute_generate(service_name, command_name)
    else:
        replace_unique_name = "--" + unique_name
        option_list = make_setting_options(profile_name, add_option_dict)
        add_parameter_list.append(replace_unique_name)
        add_parameter_list.append(unique_value)
        add_parameter_list = add_parameter_list + option_list
        if output_string != None:
            add_parameter_list.append("--output")
            add_parameter_list.append(output_string)
        if query_string != None:
            add_parameter_list.append("--query")
            add_parameter_list.append(query_string)
        return execute_process(profile_name, service_name, command_name, add_parameter_list)

def execute_two_parameter(service_name, command_name, unique_name, unique2_name, parameter_display_string):
    parameter_num = len(sys.argv)

    if parameter_num != 4:
        print("config value is not exist")
        print("Usage: python {} <config> <{}> <{}?".format(sys.argv[0], unique_name, unique2_name))
        print(parameter_display_string)
        sys.exit(1)

    profile_name = sys.argv[1]
    unique_value = sys.argv[2]
    unique2_value = sys.argv[3]
    replace_unique_name = "--" + unique_name
    replace_unique2_name = "--" + unique2_name
    execute_process(profile_name, service_name, command_name, [replace_unique_name, unique_value, replace_unique2_name, unique2_value])

def read_no_parameter_custom(service_name, command_name, add_option_dict):
    return read_no_parameter(service_name, command_name, add_option_dict, True)

def read_one_parameter_custom(service_name, command_name, unique_name, add_option_dict):
    return read_one_parameter(service_name, command_name, unique_name, add_option_dict, True)

def read_no_parameter(service_name, command_name, add_option_dict, is_custom_check = False):
    parameter_num = len(sys.argv)

    no_value_parameter_list, parameter_display_string, output_string, query_string = find_add_options(add_option_dict)
    if not is_custom_check:
        if parameter_num != 2:
            print("config value is not exist")
            print("Usage: python {} <config>".format(sys.argv[0]))
            sys.exit(1)

    profile_name = sys.argv[1]

    add_parameter_list = []
    if profile_name == "gen":
        return execute_generate(service_name, command_name)
    else:
        option_list = make_setting_options(profile_name, add_option_dict)
        add_parameter_list = add_parameter_list + option_list
        if output_string != None:
            add_parameter_list.append("--output")
            add_parameter_list.append(output_string)
        if query_string != None:
            add_parameter_list.append("--query")
            add_parameter_list.append(query_string)
        return execute_process(profile_name, service_name, command_name, add_parameter_list)

def read_setting(profile_name):
    settings = read_setting_file()
    profile_config = read_work_profile_file(profile_name)

    settings.update(profile_config)
    return settings

def find_add_options(add_option_dict):
    no_value_parameter_list = []
    parameter_display_string = ""
    output_string = None
    query_string = None
    for key, value in add_option_dict.items():
        if key == "no_value_parameter_list":
            no_value_parameter_list = value
        elif key == "parameter_display_string":
            parameter_display_string = value
        elif key == "output":
            output_string = value
        elif key == "query":
            query_string = value
    return no_value_parameter_list, parameter_display_string, output_string, query_string

def make_setting_options(profile_name, kwargs):
    setting_matching_parameter = None
    setting_key = None
    if "setting_key" in kwargs.keys():
        setting_matching_parameter = kwargs["setting_matching_parameter"]
        setting_key = kwargs["setting_key"]
        settings = read_setting(profile_name)
        if setting_key not in settings.keys():
            return None
        return [setting_matching_parameter, settings[setting_key]]
    return []


def write_one_parameter(service_name, command_name, unique_name, **kwargs):
    parameter_num = len(sys.argv)

    no_value_parameter_list, parameter_display_string = find_add_options(kwargs)

    if parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config> <{}>".format(sys.argv[0], unique_name))
        print(parameter_display_string)
        sys.exit(0)

    profile_name = sys.argv[1]
    unique_value = sys.argv[2]
    answer = input("Enter yes or no: ")
    if answer == "yes":
        replace_unique_name = "--" + unique_name
        add_parameter_list = [replace_unique_name, unique_value]
        add_parameter_list = add_parameter_list + no_value_parameter_list
        execute_process(profile_name, service_name, command_name, add_parameter_list)
    else:
        sys.exit()


def write_two_parameter(service_name, command_name, unique1_name, unique2_name, **kwargs):
    parameter_num = len(sys.argv)

    no_value_parameter_list, parameter_display_string = find_add_options(kwargs)
    if parameter_num != 4:
        print("config value is not exist")
        print("Usage: python {} <config> <{}> <{}>".format(sys.argv[0], unique1_name, unique2_name))
        sys.exit(1)

    profile_name = sys.argv[1]
    unique1_value = sys.argv[2]
    unique2_value = sys.argv[3]
    answer = input("Enter yes or no: ")
    if answer == "yes":
        replace_unique1_name = "--" + unique1_name
        replace_unique2_name = "--" + unique2_name
        execute_process(profile_name, service_name, command_name, [replace_unique1_name, unique1_value, replace_unique2_name, unique2_value])
    else:
        sys.exit()


def write_parameter(service_name, command_name):
    parameter_num = len(sys.argv)

    if parameter_num != 2 and parameter_num != 3:
        print("config value is not exist")
        print("Usage: python {} <config>".format(sys.argv[0]))
        print("Usage: python {} <config> <input_filename>".format(sys.argv[0]))
        sys.exit(1)

    profile_name = sys.argv[1]
    add_parameter_list = []
    if profile_name == "gen":
        execute_generate(service_name, command_name)
    elif parameter_num == 3:
        input_filename = sys.argv[2]
        answer = input("Enter yes or no: ")
        if not os.path.isfile(input_filename):
            lprint("input filename is not exist")
            sys.exit()
        if answer == "yes":
            add_parameter_list.append("--cli-input-json")
            add_parameter_list.append(input_filename)
            execute_process(profile_name, service_name, command_name, add_parameter_list)
        else:
            sys.exit()
    else:
        execute_generate(service_name, command_name)

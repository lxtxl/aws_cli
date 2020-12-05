#!/usr/bin/python
# -*- codding: utf-8 -*-
import logging
import os.path
from common.MakeTextFile import MakeTextFile

logging.basicConfig(filename='logging.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def lprint(sentence):
    print(sentence)
    logger.info(sentence)

def copy_file(common_dict, parameter_num, group_name, type, sample_filename, write_mode, detail_mode = ""):
    service_name = common_dict['service_name']
    if parameter_num == 0:
        directory_name = "{}_{}".format(service_name, write_mode)
    else:
        directory_name = "{}_{}_{}".format(service_name, write_mode, parameter_num)
    file_name = "{}/{}_{}{}.py".format(directory_name, group_name, type, detail_mode)
    if not os.path.isdir(directory_name):
        os.mkdir(directory_name)
    if os.path.isfile(file_name):
        lprint("{} exist".format(file_name))
    else:
        file_fullpath = "sample/{}".format(sample_filename)
        lprint("{} file make start [{}]".format(file_name, file_fullpath))
        f = open(file_fullpath, 'r')
        data = f.read()
        for key, val in common_dict.items():
            lprint("{} => {}".format(key, val))
            data = data.replace("<{}>".format(key), val)
        f.close()
        saveFile = MakeTextFile(file_name)
        saveFile.writeSave(data)
        saveFile.closeFile()
        lprint("{} file save".format(file_name))
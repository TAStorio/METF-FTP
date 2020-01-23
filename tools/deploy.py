# Packs the mod contents into a .zip and optionally puts it into %AppData%/Factorio/mods and overwrites any old versions

import argparse
import zipfile
import os
import json
from shutil import copyfile

argparser = argparse.ArgumentParser()
argparser.add_argument('--copy', dest='copy', action='store_true',
                    help='Copy the resulting zip into factorio mods folder')
argparser.add_argument('--target', dest='deploy', action='append',
                    help='Optional mods folders for copying the results into.')
argparser.add_argument('--build', dest='destination', action='store',
                    default='./build/',
                    help='Build folder for the zip')
#

arguments = vars(argparser.parse_args())

INFO = "info.json"

files = [
	"control.lua",
	"info.json"
]

with open(INFO) as f:
	info = json.load(f)
	MOD_NAME = info["name"]
	VERSION = info["version"]

destination = arguments["destination"]

do_deploy = arguments["copy"]
deploytargets = arguments["deploy"]
if deploytargets is None:
	do_deploy = False
elif len(deploytargets) > 0:
	do_deploy = True

MOD_NAME_FULL = MOD_NAME+"_"+VERSION
zip_name = MOD_NAME_FULL+".zip"
zip_path = os.path.join(destination, zip_name)

with zipfile.ZipFile(zip_path, "w") as zipped:
	for filename in files:
		zipped.write(filename, MOD_NAME_FULL+"\\"+filename)

if do_deploy:
	for target in deploytargets:
		copyfile(zip_path, os.path.join(target, zip_name))
import json
import os
import shutil

def write(filetowrite, data):
    with open(filetowrite, "w") as opentag:
        opentag.write(data)
        opentag.close()
def write_binary(filetowrite, data):
    with open(filetowrite, "wb") as opentag:
        opentag.write(data)
        opentag.close()
def read(filetoread):
    with open(filetoread, "r") as opentag:
        data = opentag.read()
        opentag.close()
        return data
def read_binary(filetoread):
    with open(filetoread, "rb") as opentag:
        data = opentag.read()
        opentag.close()
        return data
def add(filetowrite, data):
    with open(filetowrite, "a") as opentag:
        opentag.write(data)
        opentag.close()
def add_binary(filetowrite, data):
    with open(filetowrite, "ab") as opentag:
        opentag.write(data)
        opentag.close()
def remove_file(filetoremove):
    os.remove(filetoremove)
def listdir(dirtolist):
    return os.listdir(dirtolist)
def read_json(filepath: str):
    f = open (filepath, "r")
    data = json.loads(f.read())
    f.close()
    return data
def makeZipArchive(folder: str, outputFile: str):
    if outputFile.endswith(".zip"):
        outputFile = outputFile.split(".")[0]
    shutil.make_archive(outputFile, "zip", folder)
def write_json(d: dict, outfile: str, indent: int = 4):
    with open(outfile, "w") as outfile:
        json.dump(d, outfile, indent=indent)
def append_json(outfile: str, d: dict, indent: int = 4):
    with open(outfile, "r") as file:
        data = json.load(file)
    data.update(d)
    with open(outfile, "w") as file:
        json.dump(data, file, indent=indent)
def _append_json(name, value, outfile: str, indent: int = 4):
    with open(outfile, "r") as file:
        data = json.load(file)
    data.update({name:value})
    with open(outfile, "w") as file:
        json.dump(data, file, indent=indent)
def copyFile(filename: str, output: str):
        shutil.copy(filename, output)
def writefiles(filepaths: list, data: list):
    for __ in range(len(filepaths)):
        write(filepaths[__], data[__])



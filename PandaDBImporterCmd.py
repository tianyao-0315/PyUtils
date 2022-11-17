import os
import sys

def abslouteFilePath(path):
    listdir = os.listdir(path)
    filepath = path
    allfile = []
    for file in listdir:
        allfile.append(filepath + '/' + file)
    return allfile

def getAllfilesAsStr(allfile, mode):
    prefix = ""
    if mode=="node":
        prefix = "--nodes="
    if mode== "relation":
        prefix = "--relationships="
    finalResult =prefix+"\""
    for file in allfile:
        finalResult += (file + ",")
    finalResult
    return str(finalResult)[:-1]+"\""

if __name__ == '__main__':
    srcDir = os.path.abspath(sys.argv[1])
    pandaRootPath = os.path.abspath(sys.argv[2])
    databaseName = os.path.join(pandaRootPath, sys.argv[3])
    targetNodeDir = os.path.join(srcDir, "nodes")
    targetRelDir = os.path.join(srcDir, "relations")

    # bashName = "panda-admin-import"
    delimiter = "|"
    array_delimiter = ";"

    allNodeFilesStr = getAllfilesAsStr(abslouteFilePath(targetNodeDir), "node")
    allRelFilesStr = getAllfilesAsStr(abslouteFilePath(targetRelDir), "relation")
    cmd = "--db-path={} {} {} --delimeter=\"{}\" --array-delimeter=\"{}\"".format(databaseName,
                                                                                 allNodeFilesStr, allRelFilesStr, delimiter, array_delimiter)
    print(cmd)
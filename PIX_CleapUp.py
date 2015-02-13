#!/usr/bin/env python
'''
    PIX_CleanUp.py
    
    
    Created by Clare Brody on 10/02/15.
    Copyright (c) 2015 Park Road Post Production. All rights reserved.
	'''

# ------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------
import os
import sys
import shutil
import fnmatch
import glob
import subprocess

import os
import glob


__VERSION__ = 0.0


# ------------------------------------------------------------------------------
# User-Defined Variables
# ------------------------------------------------------------------------------

# sourcepath = getOnlineDir()
# dirs = os.listdir(sourcepath)



# def PIX_CleanUp():
# print
# onlineDir = raw_input("Please enter Path of the PIX package: ").strip()
#     print "You have entered: ", onlineDir
#     print
#
#
# 	getOnlineDir()
#
# 	for file in dirs:
# 		print file
#
# 	        for sroot, sdirs, sfiles in os.walk(onlineshot):
#             for sdir in sdirs:
#                 if fnmatch.fnmatch(sdir, 'THB_*_LE'):
#
#
# def list_movs(onlineDir):
#
#
#
#
# if __name__ == '__main__':
# 	PIX_CleanUp()

# onlineDir = '/Volumes/Camilla/DI/_Wrangling/temp_clare/Scripts/_Python_Scripts/PIX_CleanUp/Test_Package/PDR_Del0001_150119'
#
#
# def PIX_CleanUp():
#     print
#     onlineDir = raw_input("Please enter Path of the PIX package: ").strip()
#     print "You have entered: ", onlineDir
#
#     print

    # for sroot, sdirs, sfiles in os.walk(onlineDir):
    #     for sdir in sdirs:
    #         print sdir

#this worked at listing all last directories
#     rootDir = onlineDir
#     for dirName, subdirList, fileList in os.walk(rootDir):
#         print('Found directory: %s' % dirName)
# #        for fname in fileList:
# #            print('\t%s' % fname)

    # rootDir = onlineDir
    # for dirName, subdirList, fileList in os.walk(rootDir):
    #     if dirName == 'PIX'
    #     print('Found directory: %s' % dirName)
        # for fname in fileList:
        #     print('\t%s' % fname)
    # Remove the first entry in the list of sub-directories
    # if there are any sub-directories present
    #     if len(subdirList) > 0:
    #         del subdirList[:0]


#     for path, dirs, files in os.walk(os.path.abspath(onlineDir)):
#         for filename in fnmatch.filter(files, pattern):
#             yield os.path.join(path, filename)
#
# if __name__ == '__main__':
#     PIX_CleanUp()

########start of code from internet

# # Function for getting files from a folder
# def fetchFiles(pathToFolder, flag, keyWord):
# 	'''	fetchFiles() requires three arguments: pathToFolder, flag and keyWord
#
# 	flag must be 'STARTS_WITH' or 'ENDS_WITH'
# 	keyWord is a string to search the file's name
#
# 	Be careful, the keyWord is case sensitive and must be exact
#
# 	Example: fetchFiles('/Documents/Photos/','ENDS_WITH','.jpg')
#
# 	returns: _pathToFiles and _fileNames '''
#
# 	_pathToFiles = []
# 	_fileNames = []
#
# 	for dirPath, dirNames, fileNames in os.walk(pathToFolder):
# 		if flag == 'ENDS_WITH':
# 			selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.endswith(keyWord)]
# 			_pathToFiles.extend(selectedPath)
#
# 			selectedFile = [item for item in fileNames if item.endswith(keyWord)]
# 			_fileNames.extend(selectedFile)
#
# 		elif flag == 'STARTS_WITH':
# 			selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.startswith(keyWord)]
# 			_pathToFiles.extend(selectedPath)
#
# 			selectedFile = [item for item in fileNames if item.startswith(keyWord)]
# 			_fileNames.extend(selectedFile)
#
# 		else:
# 			print fetchFiles.__doc__
# 			break
#
# 		# Try to remove empty entries if none of the required files are in directory
# 		try:
# 			_pathToFiles.remove('')
# 			_imageFiles.remove('')
# 		except ValueError:
# 			pass
#
# 		# Warn if nothing was found in the given path
# 		if selectedFile == []:
# 			print 'No files with given parameters were found in:\n', dirPath, '\n'
#
# 	print len(_fileNames), 'files were found is searched folder(s)'
#
# 	return _pathToFiles, _fileNames

########end of code from internet


# Function for getting files from a folder
def fetchFiles(pathToFolder, flag, keyWord):
	'''	fetchFiles() requires three arguments: pathToFolder, flag and keyWord

	flag must be 'STARTS_WITH' or 'ENDS_WITH'
	keyWord is a string to search the file's name

	Be careful, the keyWord is case sensitive and must be exact

	Example: fetchFiles('/Documents/Photos/','ENDS_WITH','.jpg')

	returns: _pathToFiles and _fileNames '''



	_pathToFiles = []
	_fileNames = []

	for dirPath, dirNames, fileNames in os.walk(pathToFolder):
		if flag == 'ENDS_WITH':
			selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.endswith(keyWord)]
			_pathToFiles.extend(selectedPath)

			selectedFile = [item for item in fileNames if item.endswith(keyWord)]
			_fileNames.extend(selectedFile)

		elif flag == 'STARTS_WITH':
			selectedPath = [os.path.join(dirPath,item) for item in fileNames if item.startswith(keyWord)]
			_pathToFiles.extend(selectedPath)

			selectedFile = [item for item in fileNames if item.startswith(keyWord)]
			_fileNames.extend(selectedFile)

		else:
			print fetchFiles.__doc__
			break

		# Try to remove empty entries if none of the required files are in directory
		try:
			_pathToFiles.remove('')
			_imageFiles.remove('')
		except ValueError:
			pass

		# Warn if nothing was found in the given path
		if selectedFile == []:
			print 'No files with given parameters were found in:\n', dirPath, '\n'

	print len(_fileNames), 'files were found is searched folder(s)'

	return _pathToFiles, _fileNames


import os, errno

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured


oldFile = open('ORBvoc.txt', 'r')
silentremove('newORBvoc.txt')
newFile = open('newORBvoc.txt','w')

firstLine = oldFile.readline()
newFile.write(firstLine)

lines = oldFile.readlines()

for line in lines:
	list = line.split(" ")
	list[-1] = list[-1].rstrip('\n')
	newFile.write(' '.join(list[0:2]))
	newFile.write(' ' + list[-1] + ' ')
	newFile.write(' '.join(list[2:-1]))
	newFile.write('\n')
	
oldFile.close()
newFile.close()
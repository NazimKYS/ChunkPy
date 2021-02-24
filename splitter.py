import argparse
import sys
import re
import os


# define the function to split the file into smaller chunks
def splitFile(fileName,fileExtension, chunkSize):
    # read the contents of the file
    inputFile=fileName+fileExtension
    f = open(inputFile, 'rb')
    data = f.read()
    f.close()

# get the length of data, ie size of the input file in bytes
    bytes = len(data)

# calculate the number of chunks to be created
    if sys.version_info.major == 3:
        noOfChunks = int(bytes / chunkSize)
    elif sys.version_info.major == 2:
        noOfChunks = bytes / chunkSize
    if(bytes % chunkSize):
        noOfChunks += 1

# create a metadata txt file for writing metadata
    directory="chunks_of_"+fileName
    if not os.path.exists(directory):
        os.makedirs(directory)
    metadata_file = directory+"/metaData.txt" 
    f = open(metadata_file, 'w')
    f.write('fileName = ' + fileName + '\n')
    f.write('fileExtension = ' + fileExtension + '\n')
    f.write('ChunkNumber = ' + str(noOfChunks) + '\n')
    f.write('ChunkSize = ' + str(chunkSize) + '\n')
    f.close()
    

    chunkNames = []
    j = 0
    for i in range(0, bytes + 1, chunkSize):
        j += 1
        fn1 = directory+"/chunk_%s_Of_%s%s" % (j, noOfChunks,fileExtension)
        chunkNames.append(fn1)
        f = open(fn1, 'wb')
     
        f.write(data[i:i + chunkSize])
        f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', action="store", help='provide input filename as first argument')
    parser.add_argument('chuncksize', action="store", type=int,
                        help='provide chucksize as second arguments.. Ex: 10000000 = 10 MB')
    args = parser.parse_args()
    if args.filename and args.chuncksize:
        fileNameWithExtension= re.split('[.]',args.filename)
        #fullName=fileNameWithExtension[0]+str(".")+fileNameWithExtension[1]
        splitFile(fileNameWithExtension[0],"."+fileNameWithExtension[1], args.chuncksize)

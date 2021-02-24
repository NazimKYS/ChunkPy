import os
import argparse

# define the function to join the chunks of files into a single file


def joinFiles(chunksFolder):
    file1 = open(chunksFolder+'metaData.txt', 'r')
    allLines=file1.read().splitlines()
    keysValues = {}
    for line in allLines:
        keyValue = line.split('=')
        keysValues[str(keyValue[0]).replace(" ", "")] = str(keyValue[-1]).replace(" ", "")
    
    #print(keysValues["fileName"])
    file1.close()
 
    dataList = []
    noOfChunks=int(keysValues["ChunkNumber"])
    fileExtension=keysValues["fileExtension"]
    j = 0
    for i in range(0, noOfChunks, 1):
        j += 1
        chunkName = "chunk_"+str(j)+"_Of_"+str(noOfChunks)+fileExtension 
        f = open(chunksFolder+chunkName, 'rb')
        dataList.append(f.read())
        f.close()

    j = 0
    for i in range(0, noOfChunks, 1):
        j += 1
        chunkName = "chunk_"+str(j)+"_Of_"+str(noOfChunks)+fileExtension 
        # Deleting the chunck file.
        os.remove(chunksFolder+"/"+chunkName)

    newFileName=keysValues["fileName"]+"FromChunks"+fileExtension
    f2 = open(newFileName, 'wb')
    for data in dataList:
        f2.write(data)
    f2.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('chunksFolder', action="store",
                        help='provide original filename as first argument')
    """ parser.add_argument('new_filename', action="store",
                        help='provide new filename as second argument')
    parser.add_argument('chunks', action="store",
                        help='provide number of chunks as third argument', type=int) """
    args = parser.parse_args()
    if args.chunksFolder :
        #joinFiles('one.mp4', 'myNewFile.mp4', 11)
        #joinFiles(args.orig_filename, args.new_filename)
        joinFiles(args.chunksFolder)
        

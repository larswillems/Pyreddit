from helper import deleteTemporaryFiles, deleteFiles
from redditScraper import getContent

print("delete previous output videos")
deleteFiles("../output")

getContent(2)

deleteTemporaryFiles()
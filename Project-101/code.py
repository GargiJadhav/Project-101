from os import access
import dropbox

class TransferData :
    def __init__(self , accessToken) :
       self.AccessToken = accessToken

    def uploadFiles(self , source , destination):
        dbx = dropbox.Dropbox(self.AccessToken)

        f = open(source,'rb')
        dbx.files_upload(f.read() , destination)

def main():
        accessToken = "sl.BGs01h0stkM-oHH2Ek5BwImGsGAfKY6ojXgsGtQGtgUZ7ck5c5oJ_hmfoFeS314azJZSIKIcXkTNyaLakvgNHZ5oFWwE2-kauC1LmWYtsiBD4XLjj_SDa0P5yezDp_834jhNzKZBWthl"
        transferData = TransferData(accessToken)

        source=input("Enter the files to be uploaded : ")
        destination = input("Enter the path where files to be uploaded")

        transferData.uploadFiles(source,destination)
        print("Files are uploaded !!!!!!!!!!!!")


main()
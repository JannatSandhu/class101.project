import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token= access_token

        def upload_file(self, file_from, file_to):
            dbx=dropbox.Dropbox(self.access_token)

            with open(file_from, 'rb') as f:
                dbx.files_upload(f.read(), file_to)

def main():
    access_token = '*****'
    transferData = TransferData(access_token)
            
    file_from = 'text.txt'
    file_to = 'text.txt'

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

    

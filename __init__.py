import logging
#import csv
import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# use static client to avoid resource exhaustion 
service_client = BlobServiceClient.from_connection_string(os.environ['AZURE_STORAGE_CONNECTION_STRING']) # create the service client from connection str in app settings
client = service_client.get_container_client("mycontainer") # get the client based on the blob container name

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    writeToBlob()
    csv_data = readBlob()

    # Convert json to filebytes in UTF-8
    filebytes = bytes(csv_data, 'utf-8')

    return func.HttpResponse(
        body=filebytes, # return the filebytes in the body of the response
        status_code=200, # set response status code to 200
        headers={'Content-Disposition': 'inline; filename="myfile.csv"'}, # add in the header to include specify the filename
        mimetype='application/octet-stream' # set the mimetype of the response to application/octet-stream, which will indicate it is a binary file.
    )


# Recommended: Write To blob
def writeToBlob():

    #create str to hold data
    csv_data = ""

    # create and set the data to write
    Document_Title = 'abc'
    Document_Generated='27/10/2021 1:16pm'
    Search_Date_Range = '21/10/2021 - 27/10/2021'
    Search_Location = 'def'
    Search_Radius='123'

    csv_data += 'Document_Title,{}\n'.format(Document_Title)
    csv_data += 'Document_Generated,{}\n'.format(Document_Generated)
    csv_data += 'Search_Date_Range,{}\n'.format(Search_Date_Range)
    csv_data += 'Search_Location,{}\n'.format(Search_Location)
    csv_data += 'DocumeSearch_Radiusnt_Title,{}\n'.format(Search_Radius)

    # note that we are overwriting the current blob
    client.upload_blob(name="myfile.csv", data=csv_data, overwrite=True)

# Recommended: Read blob
def readBlob() -> str:
 
    bc = client.get_blob_client(blob="output.csv") # get the blob based on the filename - can also do subfolders like folder/output.csv

    blob = bc.download_blob()
    blobContent = blob.readall().decode("utf-8")

    return blobContent

'''
    #####################################################################################################################################################################
    # Keep in mind that Azure has restrictions on writing to files on the host. It is recommended for a deployed function to use blob storage or other storage method   #
    # You can learn more about blob storage here: https://docs.microsoft.com/en-us/azure/storage/common/storage-samples-python#blob-samples                             #
    # The below is just an example of how to use the csv.writer and csv.reader                                                                                          #
    #####################################################################################################################################################################

# Not recommended to use CSV
def writeCsv():

     # open the csv file
    with open('HttpTrigger1\output.csv', mode='w', newline='') as cw:

        #create the writer
        csv_writer = csv.writer(cw, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)        

        # create and set the data to write
        Document_Title = 'abc'
        Document_Generated='27/10/2021 1:16pm'
        Search_Date_Range = '21/10/2021 - 27/10/2021'
        Search_Location = 'def'
        Search_Radius='123'

        # write the data to the csv using the csv_writer
        csv_writer.writerow(['Document_Title', str(Document_Title)])
        csv_writer.writerow(['Document_Generated', str(Document_Generated)])
        csv_writer.writerow(['Search_Date_Range', str(Search_Date_Range)])
        csv_writer.writerow(['Search_Location', str(Search_Location)])
        csv_writer.writerow(['Search_Radius', str(Search_Radius)])

# Not recommended to use CSV
def readCsv() -> str:

    # create str for use later
    csv_data = ""

    # open back up the file in read mode
    with open('HttpTrigger1\output.csv', mode='r', newline='') as cr:

        # create the reader
        csv_reader = csv.reader(cr, delimiter=',', quotechar='"')

        #read each row into a string
        for row in csv_reader:
            csv_data += ",".join(row) # join row values by delimiter
            csv_data += '\n' # need to add in a newline break  

    return csv_data
'''




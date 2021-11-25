import logging
import csv
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    csv_data = "" # create var to read the data into

    #####################################################################################################################################################################
    # Keep in mind that Azure has restrictions on writing to files on the host. It is recommended for a deployed function to use blob storage or other storage method   #
    # You can learn more about blob storage here: https://docs.microsoft.com/en-us/azure/storage/common/storage-samples-python#blob-samples                             #
    # The below is just an example of how to use the csv.writer                                                                                                         #
    #####################################################################################################################################################################
    
    # open the csv file
    with open('PathToFile\output.csv', mode='w', newline='') as cw:

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

    #End with to close the doc

    # open back up the file in read mode
    with open('PathToFile\output.csv', mode='r', newline='') as cr:
        
        # create the reader
        csv_reader = csv.reader(cr, delimiter=',', quotechar='"')

        #read each row into a string
        for row in csv_reader:
            csv_data += ",".join(row) # join row values by delimiter
            csv_data += '\n' # need to add in a newline break 

    # Convert json to filebytes in UTF-8
    filebytes = bytes(csv_data, 'utf-8')

    return func.HttpResponse(
        body=filebytes, # return the filebytes in the body of the response
        status_code=200, # set response status code to 200
        headers={'Content-Disposition': 'inline; filename="myfile.csv"'}, # add in the header to include specify the filename
        mimetype='application/octet-stream' # set the mimetype of the response to application/octet-stream, which will indicate it is a binary file.
    )





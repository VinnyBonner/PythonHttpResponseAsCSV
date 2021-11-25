import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Fake Json data as string
    json = "{'id': 9,'title': 'Infinix INBOOK','description': 'Infinix Inbook X1 Ci3 10th 8GB...','price': 1099,'discountPercentage': 11.83,'rating': 4.54,'stock': 96,'brand': 'Infinix','category': 'laptops','thumbnail': 'https://dummyjson.com/image/i/products/9/thumbnail.jpg','images': [  'https://dummyjson.com/image/i/products/9/1.jpg',  'https://dummyjson.com/image/i/products/9/2.png',  'https://dummyjson.com/image/i/products/9/3.png',  'https://dummyjson.com/image/i/products/9/4.jpg',  'https://dummyjson.com/image/i/products/9/thumbnail.jpg']}"

    # Convert json to filebytes in UTF-8
    filebytes = bytes(json, 'utf-8')

    return func.HttpResponse(
        body=filebytes, # return the filebytes in the body of the response
        status_code=200, # set response status code to 200
        headers={'Content-Disposition': 'inline; filename="myfile.csv"'}, # add in the header to include specify the filename
        mimetype='application/octet-stream' # set the mimetype of the response to application/octet-stream, which will indicate it is a binary file.
    )








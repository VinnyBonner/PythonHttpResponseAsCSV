import logging

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    csv = "{'id': 9,'title': 'Infinix INBOOK','description': 'Infinix Inbook X1 Ci3 10th 8GB...','price': 1099,'discountPercentage': 11.83,'rating': 4.54,'stock': 96,'brand': 'Infinix','category': 'laptops','thumbnail': 'https://dummyjson.com/image/i/products/9/thumbnail.jpg','images': [  'https://dummyjson.com/image/i/products/9/1.jpg',  'https://dummyjson.com/image/i/products/9/2.png',  'https://dummyjson.com/image/i/products/9/3.png',  'https://dummyjson.com/image/i/products/9/4.jpg',  'https://dummyjson.com/image/i/products/9/thumbnail.jpg']}"

    filebytes = bytes(csv, 'utf-8')

    return func.HttpResponse(body=filebytes, status_code=200, headers={'Content-Disposition': 'inline; filename="myfile.csv"'}, mimetype='application/octet-stream')

import requests

class TELHTTP:
    '''
    ## HTTP Requests
    ---
    This class provides utility functions for managing and sending http requests.

    **Note:** This class is a work in progress and subject to further development.
    '''

    def __init__(self):
        pass

    def get(self, url: str, params=None, headers=None) -> requests.Response:
        '''
        ## GET Request
        ---
        ### Description
        Make a GET request to the specified URL.\n
        ---
        ### Arguments
            - `url`: The URL to send the GET request to.
            - `params` (optional): Query parameters for the request.
            - `headers` (optional): Headers to include in the request.
        ---
        ### Return
            - The response object containing the response data.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the request or response handling.\n
        '''
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def post(self, url, data=None, json=None, headers=None) -> requests.Response:
        '''
        ## POST Request
        ---
        ### Description
        Make a POST request to the specified URL.\n
        ---
        ### Arguments
            - `url`: The URL to send the POST request to.
            - `data` (optional): Data to include in the request.
            - `json` (optional): JSON data to include in the request.
            - `headers` (optional): Headers to include in the request.\n
        ---
        ### Return
            - The response object containing the response data.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the request or response handling.\n
        '''
        try:
            response = requests.post(url, data=data, json=json, headers=headers)
            return response
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def put(self, url, data=None, json=None, headers=None):
        '''
        ## PUT Request
        ---
        ### Description
        Make a PUT request to the specified URL.\n
        ---
        ### Arguments
            - `url`: The URL to send the PUT request to.
            - `data` (optional): Data to include in the request.
            - `json` (optional): JSON data to include in the request.
            - `headers` (optional): Headers to include in the request.\n
        ---
        ### Return
            - The response object containing the response data.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the request or response handling.\n
        '''
        try:
            response = requests.put(url, data=data, json=json, headers=headers)
            return response
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def delete(self, url, headers=None):
        '''
        ## DELETE Request
        ---
        ### Description
        Make a DELETE request to the specified URL.\n
        ---
        ### Arguments
            - `url`: The URL to send the DELETE request to.
            - `headers` (optional): Headers to include in the request.\n
        ---
        ### Return
            - The response object containing the response data.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the request or response handling.\n
        '''
        try:
            response = requests.delete(url, headers=headers)
            return response
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

    def download_file(self, url, local_path):
        '''
        ## Download File
        ---
        ### Description
        Download a file from the specified URL and save it to the local path.\n
        ---
        ### Arguments
            - `url`: The URL of the file to download.
            - `local_path`: The local path to save the downloaded file.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the request or file writing.\n
        '''
        try:
            response = requests.get(url, stream=True)
            with open(local_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")
    
    def status(self, code: int, long_desc: bool = False):
        '''
        ## HTTP Status Description
        ---
        ### Description
        Get the description of an HTTP status code.\n
        ---
        ### Arguments
            - `code`: The HTTP status code to get the description for.
            - `long_desc` (optional): If True, return the detailed description.\n
        ---
        ### Return
            - The description of the provided status code. If long_desc is True, returns the detailed description.\n
        ---
        ### Exceptions
            - `Exception`: If an error occurs during the status code lookup.\n
        '''
        short_codes = {
            100: "Continue",
            101: "Switching Protocols",
            200: "OK",
            201: "Created",
            202: "Accepted",
            204: "No Content",
            300: "Multiple Choices",
            301: "Moved Permanently",
            302: "Found",
            304: "Not Modified",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
        }

        long_codes = {
            100: "Continue - The initial part of a request has been received, and the server has acknowledged that it will continue to process the request.",
            101: "Switching Protocols - The server acknowledges that it will switch to the protocol specified in the Upgrade header field during the connection setup.",
            200: "OK - The request has succeeded. The meaning of the success depends on the HTTP method used.",
            201: "Created - The request has been fulfilled, and a new resource has been created.",
            202: "Accepted - The request has been accepted for processing, but the processing has not been completed yet.",
            204: "No Content - The server has successfully processed the request, but there is no representation to send in the response.",
            300: "Multiple Choices - The requested resource has multiple representations. The server cannot choose which one to return.",
            301: "Moved Permanently - The requested resource has been permanently moved to a new location.",
            302: "Found - The requested resource has been temporarily moved to a different location.",
            304: "Not Modified - The client's cached version of the requested resource is still valid.",
            400: "Bad Request - The server cannot or will not process the request due to a client error.",
            401: "Unauthorized - The client must authenticate itself to get the requested response.",
            403: "Forbidden - The client does not have permission to access the requested resource.",
            404: "Not Found - The server cannot find the requested resource.",
            405: "Method Not Allowed - The method specified in the request is not allowed for the resource identified by the request.",
            500: "Internal Server Error - The server has encountered a situation it doesn't know how to handle.",
            501: "Not Implemented - The server does not support the functionality required to fulfill the request.",
            502: "Bad Gateway - The server, while acting as a gateway or proxy, received an invalid response from an inbound server it accessed.",
            503: "Service Unavailable - The server is currently unable to handle the request due to temporary overloading or maintenance of the server.",
        }
        try:
            return short_codes.get(code, "Unknown") if not long_desc else long_codes.get(code, "Unknown")
        except Exception as e:
            raise Exception(f"Something whent wrong: {e}")

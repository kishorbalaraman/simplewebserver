## EX01 Developing a Simple Webserver
## Date:05.10.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Table</title>
    </head>
    <body>
        <h1 align="center" style="color: rgb(56, 76, 76);">Device specification:25017562</h1>
        <table border="5"  cellspacing="10" cellpadding="30" align="center">
            <tr>
                <th>S.NO:</th>
                <th>Device specification</th>
                <th>Details</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Storage</td>
                <td>512gb</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Proccesor</td>
                <td>Intel-5</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Graphics</td>
                <td>Intel UHD</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Ram</td>
                <td>16GB</td>
            </tr>
            <tr>
                <td>5</td>
                <td>OS</td>
                <td>Windows11</td>
            </tr>
        </table>

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
<img width="1920" height="1080" alt="Screenshot 2025-10-15 134522" src="https://github.com/user-attachments/assets/de8e599b-4388-41d1-9d75-4332bb639b71" />


## RESULT:
The program for implementing simple webserver is executed successfully.

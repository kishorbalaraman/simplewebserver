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
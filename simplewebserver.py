from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>LAPTOP STORE</title>
    </head>
    <center>
    <h3>N.Durgasri</h3>
    <h3>(26019019)</h3>
    <body style="color : white" bgcolor="black">
        <table border="1">
            <tr>
                <th>1</th>
                <th>Device name</th>
                <th>TL15-53M-G2</th>
            </tr>
            <tr>
                <th>2</th>
                <th>Processor</th>
                <th>(Intel(R) Core(TM) 5 210H (2.20 GHz))</th>
            </tr>
            <tr>
                <th>3</th>
                <th>Installed RAM</th>
                <th>16.0 GB (16.0 GB (15.7 GB usable))</th>
            </tr>
            <tr>
                <th>4</th>
                <th>Graphics card</th>
                <th>Intel(R) Graphics (128 MB)</th>
            </tr>
            <tr>
                <th>5</th>
                <th>Storage</th>
                <th>115 GB of 477 GB used</th>
            </tr>
            <tr>
                <th>6</th>
                <th>Device ID</th>
                <th>E2BCF409-EAA0-4F20-ACC0-E9D432D9CA2E</th>
            </tr>
            <tr>
                <th>7</th>
                <th>Product ID</th>
                <th>00342-42945-51974-AAOEM</th>
            </tr>
            <tr>
                <th>8</th>
                <th>System type</th>
                <th>64-bit operating system, x64-based processor</th>
            </tr>
            <tr>
                <th>9</th>
                <th>Pen and touch</th>
                <th>No pen or touch input is available for this display</th>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()
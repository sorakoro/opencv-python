from http.server import HTTPServer, BaseHTTPRequestHandler
import cv2

camera = cv2.VideoCapture(0)

class liveHTTPServer_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("path=",self.path)
        if self.path[0:7] == "/camera":
            self.send_response(200)
            self.send_header('Cotent-Type', 'image/jpeg')
            self.end_headers()

            _, frame = camera.read()
            img = cv2.resize(frame, (300,200))
            param = [int(cv2.IMWRITE_JPEG_QUALITY), 80]
            _, encimg = cv2.imencode('.jpg', img, param)
            self.wfile.write(encimg)

        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            try:
                f = open('live2.html', 'r', encoding='utf-8')
                s = f.read()
            except:
                s = "file not found"
            self.wfile.write(s.encode('utf-8'))

        else:
            self.send_response(404)
            self.wfile.write("file not found".encode('utf-8'))

try:
    addr = ('', 8081)
    httpd = HTTPServer(addr, liveHTTPServer_Handler)
    print('サーバーを開始', addr)
    httpd.serve_forever()

except KeyboardInterrupt:
    httpd.socket.close()



from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi
from urllib.parse import parse_qs

query_list = []


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/query'):
            content_len = int(self.headers.get('Content-Length'))
            post_body = (self.rfile.read(content_len)).decode("utf-8")
            counter = 0
            for query in query_list:
                if(query == post_body):
                    counter = counter + 1

            print(counter)

            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(str(counter),"utf-8"))


    def do_POST(self):
        if self.path.endswith('/input'):
            self.send_response(200)
            self.send_header("content-type","text/xml")
            self.end_headers()
            content_len = int(self.headers.get('Content-Length'))
            post_body = (self.rfile.read(content_len)).decode("utf-8")
            print("body : ",post_body)
            query_list.append(post_body)



def main():
    PORT = 9000
    server_adress = ('localhost',PORT)
    server = HTTPServer(server_adress,requestHandler)
    print('[STARTING] Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
     main()

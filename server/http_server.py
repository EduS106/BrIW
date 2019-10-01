import source.db_extraction as db_extraction
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class DrinkHandler(BaseHTTPRequestHandler):
    pass


class RoundHandler(BaseHTTPRequestHandler):
    pass


class PersonHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        people = db_extraction.get_table("person")

        jd = json.dumps(people)
        self.wfile.write(jd.encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(content_length))
        db_extraction.add_data("person", "name", [data["name"]])

        self.send_response(201)
        self.end_headers()


if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, PersonHandler)
    print("Starting server")

    httpd.serve_forever()

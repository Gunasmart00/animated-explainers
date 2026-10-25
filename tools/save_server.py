import http.server
import urllib.parse
import os
import sys

PORT = 8765

class SaveHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)
        filename = qs.get('name', ['image.png'])[0]

        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length)

        out_path = os.path.join(r'episodes\jupiter-crash\images', filename)
        with open(out_path, 'wb') as f:
            f.write(data)

        print(f"[SAVE_SERVER] Saved {out_path} ({len(data)} bytes)")
        sys.stdout.flush()

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = http.server.HTTPServer(('127.0.0.1', PORT), SaveHandler)
    print(f"[SAVE_SERVER] Listening on http://127.0.0.1:{PORT}")
    sys.stdout.flush()
    server.serve_forever()

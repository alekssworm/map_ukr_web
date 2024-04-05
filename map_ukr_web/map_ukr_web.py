import http.server
import socketserver
import webbrowser


PORT = 8000  # ����, �� ������� ����� ������� ���-������

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("", PORT)
    webbrowser.open_new_tab(f"http://localhost:{PORT}/index.html")
    httpd.serve_forever()


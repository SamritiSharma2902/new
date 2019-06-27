from app import app
@app.route('/')
@app.route('/index')
def index():
    return'''
    <html>
     <head><title>Home</title></head>
      <body>hello everyone</body>
    </html>'''

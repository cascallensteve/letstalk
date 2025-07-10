from whisperlink_backend.wsgi import application

# Vercel expects the WSGI application to be named 'app'
app = application

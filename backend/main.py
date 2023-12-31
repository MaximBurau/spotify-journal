from app import app, db 
from app.models import Album, Track, Note

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Album': Album, 'Track': Track, 'Note': Note}
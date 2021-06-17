from app import create_app, db
from db_manager import Db_Build, Db_Destroy

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'app': create_app, 'db': db, 'db_init': Db_Build.db_init_all, 'db_destroy': Db_Destroy.db_destroy }

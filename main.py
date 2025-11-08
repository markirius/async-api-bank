import uvicorn
from alembic import command
from alembic.config import Config
import pathlib

def run_migrations():
    """
    Carrega o arquivo alembic.ini e aplica todas as migrations
    (equivalente a `alembic upgrade head`).
    """
    cfg_path = pathlib.Path(__file__).with_name("alembic.ini")

    cfg = Config(str(cfg_path))
    cfg.set_main_option(
            "script_location",
            str(pathlib.Path(__file__).parent / "migrations")
        )

    command.upgrade(cfg, "head")

if __name__ == "__main__":
    run_migrations()
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_path: str) -> None:
    global __factory

    if __factory:
        return

    if not db_path or not db_path.strip():
        raise Exception("Необходимо указать файл базы данных.")

    connection = f"sqlite:///{db_path.strip()}?check_same_thread=False"
    print(f"Подключение к базе данных по адресу {connection}")

    engine = sa.create_engine(connection, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()

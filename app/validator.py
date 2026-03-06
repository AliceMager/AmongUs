from app.models.deployment import Deployment
from app.exceptions import UsernameError, DataBaseNameErr

def validate_deployment(deployment: Deployment):
    db_startswith_user_check(deployment.db_name)
    db_user_number_check(deployment.db_name)
    username_len_check(deployment.username)


def db_startswith_user_check(db_name: str):
    if not db_name.startswith('user'):
        raise DataBaseNameErr

def db_user_number_check(db_name: str):
    _, _, res = db_name.partition('user')
    if len(res) > 1:
        if not res[1].isdigit():
            raise DataBaseNameErr
    else:
        raise DataBaseNameErr


def username_len_check(username: str):
    if len(username) < 3:
        raise UsernameError
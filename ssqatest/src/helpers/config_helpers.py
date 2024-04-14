

import os




def get_base_url():
    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        # return 'http://demostore.supersqa.com'
        return 'http://localhost:8888/quicksite/'
    elif env.lower() == 'prod':
        return 'http://demostore.prod.supersqa.com'
    else:
        raise Exception(f"Unknown environment: {env}")


def get_database_credentials():

    env = os.environ.get('ENV', 'test')

    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")
    if not db_user or not db_password:
        raise Exception("Environemnt variavles 'DB_USER'  and 'DB_PASSWORD' must be set.")

    if env == 'test':
        db_host = '127.0.0.1'
        db_port = 3306

    elif env == 'prod':
        db_host = 'demostore.supersqa.com'
        db_port = 3306
    else:
        raise Exception(f"Unknown environment: {env}")

    db_info = {"db_host": db_host, "db_port": db_port,
               "db_user": db_user, "db_password": db_password}

    return db_info










#
# def get_base_url():
#
#     env = os.environ.get('ENV', 'test')
#
#     if env.lower() == 'test':
#         # return 'http://demostore.supersqa.com'
#         # return 'http://127.0.0.1:8888/localdemostore/'
#         return 'http://localhost:8888/localdemostore/'
#     elif env.lower() == 'prod':
#         return 'http://demostore.prod.supersqa.com'
#     else:
#         raise Exception(f"Unknown environment: {env}")
#
# def get_database_credentials():
#
#     env = os.environ.get('ENV', 'test')
#
#     db_user = os.environ.get("DB_USER")
#     db_password = os.environ.get("DB_PASSWORD")
#     if not db_user or not db_password:
#         raise Exception("Environment variables 'DB_USER' and 'DB_PASSWORD' must be set.")
#
#     if env == 'test':
#         db_host = '127.0.0.1'
#         db_port = 8889
#     elif env == 'prod':
#         db_host = 'demostore.supersqa.com'
#         db_port = 3306
#     else:
#         raise Exception(f"Unknown environment: {env}")
#
#     db_info = {"db_host": db_host, "db_port": db_port,
#                "db_user": db_user, "db_password": db_password}
#
#     return db_info
#
#
# def get_api_credentials():
#
#     base_url = get_base_url()
#     api_key = os.environ.get("API_KEY")
#     api_secret = os.environ.get("API_SECRET")
#     if not all([api_key, api_secret]):
#         raise Exception("Both 'API_KEY' and 'API_SECRET' must be set as environment variable.")
#
#     return {'base_url': base_url, 'api_key': api_key, 'api_secret': api_secret}

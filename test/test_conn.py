import psycopg2
import configparser

Config = configparser.ConfigParser()
Config.read("config.ini")

def postgres_test():

    DB_ST = "dbname={} user={} host={} password={} connect_timeout=1 ".format(
                Config['POSTGRES']['DBNAME'],
                Config['POSTGRES']['NAME'],
                Config['POSTGRES']['HOST'],
                Config['POSTGRES']['PASSWORD']
                                )

    try:
        print(DB_ST)
        conn = psycopg2.connect(DB_ST)
        conn.close()
        return ("connection successful")
    except Exception as e:
        return "Error:", e
    
print(postgres_test())
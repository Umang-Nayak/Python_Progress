import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="kingun39",
    port=5432,
    database="UMA"
)

mc = mydb.cursor()


sql = "INSERT INTO teacher (t_id) VALUES (%s)"
val = [
        (1,),
        (2,),
        (3,)
]

mc.executemany(sql, val)
mydb.commit()

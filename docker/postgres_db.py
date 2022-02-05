import psycopg2

conn = psycopg2.connect(
    database='test_database',
    user='kirill',
    password='password',
    host='127.0.0.1',
    port='5432'
)
cur = conn.cursor()

try:
    cur.execute(
        'CREATE TABLE test (student_id INTEGER PRIMARY KEY);'
    )
except:
    print('Table already exist')
conn.commit()
try:
    cur.execute(
        'ALTER TABLE test ADD COLUMN student_name VARCHAR'
    )
except:
    print('Column already exist')
conn.commit()
try:
    cur.execute(
        "INSERT INTO test (student_id, student_name) VALUES (%s, %s)", (3, 'Kirill')
    )
except:
    print('Already inserted')
conn.commit()
try:
    cur.execute(
        'UPDATE test SET student_name = %s WHERE student_id = %s', ('Kostya', 3)
    )
except:
    print('Already changed')
conn.commit()
try:
    cur.execute(
        """CREATE TABLE test_grade (
            id INTEGER PRIMARY KEY,
            student_grade INT)
    """
    )
except:
    print('created new table')
conn.commit()
try:
    cur.execute(
        """CREATE TABLE many_to_many_table (
                test_id INT,
                test_2_id INT,
                PRIMARY KEY (test_id, test_2_id),
                CONSTRAINT fk_test_id FOREIGN KEY (test_id) REFERENCES test (student_id),
                CONSTRAINT fk_test_id_2 FOREIGN KEY (test_2_id) REFERENCES test_grade (id)
                )
        """
    )
except:
    print('created many to many table')
conn.commit()
try:
    cur.execute(
        """WITH first_insert as (INSERT INTO test (student_id, student_name) VALUES (4, 'George') RETURNING student_id),
           second_insert as (INSERT INTO test_grade (id, student_grade) VALUES (5, 10) RETURNING id)
           INSERT INTO many_to_many_table (test_id, test_2_id) SELECT first_insert.student_id, second_insert.id FROM first_insert, second_insert
        """
    )
except:
    print("all inserted")
conn.commit()
cur.close()
conn.close()

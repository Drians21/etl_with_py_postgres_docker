import pandas as pd
from sqlalchemy import create_engine
from faker import Faker
from datetime import datetime
import pytz

user = 'postgres'
password = 'postgres'
hostname = 'postgres-db'
database = 'etl'
port = '5432'
conn_string = f'postgresql://{user}:{password}@{hostname}:{port}/{database}'
engine = create_engine(conn_string)
conn = engine.connect()

jakarta_timezone = pytz.timezone('Asia/Jakarta')

fake = Faker()
data = []
for _ in range(2000):
    nama = fake.name()
    alamat = fake.address()
    tanggal_lahir = fake.date_of_birth()
    email = fake.email()
    nomor_telepon = fake.phone_number()
    created_at = datetime.now(jakarta_timezone)

    data.append([nama, alamat, tanggal_lahir, email, nomor_telepon, created_at])

df = pd.DataFrame(data, columns=['Nama', 'Alamat', 'Tanggal_Lahir', 'Email', 'Nomor_Telepon', 'created_at'])
df.to_sql("data", engine, if_exists='replace', index=False)


# load to another database table
query = \
"""
    SELECT
        "Nama",
        "Alamat",
        "Tanggal_Lahir",
        "Email",
        "created_at"
    FROM data
 """
df_read = pd.read_sql(query, engine)
df_read = df_read.rename(columns={ # rename columns
                "Nama":"nama",
                "Alamat":"alamat",
                "Tanggal_Lahir":"tanggal_lahir",
                "Email":"email"
            })
# formatting data type
df_read['tanggal_lahir'] = pd.to_datetime(df_read['tanggal_lahir'])
df_read['created_at'] = pd.to_datetime(df_read['created_at'])
df_read.to_sql("data_dummy_2", engine, if_exists='replace', index=False)
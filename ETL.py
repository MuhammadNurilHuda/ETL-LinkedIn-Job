import pandas as pd
import os

def extract(data):
    df = pd.read_csv(data)
    return transform(df)

def transform(df):
    columns = ['Company Name', 'Job Title', 'Location', 'Company Domain', 'Posted On', 'Tech Stack']
    df = df.drop_duplicates(subset=['Job LinkedIn URL']) # menghapus duplikat
    df = df[columns] # Menentukan kolom yang digunakan
    df = df.dropna(subset=["Tech Stack"]) # Menghapus null value
    df['Posted On'] = pd.to_datetime(df['Posted On'], format='ISO8601') # Mengganti tipe data untuk kolom 'Posted On'
    df['Tech Stack'] = df['Tech Stack'].str.split(', ') # Explode data
    df = df.explode('Tech Stack')
    return load(df)

def load(df):
    dir = os.getcwd()
    path = os.path.join(dir, 'cleaned_joblist.csv')
    df.to_csv(path, index=False)
    print("File telah disimpan di direktori saat ini.")

if __name__ =="__main__":
    data = input("Masukkan nama file: ")
    extract(str(data))
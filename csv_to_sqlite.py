import sqlite3
import pandas as pd

#this file loads the csv files into the database using pandas

def main():
    conn = sqlite3.connect("login_info.db")
    cur = conn.cursor()
    load_file("info", conn, cur)


def load_file(name, conn, cur):
    df = pd.read_csv(name +".csv")
    header_list = df.columns.values.tolist()

    first_line = "'" + header_list[0] + "'"
    for num in range(len(header_list)-1):
        first_line += (",'" + header_list[num+1] + "'")
    
    cur.execute("DROP TABLE IF EXISTS "+ name + ";")
    cur.execute('''CREATE TABLE '''+ name + ''' (''' + first_line + ''')''')
    
    df.to_sql(name, conn, if_exists='replace', index = True, index_label = 'number')
    
    conn.commit()

main()
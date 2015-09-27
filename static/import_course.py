import pandas as pd
import sqlite3 as sql
import re

TAG_ID = "Class Nbr"
TAG_school = "Acad Group"
TAG_dept = "Subject"
TAG_catlog = "Catalog Nbr"
TAG_title = "Course Title"
TAG_section = "Section"
TAG_component = "Component"
TAG_location = "Location"
TAG_instructor = "Instructor"
TAG_term = "Term"

dat = pd.read_csv('FA2015.csv')
print 'Num records read in', dat.shape[0]

records = []
pattern = re.compile(r'\((.*)\)')
for idx, row in dat.iterrows():
  cid = idx
  class_nbr = row[TAG_ID]
  school = row[TAG_school]
  dept = row[TAG_dept]
  dept_abbrv = re.search(pattern, dept).group(1)
  catlog = row[TAG_catlog]
  title = row[TAG_title]
  section = row[TAG_section]
  component = row[TAG_component]
  location = row[TAG_location]
  instructor = row[TAG_instructor]
  term = row[TAG_term]

  # create a tuple
  record = (cid, class_nbr, school, dept, dept_abbrv, catlog, title, section, component, location, instructor, term)
  records.append(record)

  if (idx % 100) == 0:
    print 'Records parsed', idx

# insert data into DB
conn = sql.connect('class.db')
# drop existing table



# for each row, insert a record into the DB
c = conn.cursor()
sql_str = "INSERT INTO courses VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
c.executemany(sql_str, records)
conn.commit()
conn.close()


  


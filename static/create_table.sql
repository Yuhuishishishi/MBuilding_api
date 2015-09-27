CREATE TABLE courses (
  id INTEGER PRIMARY KEY NOT NULL,
  class_nbr INTEGER NOT NULL,
  school NVARCHAR(250),
  dept NVARCHAR(250),
  dept_abbrv NVARCHAR(250),
  catlog_nbr NVARCHAR(250),
  title NVARCHAR(250),
  section INTEGER,
  component NVARCHAR(250),
  location NVARCHAR(250),
  instructor NVARCHAR(250),
  term NVARCHAR(250) NOT NULL
);
  

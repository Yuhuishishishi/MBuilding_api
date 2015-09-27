__author__ = 'yuhui'


class Course:
    TAG = {}
    TAG['id'] = 'id'
    TAG['class_nbr'] = 'class_nbr'
    TAG['school'] = 'school'
    TAG['dept'] = 'dept'
    TAG['dept_abbrv'] = 'dept_abbrv'
    TAG['catlog_nbr'] = 'catlog_nbr'
    TAG['title'] = 'title'
    TAG['section'] = 'section'
    TAG['component'] = 'component'
    TAG['location'] = 'location'
    TAG['instructor'] = 'instructor'
    TAG['term'] = 'term'

    def __init__(self, row):
        self.id = row[Course.TAG['id']]
        self.class_nbr = row[Course.TAG['class_nbr']]
        self.school = row[Course.TAG['school']]
        self.dept = row[Course.TAG['dept']]
        self.dept_abbrv = row[Course.TAG['dept_abbrv']]
        self.catlog_nbr = row[Course.TAG['catlog_nbr']]
        self.title = row[Course.TAG['title']]
        self.section = row[Course.TAG['section']]
        self.component = row[Course.TAG['component']]
        self.location = row[Course.TAG['location']]
        self.instructor = row[Course.TAG['instructor']]
        self.term = row[Course.TAG['term']]

    def serialize(self):
        return {
            Course.TAG['id'] : self.id,
            Course.TAG['class_nbr'] : self.class_nbr,
            Course.TAG['school'] : self.school,
            Course.TAG['dept'] : self.dept,
            Course.TAG['dept_abbrv'] : self.dept_abbrv,
            Course.TAG['catlog_nbr'] : self.catlog_nbr,
            Course.TAG['title'] : self.title,
            Course.TAG['section'] : self.section,
            Course.TAG['component'] : self.component,
            Course.TAG['location'] : self.location,
            Course.TAG['instructor'] : self.instructor,
            Course.TAG['term'] : self.term
        }

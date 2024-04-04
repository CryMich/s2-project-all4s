from App.database import db
from .student import Student
from .staff import Staff

class Accomplishment(db.Model):
      __tablename__ = "accomplishment"
      id = db.Column(db.Integer, primary_key=True)
      verified = db.Column(db.Boolean, nullable=False)
      topic = db.Column(db.String(400), nullable=False)
      taggedStaffId = db.Column(db.String(10), db.ForeignKey('staff.ID'))
      createdByStudentID = db.Column(db.String(10), db.ForeignKey('student.ID'))
      studentName = db.Column(db.String(40), nullable=False)
      details = db.Column(db.String(400), nullable=False)
      points = db.Column(db.Float, nullable=False, default=0.0)
      status = db.Column(db.String(40), nullable=False)

      def __init__(self,student ,verified, taggedStaffId, topic, details, points,status):
        self.createdByStudentID = student.ID
        self.studentName= f"{student.firstname} {student.lastname}"
        self.verified = verified
        self.topic = topic
        self.taggedStaffId = taggedStaffId
        self.details = details
        self.points = points
        self.status = status

      def to_json(self):
        return {"id": self.id,
            "studentID": self.createdByStudentID,
            "verified": self.verified,
            "taggedStaffId": self.taggedStaffId,
            "topic":self.topic,
            "name":self.studentName,
            "points": self.points,
            "details": self.details,
            "status": self.status}
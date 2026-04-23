# pip install sqlalchemy

from sqlalchemy import create_engine, String, Boolean, ForeignKey

from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
    Mapped,
    mapped_column,
    relationship,
)


from config import URL

engine = create_engine(URL, echo=False)

Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    def create_db(self):
        Base.metadata.create_all(engine)

    def drop_db(self):
        Base.metadata.drop_all(engine)


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    university: Mapped[str] = mapped_column(String(100))
    specialty: Mapped[str] = mapped_column(String(100))
    group: Mapped[str] = mapped_column(String(100))
    exams: Mapped[list["ExamResult"]] = relationship(
        "ExamResult", back_populates="student"
    )


class ExamResult(Base):
    __tablename__ = "exam_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    subject: Mapped[str] = mapped_column(String(100))
    grade: Mapped[int] = mapped_column()
    passing_grade: Mapped[int] = mapped_column()
    passed: Mapped[bool] = mapped_column(Boolean)
    student: Mapped["Student"] = relationship("Student", back_populates="exams")



base = Base()
base.create_db()
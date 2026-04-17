"""
ALTER TABLE enrollments
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE enrollments
ADD CONSTRAINT fk_course
FOREIGN KEY (course_id) REFERENCES courses(id);
"""
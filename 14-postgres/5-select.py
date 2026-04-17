"""
SELECT u.name, c.title
FROM users u
JOIN enrollments e ON u.id = e.user_id
JOIN courses c ON c.id = e.course_id;
"""
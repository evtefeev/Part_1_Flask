-- Active: 1776353800541@@dpg-d7gd4fho3t8c73c6167g-a.oregon-postgres.render.com@5432@nikita

SELECT u.name, c.title
FROM users u
JOIN enrollments e ON u.id = e.user_id
JOIN courses c ON c.id = e.course_id;

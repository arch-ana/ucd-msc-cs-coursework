SELECT courses.coursename
FROM students, courses
WHERE students.takingcourse = courses.coursecode and lastname = "Murphy"
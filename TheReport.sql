SELECT 
CASE
  WHEN Grade >= 8 THEN Name
  ELSE NULL
END AS Name, Grade, Marks 
FROM Students INNER JOIN Grades 
ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark 
ORDER BY Grade DESC, Name ASC, Marks ASC;
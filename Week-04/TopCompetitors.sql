SELECT c.hacker_id, d.name
FROM Difficulty a JOIN Challenges b ON a.difficulty_level = b. difficulty_level
                                                        JOIN Submissions  c ON c.challenge_id = b.challenge_id 
                                                        JOIN Hackers  d ON d.hacker_id  = c.hacker_id 
WHERE c.score = a.score
GROUP BY c.hacker_id, d.name
HAVING COUNT(c.challenge_id) > 1
ORDER BY COUNT(c.challenge_id) DESC, c.hacker_id ASC;
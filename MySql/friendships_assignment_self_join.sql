SELECT * FROM friendships_assignment.users;

/*INSERT INTO friendships_assignment.users (first_name, last_name, created_at, updated_at)
VALUES 
	('Chris', 'Baker', now(), now()) ,
   ('Diana', 'Smith', now(), now()),
   ('James', 'Johnson', now(), now()),
   ('Jessica', 'Davidson', now(), now()); */
   
-- DELETE FROM friendships_assignment.users WHERE id in (5,6,7,8);


/*INSERT INTO friendships_assignment.friendships (users_id, friend_id, created_at, updated_at)
VALUES 
	(1, 4, now(), now()),
	(1, 3, now(), now()),
    (1, 2, now(), now()),
	(2, 1, now(), now()),
	(3, 1, now(), now()),
    (4, 1, now(), now()); */
    
SELECT 	users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name
FROM		users
JOIN		friendships
ON			users.id = friendships.users_id
JOIN		users AS users2
ON			friendships.friend_id = users2.id;




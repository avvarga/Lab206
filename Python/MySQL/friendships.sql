INSERT users (first_name, last_name, created_at, updated_at) VALUES ('Jessica', 'Davidson', NOW(), NOW());
INSERT friendships (user_id, friend_id, created_at, updated_at) VALUES (4,1, NOW(), NOW());

SELECT users.id, users.first_name, users.last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name 
FROM users 
	LEFT JOIN friendships ON users.id=friendships.user_id 
	LEFT JOIN users as user2 ON friendships.friend_id = user2.id
    ORDER BY users.id ASC;
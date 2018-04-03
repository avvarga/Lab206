SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
FROM city
	JOIN address ON city.city_id = address.city_id
    JOIN customer ON customer.address_id = address.address_id
    WHERE city.city_id = 312;
    
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre
FROM film
	JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id
    WHERE category.name = 'Comedy';
    
SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year
FROM actor
	JOIN film_actor ON actor.actor_id = film_actor.actor_id
    JOIN film ON film.film_id = film_actor.film_id
    WHERE actor.actor_id = 5;
    
SELECT store.store_id, address.city_id, customer.first_name, customer.last_name, customer.email, address.address
FROM customer
	JOIN address ON address.address_id = customer.address_id
    JOIN store ON customer.store_id = store.store_id
    WHERE store.store_id = 1 and address.city_id= 1 or store.store_id = 1 and address.city_id= 4 or store.store_id = 1 and address.city_id= 42 or store.store_id = 1 and address.city_id= 459;
    
SELECT film.title,film.description,film.release_year,film.rating,film.special_features 
FROM film
    JOIN film_actor ON film_actor.film_id=film.film_id
	WHERE rating='G' AND actor_id=15 AND special_features LIKE "%B%es%";
    
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name,' ',actor.last_name) AS actor_name, actor.last_update
FROM film
	JOIN film_actor ON film.film_id = film_actor.film_id
    JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE film.film_id = 369;
    
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
FROM film
	JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id
    WHERE category.name = "Drama" AND film.rental_rate = 2.99;
    
SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) as actor_name, film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
	JOIN film_category ON film.film_id = film_category.film_id
    JOIN category ON film_category.category_id = category.category_id
    JOIN film_actor ON film.film_id = film_actor.film_id
    JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE category.name = "Action" AND CONCAT(actor.first_name, ' ', actor.last_name) = "SANDRA KILMER";

-- Query 1
SELECT 	countries.name, 
				languages.language, 
                languages.percentage
FROM 	countries
JOIN 		languages
ON 			countries.id = languages.country_id
WHERE 		languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- Query 2
SELECT		countries.name, 
					COUNT(cities.id) as cities_count
FROM 		countries
JOIN 			cities
ON 				countries.id = cities.country_id
GROUP BY countries.id
ORDER BY COUNT(cities.id) DESC;
				
-- Query 3
SELECT  cities.name,
				cities.population
FROM 	cities
JOIN		countries
ON			cities.country_id = countries.id
WHERE countries.name = 'Mexico'
AND cities.population > 500000
ORDER BY cities.population DESC;

-- Query 4
SELECT	countries.name, 
				languages.language, 
                languages.percentage
FROM 	countries
JOIN 		languages
ON 			countries.id = languages.country_id
WHERE 		languages.percentage >  89
ORDER BY  languages.percentage DESC;

-- Query 5
SELECT 	countries.name
FROM 	countries
WHERE	countries.population > 100000 
AND		countries.surface_area < 501;

-- Query 6
SELECT 	countries.name
FROM 	countries
WHERE	countries.government_form = 'constitutional monarchy' 
AND		countries.capital > 200
AND		countries.life_expectancy > 75;	

-- Query 7
SELECT	countries.name,
				cities.name,
                cities.district,
				cities.population
FROM		countries
JOIN		cities
ON			countries.id = cities.country_id
WHERE	countries.name = 'Argentina'
AND		cities.district = 'Buenos Aires'
AND		cities.population > 500000;


-- Query 8
SELECT	countries.region,
				COUNT(countries.id) as country_count
FROM 	countries
GROUP BY	countries.region
ORDER BY COUNT(countries.id) DESC;






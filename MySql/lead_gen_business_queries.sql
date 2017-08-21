
-- Query 1. What query would you run to get the total revenue for March of 2012?
SELECT	SUM(billing.amount) as march_2012_revenue
FROM		billing
WHERE	billing.charged_datetime between '2012-03-01' AND '2012-03-31';


-- Query 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT	SUM(billing.amount) as client_10_revenue
FROM		billing
JOIN		clients
ON			billing.client_id = clients.client_id
WHERE	clients.client_id = 10 ;

-- Query 3. What query would you run to get all the sites that client=10 owns?
SELECT	sites.domain_name,
				clients.first_name,
                clients.last_name
FROM		sites
JOIN		clients
ON			sites.client_id = clients.client_id
WHERE	clients.client_id = 10 ;

-- Query 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT 	COUNT(sites.site_id) as monthly_site_creation_count,
				MONTH(sites.created_datetime) AS month_created,
                YEAR(sites.created_datetime) AS year_created
FROM		sites
JOIN 		clients
ON			sites.client_id = clients.client_id
-- WHERE	clients.client_id = 1
WHERE	clients.client_id = 20
GROUP BY YEAR(sites.created_datetime), MONTH(sites.created_datetime)
ORDER BY YEAR(sites.created_datetime), MONTH(sites.created_datetime);

-- Query 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT	COUNT(leads.leads_id),
				sites.domain_name,
                leads.registered_datetime
FROM		leads
JOIN		sites
ON			leads.site_id = sites.site_id
WHERE	leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.domain_name;

-- Query 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				COUNT(leads.leads_id)
FROM		leads
JOIN		sites
ON			leads.site_id = sites.site_id
JOIN 		clients
ON			sites.client_id = clients.client_id
WHERE	leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY CONCAT(clients.first_name, " " , clients.last_name);	

-- Query 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				COUNT(leads.leads_id)
FROM		leads
JOIN		sites
ON			leads.site_id = sites.site_id
JOIN 		clients
ON			sites.client_id = clients.client_id
WHERE	MONTH(leads.registered_datetime) BETWEEN 1 AND 6
AND		YEAR(leads.registered_datetime) = 2011
GROUP BY YEAR(leads.registered_datetime), MONTH(leads.registered_datetime), CONCAT(clients.first_name, " " , clients.last_name);	

-- Query 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.
SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				sites.domain_name,
				COUNT(leads.leads_id)
FROM		leads
JOIN		sites
ON			leads.site_id = sites.site_id
JOIN 		clients
ON			sites.client_id = clients.client_id
WHERE	leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name, CONCAT(clients.first_name, " " , clients.last_name)
ORDER BY clients.client_id;	

SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				sites.domain_name,
				COUNT(leads.leads_id)
FROM		leads
JOIN		sites
ON			leads.site_id = sites.site_id
JOIN 		clients
ON			sites.client_id = clients.client_id
-- WHERE	leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY sites.domain_name, CONCAT(clients.first_name, " " , clients.last_name)
ORDER BY clients.client_id;	

-- Query 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.
SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				SUM(billing.amount) as client_10_revenue,
				MONTH(billing.charged_datetime) AS billed_month,
                YEAR(billing.charged_datetime) AS billed_year
FROM		billing
JOIN		clients
ON			billing.client_id = clients.client_id
GROUP BY CONCAT(clients.first_name, " " , clients.last_name) , YEAR(billing.charged_datetime), MONTH(billing.charged_datetime) 
ORDER BY clients.client_id ;


-- Query 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

SELECT	CONCAT(clients.first_name, " " , clients.last_name) AS client_full_name,
				GROUP_CONCAT(sites.domain_name separator ' / ') as sites_list
FROM		sites
JOIN		clients
ON			sites.client_id = clients.client_id
GROUP BY  CONCAT(clients.first_name, " " , clients.last_name)
ORDER BY clients.client_id ;




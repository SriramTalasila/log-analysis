# Log analysis
  This is the Udacity Full Stack Nanodegree Course project 3.
# Project Overview
  This project is the report generation-tool for online news website which outputs the plain text report based on data.
# Views Used in this project
  - author_slug
  - slug_count
  - req_count
  - fail_count
  
  #### author_slug
  ```
    create view author_slug AS select authors.name,articles.slug from authors INNER JOIN articles ON articles.author = authors.id;
  
  ```
  
  ```
      Run this command to create author_slug view.
                name          |           slug
    ------------------------+---------------------------
     Anonymous Contributor  | bad-things-gone
     Markoff Chaney         | balloon-goons-doomed
     Ursula La Multa        | bears-love-berries
     Rudolf von Treppenwitz | candidate-is-jerk
     Ursula La Multa        | goats-eat-googles
     Ursula La Multa        | media-obsessed-with-bears
     Rudolf von Treppenwitz | trouble-for-troubled
     Ursula La Multa        | so-many-bears
  ```
  #### slug_count
  
  ```
  create view slug_count AS select count(path),REPLACE(path, '/article/','')from log where status ='200 OK' and path!='/' group by path order by count(path) DESC;
  
  ```
  ```
  
  This commant will create a view like this
     count  |          replace
    --------+---------------------------
     338647 | candidate-is-jerk
     253801 | bears-love-berries
     170098 | bad-things-gone
      84906 | goats-eat-googles
      84810 | trouble-for-troubled
      84557 | balloon-goons-doomed
      84504 | so-many-bears
      84383 | media-obsessed-with-bears
  
  ```
  #### req_count
  ```
   create view Req_count as select count(time::timestamp::date),time::timestamp::date from log  GROUP BY time::timestamp::date;
  
  ```
  ```
   count |    time
  -------+------------
   38705 | 2016-07-01
   55200 | 2016-07-02
   54866 | 2016-07-03
   54903 | 2016-07-04
   54585 | 2016-07-05
   54774 | 2016-07-06
   54740 | 2016-07-07
   55084 | 2016-07-08
   This view contains the total number of requests per day 
   
  ```
  #### fail_count
  ```
  create view fail_count as select count(time::timestamp::date),time::timestamp::date from log where status='404 NOT FOUND' GROUP BY time::timestamp::date;
  
  ```
  ```
  This view contain Date and request failure count
   count |    time
  -------+------------
     329 | 2016-07-31
     420 | 2016-07-06
    1265 | 2016-07-17
     433 | 2016-07-19
     431 | 2016-07-24
     373 | 2016-07-12
     360 | 2016-07-07
     371 | 2016-07-10
  
  ```
  

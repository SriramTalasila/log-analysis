# Log analysis
  This is the Udacity Full Stack Nanodegree Course project 3.
# Project Overview
  This project is the report generation-tool for online news website which outputs the plain text report based on data.
  
# Prerequisites
  - Install Vagrant and virtualbox.
  - Download the vagrant box suitable for you virtualbox.
  - Configure and install postgres sql .
  - Create a user vagrant with password '12345' and grant Superuser and Createdb permissions.
  - Now Login into psql as vagrant and create a database name news.
  - [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) .sql file and import to news      database
  - Command to import .sql file is
  ```
    psql -d news -f newsdata.sql
  ```

# Views Used in this project
  - top_art
  - author_slug
  - slug_count
  - req_count
  - fail_count
  
  #### top_art
  ```
  create view top_art AS select count(path),REPLACE(path, '/article/','')from log where status ='200 OK' and path!='/' group by path order by count(path) DESC LIMIT 3;
  
  ```
  ```
  This View Contains the top tree articles views count
   count  |      replace
  --------+--------------------
   338647 | candidate-is-jerk
   253801 | bears-love-berries
   170098 | bad-things-gone
  
  Here 'replace' is the slug of the article
  ```
  
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
  
# Running the script 
  After importing the data and creating the views move the loganalysis.py file to your vagrant directory or git clone the directory
  in vagrant virtual machine and run the file using
  ```
  python loganalysis.py
  ```
# Output of script
```
  vagrant@ubuntu-xenial:/vagrant/newslogs$ python loganalaysis.py
    Top three most popular articles of the time
        candidate-is-jerk ---  338647
        bears-love-berries ---  253801
        bad-things-gone ---  170098
    Top most popular authors of the time
        Ursula La Multa ---> 507594
        Rudolf von Treppenwitz ---> 423457
        Anonymous Contributor ---> 170098
        Markoff Chaney ---> 84557
    Day with more than 1% of requests lead to errors
        2016-07-17 ---> 2.26 %
```

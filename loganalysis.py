#!/usr/bin/env python
import psycopg2

# This module helps to connect to postgres database
# connection to the database with user vagrant and password 12345
conn = psycopg2.connect(database="news",
                        user="vagrant",
                        password="12345",
                        host="127.0.0.1",
                        port="5432")
cur = conn.cursor()

# Function that prints Most popular articles all the time using view top_art


def print_pop_art():
    print("Top three most popular articles of the time\n")
    sql = '''select articles.title,top_art.count from articles INNER JOIN top_art
    ON articles.slug=top_art.replace order by top_art.count DESC;'''
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print str(row[0]), "--->", row[1], "\n"

# This function uses views author_slug And slug count
# to get the popular authors all the time
# Refer to the readme for more information about views
# and thier schemas


def print_pop_auth():
    print("Top most popular authors of the time\n")
    sql = '''select author_slug.name,sum(slug_count.count) from author_slug
    INNER JOIN slug_count ON
    author_slug.slug=slug_count.replace GROUP BY author_slug.name
    ORDER BY sum(slug_count.count) DESC;'''
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print str(row[0]), "--->", row[1], "\n"

# This function prints the failure percentage of requests


def print_err_percent():
    print("Day with more than 1% of requests lead to errors\n")
    sql = '''select fail_count.count*100.00 / req_count.count as percent,
    fail_count.time from fail_count INNER JOIN req_count
    ON fail_count.time=req_count.time
    where fail_count.count*100.00 / req_count.count > 1
    ORDER BY  fail_count.count*100.00 / req_count.count DESC LIMIT 1;'''
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print row[1], "--->", round(row[0], 2), "%", "\n"

print_pop_art()
print_pop_auth()
print_err_percent()
# closing cursor
cur.close()
# closing connection with database
conn.close()

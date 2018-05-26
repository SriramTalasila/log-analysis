import psycopg2
#psycopg2 module help to connect with postgresql database
#connection to the database news as user vagrant
conn = psycopg2.connect(database="news", user = "vagrant", password = "12345", hos$cur = conn.cursor()

#Function that prints Most popular articles all the time
def print_pop_art():
    print("Top three most popular articles of the time\n")
    cur.execute("select count(path),REPLACE(path, '/article/','')from log where st$    rows = cur.fetchall()
    for row in rows:
        print  str(row[1]),"--- ",row[0], "\n"

#This function uses views author_slug And slug count
#to get the popular authors all the time
# Refer to the readme for more information about views
# and thier schemas 

def print_pop_auth():
    print("Top most popular authors of the time\n")
    cur.execute("select author_slug.name,sum(slug_count.count) from author_slug IN$    rows = cur.fetchall()
    for row in rows:
        print  str(row[0]),"--->",row[1], "\n"

#this function prints the failure percentage of requests
def print_err_percent():
    print("Day with more than 1% of requests lead to errors\n")
    cur.execute("select fail_count.count*100.00 / req_count.count as percent,fail_$    rows = cur.fetchall()
    for row in rows:
        print  row[1],"--->",round(row[0],2),"%","\n"

print_pop_art()
print_pop_auth()
print_err_percent()
#closing cursor
cur.close()
#closing connection with database
conn.close()
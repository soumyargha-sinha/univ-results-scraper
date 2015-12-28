from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from selenium.common.exceptions import NoSuchElementException
import MySQLdb
db = MySQLdb.connect("localhost","user","pass","database")
cursor = db.cursor()
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Firefox()
test = 0
print "Enter the first roll no : "
no = int(raw_input())
n = no
print "Enter sem no : 1 or 3 or 5 or 7 : "
sem = int(raw_input())
while(no < n + 130 ): 
    elexists = 0
    if(test == 3):
	break
    driver.get("http://wbutech.net/result_odd.php")
    element = driver.find_element_by_name("rollno")
    element.send_keys(no)
    if(sem == 1):
    	driver.find_element_by_id("sem_1").click()
    elif(sem == 3):
	driver.find_element_by_id("sem_3").click()
    elif(sem == 5):
	driver.find_element_by_id("sem_5").click()
    elif(sem == 7):
	driver.find_element_by_id("sem_7").click()    
    else:
	print "WTF Dude!"
    if(no>0):
	try:
        	body = driver.find_element_by_class_name("errormsgbox")
    	except NoSuchElementException, e:
        	elexists = 1
    if(elexists == 0):
	no = no + 1
	test = test + 1
        continue
    for el in driver.find_elements_by_xpath("//th[contains(.,'Name : ')]"):
        name = el.text
    for m in driver.find_elements_by_xpath("//td[contains(.,'SEMESTER : ')]"):
        point = m.text
    cursor.execute('''INSERT into aot (rollno, sem, name, odd)
                  values (%r, %r, %r, %r)'''%(no, sem, db.escape_string(name), db.escape_string(point)))
    db.commit()
    no = no + 1
display.stop()
driver.quit()


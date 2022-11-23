from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
DRIVER_PATH = '/Users/mayank/Downloads/chromedriver 2'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://clutch.co/developers')
company = driver.find_elements_by_xpath('//h3[@class="company_info"]')
company1 = driver.find_elements_by_xpath('//a[@data-link_text="Profile Title"]')
location = driver.find_elements_by_xpath('//span[@class="locality"]')
rating = driver.find_elements_by_xpath('//span[@class="rating sg-rating__number"]')
review_count = driver.find_elements_by_xpath('//a[@class="reviews-link sg-rating__reviews directory_profile"]')
hourly_rate = driver.find_elements_by_xpath('//div[@data-content="<i>Avg. hourly rate</i>"]')
min_project_size = driver.find_elements_by_xpath('//div[@data-content="<i>Min. project size</i>"]')
employee_size = driver.find_elements_by_xpath('//div[@data-content="<i>Employees</i>"]')

link=driver.find_elements_by_xpath('//a[@class="website-link__item"]')
company_list = []
website_list=[]
location_list=[]
#contact_list=[]
rating_list=[]
review_count_list=[]
hourly_rate_list=[]
min_project_size_list=[]
employee_size_list=[]
#driver1 = webdriver.Chrome(executable_path=DRIVER_PATH)
for p in range(len(company)):
    #print(company[p].text)
    company_list.append(company[p].text)
for p in link:
    link1=p.get_attribute("href")
    website_list.append(link1)
    #driver1.get(link1)
    #print(link1)
    

#for p in company1:
    #print(p.get_attribute("href"))
    #link2=p.get_attribute("href")
    #driver1.get(link2)
    #contact = driver1.find_elements_by_xpath('//a[@class="contact phone_icon"]')
    #print(contact)
#for p in range(len(company)):
    #print(p.get_attribute("href"))
    #link2='https://clutch.co/profile/'+company[p].text.lower()
    #print(link2)
    #driver1.get(link2)
    #company_list.append(company[p].text)
for p in range(len(location)):
    #print(location[p].text)
    location_list.append(location[p].text)
#for p in range(len(contact)):
    #print(contact[p].text)
    #contact_list.append(contact[p].text)
for p in range(len(rating)):
    #print(rating[p].text)
    rating_list.append(rating[p].text)
for p in range(len(review_count)):
    #print(review_count[p].text)
    review_count_list.append(review_count[p].text)
for p in range(len(hourly_rate)):
    #print(hourly_rate[p].text)
    hourly_rate_list.append(hourly_rate[p].text)
for p in range(len(min_project_size)):
    #print(min_project_size[p].text)
    min_project_size_list.append(min_project_size[p].text)
for p in range(len(employee_size)):
    #print(employee_size[p].text)
    employee_size_list.append(employee_size[p].text)    
#print(len(company_list))
#print(len(website_list))
#print(len(location_list))
#print(len(rating_list))
#print(len(review_count_list))
#print(len(hourly_rate_list))
#print(len(min_project_size_list))
#print(len(employee_size_list))
#print(len(company))
df = pd.DataFrame({'Company':company_list,'Website':website_list,'Location':location_list,'Rating':rating_list,'Review Count':review_count_list,'Hourly Rate':hourly_rate_list,'Min Project Size':min_project_size_list,'Employee Size':employee_size_list}) 
df.to_csv('info.csv', index=False, encoding='utf-8')
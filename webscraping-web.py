import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
jop_skill = []
links = []
salary = []

#while True:
    # Frist step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")
    #result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_num}")

    # 2nd step save page content/markup
src = result.content
    #print(src)
       
    # 3rd step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
    
    # page_limit = int(soup.find("strong").text)
    
    # if (page_num > page_limit // 15):
    #     print("pages ended , terminate")
    #     break
        
    
    #print(soup)

    # 4th step find the elements containing info we need 
    #-- job titles, jop skills, company names, location names
job_titles = soup.find_all("h2", {"class":"css-m604qf"} )
company_names = soup.find_all("a", {"class":"css-17s97q8"} )
location_names = soup.find_all("span", {"class":"css-5wys0k"} )
jop_skills = soup.find_all("div", {"class":"css-y4udm8"} )
    

    # 5th step loop over returned lists to extract needed info into other list
for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        links.append(job_titles[i].find("a").attrs['href'])
        company_name.append(company_names[i].text)
        location_name.append(location_names[i].text)
        jop_skill.append(jop_skills[i].text)
    #page_num += 1
    #print("page switching")

# print(links)
# print(job_title)
# print(company_name)
# print(location_name)
# print(jop_skill)

for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    salaries = soup.find_all("div", {"class":"css-rcl8e5","class":"css-4xky9y"} )
    print(salaries)
    #salary.append(salaries.text.strip())
    
    
# 6th step create csv file and fill it with values
file_list = [job_title, company_name, location_name, jop_skill, links, salary]
exported = zip_longest(*file_list) 
with open("C:/Users/m-badr/Desktop/course_ML-Python/jobs.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["job_title", "company_name", "location_name", "jop_skill", "links", "salary"])
    wr.writerows(exported)

# 7th step to fetch the link of the job and fetch in page details 
# -- salary, job requirements

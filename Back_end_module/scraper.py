import requests
from bs4 import BeautifulSoup

def scrape(jobId):

    job_posting_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/' + jobId

    response = requests.get(job_posting_url)
    soup = BeautifulSoup(response.text,'html.parser')

    job_object ={}
    
    try:
        job_object["job_title"] = soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job_object["job_title"] = None

    try:
        parent = soup.find("ul",{"class":"description__job-criteria-list"})
        text = list(parent.descendants) 
        inner_soup_1 = BeautifulSoup(str(text[1]),'html.parser')
        seniority_level_element = inner_soup_1.find('li', class_='description__job-criteria-item')
        job_object["seniority_level"]  = seniority_level_element.find('span', class_='description__job-criteria-text--criteria').get_text(strip=True)
    except():
        job_object["seniority_level"] = None

    try:
        parent = soup.find("ul",{"class":"description__job-criteria-list"})
        text = list(parent.descendants) 
        inner_soup_2 = BeautifulSoup(str(text[10]),'html.parser')
        employment_type_element = inner_soup_2.find('li', class_='description__job-criteria-item')
        job_object["employment_type"]  = employment_type_element.find('span', class_='description__job-criteria-text--criteria').get_text(strip=True)
    except():
        job_object["employment_type"] = None

    try:
        job_object["job_description"] = soup.find("div",{"class":"show-more-less-html__markup"}).text.strip()
    except:
        job_object["job_description"] = None

    return job_object
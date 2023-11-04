import requests
from bs4 import BeautifulSoup

def scrape(jobId):

    job_posting_url = 'https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/' + jobId

    response = requests.get(job_posting_url)
    soup = BeautifulSoup(response.text,'html.parser')

    job_object ={}

    try:
        job_object["company"] = soup.find("div",{"class":"top-card-layout__card"}).find("a").find("img").get('alt')
    except:
        job_object["company"] = None
    
    try:
        job_object["job_title"] = soup.find("div",{"class":"top-card-layout__entity-info"}).find("a").text.strip()
    except:
        job_object["job_title"] = None

    try:
        job_object["level"] = soup.find("ul",{"class":"description__job-criteria-list"}).find("li").text.replace("Seniority level","").strip()
    except:
        job_object["level"] = None
    
    try:
        job_object["description"] = soup.find("div",{"class":"show-more-less-html__markup"}).text.strip()
    except:
        job_object["description"] = None


    return job_object
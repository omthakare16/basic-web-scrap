import requests
from bs4 import BeautifulSoup
import json

url="https://realpython.github.io/fake-jobs/"
page=requests.get(url)
soup= BeautifulSoup(page.content,"html.parser")
dictr = {"job-data":[]}


results = soup.find(id="ResultsContainer")

# job_elements = results.find_all("h2", string=lambda text: "python" in text.lower())
# # print(job_elements[1].text)
file=open("data.json","w")
# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in job_elements
# ]
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    dictr['job-data'].append({"title":title_element.text.strip(),"company":company_element.text.strip(),"location":location_element.text.strip(),"link":f"Apply here: {link_url}"})
   



final_data = json.dumps(dictr,indent=4)
file.write(final_data)
    
    # file.write(title_element.text.strip())

    # file.write(company_element.text.strip())
    # file.write("\n")
    # file.write(location_element.text.strip())
    # file.write("\n")
    # link_url = job_element.find_all("a")[1]["href"]
    # file.write(f"Apply here: {link_url}\n")
    # file.write("\n")

    # print(job_element.text, "\n")
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     # file.write(title_element.text())
#     # file.write(company_element.text.strip())
#     # file.write(location_element.text.strip())
#     print(title_element)


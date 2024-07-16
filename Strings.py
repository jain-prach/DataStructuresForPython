from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')

#connecting chrome webdriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# login
driver.get("https://www.linkedin.com/login")
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("..")
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys("..")
password.send_keys(Keys.RETURN)
time.sleep(30)

# search data science in jobs
driver.get("https://www.linkedin.com/jobs/search/?keywords=data%20scientist")
# job_cards = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container")))
# print(len(job_cards)) ### only capturing 7 job_cards element

selected_phrases = ['Job Responsibilities', 'Key Responsibilities', 'Responsibilities', 'Role and Responsibilities', 'Mandatory skills', 'Qualifications',
    'Job Description', 'Must Have', 'Good to Have', 'Nice to Have', 'Candidate Profile', 'Preferred Qualifications', 'Job Requirements', 'Skill Set', 'Duties', 'Requirements', 'Required skills', 'Preferred Skills']
exclude_phrases = ['About', 'Last date', 'Job Location', 'Job Title', 'Role', 'Location', 'Description', 'We Offer', 'Application Link', 'Our Offerings', 'We work', 'Meet Your Team', 'CTC', 'Salary', 'Our Client']
details_text = ''

#get details from each card
for _ in range(5):
    #clicking each card
    for i in range(1, 40):
        try:
            job_card_xpath = f"(//div[contains(@class, 'job-card-container')])[{i}]"
            job_card = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, job_card_xpath)))
            print(f"Processing card {i}") 
            driver.execute_script("arguments[0].scrollIntoView();", job_card)
            time.sleep(1) 
            job_card.click()
            time.sleep(1)
            #finding job details
            try:
                job_details = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "jobs-description-content")))
            except:
                print("Couldn't find job details. Skipping this card")
                continue
            #getting text available in job details
            html_content = job_details.get_attribute('innerHTML')
            if not html_content:
                print("No HTML content found, skipping this card")
                continue
            soup = BeautifulSoup(html_content, 'html.parser')
            #finding relevant job details
            spans = soup.find_all('span')
            for j, span in enumerate(spans):
                text = span.get_text(strip=True)
                if text != "":
                    if not any(phrase.lower() in text.lower() for phrase in selected_phrases):
                        if any(phrase.lower() in text.lower() for phrase in exclude_phrases):
                            # print(f"Excluding phrase: {text}")
                            try:
                                j=j+3
                                span = spans[j+3]
                                continue
                            except:
                                try:
                                    j=j+2
                                    span = spans[j+2]
                                    continue
                                except:
                                    print("no skips")
                                    continue
                        else:
                            # print(f"Printing span {j}")
                            details_text = f"{details_text} {text}"
                            # print(text)
                    else:
                        # print(f"Excluding phrase: {text}") 
                        continue
        except:
            print("Couldn't click job card")
            break
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "jobs-search-pagination__button--next"))
        )
        next_button.click()
        time.sleep(3)
        print("Next Page")
        continue
    except:
        print("No next page")
        break
driver.quit()

with open("Output.txt", "w") as text_file:
    text_file.write(details_text)

with open("Output.txt", "r") as file:
    details_text = file.read().rstrip()
    # clean text in details_text
    details_text = re.sub(r'http\S+', '', details_text)  # Remove URLs
    details_text = re.sub(f'[{string.punctuation}]', '', details_text)  # Remove punctuation
    # using nltk - natural language toolkit for cleaning data
    # set(stopwords.words())
    nltk_stopwords = set(stopwords.words('english'))
    custom_stopwords = set(['skills', 'proficiency', 'qualified', 'preferred', 'qualifications', 'experience', 'knowledge', 'country', 'Job', 'details', 'apply', 'eg', 'effectively', 'ability', 'transfer', 'etc', 'excellent', 'plus', 'city', 'manage', 'incorporate', 'data', 'science', 'scientist', 'technical', 'non-technical', 'using', 'develop', 'across', 'need', 'following', 'demonstrate', 'work', 'working', 'strong', 'provide'])
    total_stopwords = nltk_stopwords.union(custom_stopwords)
    details = word_tokenize(details_text)
    clean_details = ' '.join([w for w in details if not w.lower() in total_stopwords])
    with open('Clean.txt', 'w') as w_file:
        w_file.write(clean_details)
    # print(clean_details)
    # build a word cloud
    word_cloud = WordCloud(width=800, height=400, background_color='white').generate(clean_details)
    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Requirements in Data Science Jobs')
    plt.show()
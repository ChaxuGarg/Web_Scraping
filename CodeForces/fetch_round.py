from selenium import webdriver
import sys
import os
import time
PATH = "/Users/chaxu/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
contest = sys.argv[1]
website = "https://codeforces.com/contest/" + contest
driver.get(website)
table = driver.find_element_by_class_name("problems")
links = table.find_elements_by_tag_name("a")
for i in range(len(links)):
    if i%4 != 0:
        continue
    time.sleep(2)
    table = driver.find_element_by_class_name("problems")
    links = table.find_elements_by_tag_name("a")
    link = links[i].get_attribute("href")
    problem_code = link.split("https://codeforces.com/contest/"+ contest +"/problem/", 1)[1]
    if not os.path.exists(contest + "/" + problem_code):
        os.makedirs(contest + "/" + problem_code)
    links[i].click()
    time.sleep(2)
    driver.save_screenshot(contest + "/" + problem_code + "/problem.png")
    inputs = driver.find_elements_by_class_name("input")
    outputs = driver.find_elements_by_class_name("output")
    for j in range(len(inputs)):
        input_text = inputs[j].find_element_by_tag_name("pre")
        txt = input_text.text
        f = open(contest + "/" + problem_code + "/input" + str(j+1) + ".txt", "w")
        f.write(txt)
        f.close
    for j in range(len(outputs)):
        output_text = outputs[j].find_element_by_tag_name("pre")
        txt = output_text.text
        f = open(contest + "/" + problem_code + "/output" + str(j+1) + ".txt", "w")
        f.write(txt)
        f.close
    driver.back()



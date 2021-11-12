import codecs
import os
import re
from shutil import copyfile

import requests
import yaml

day = 17
year = 2020

cookies = {
    "session": None
}

url = "https://adventofcode.com/" + str(year) + "/day/"


def html_to_markdown(text: str):
    text = re.search('<main>(.|\n)*</main>', text).group(0)
    text = text.replace('<em class="star">', "**") \
        .replace('</em>', "**") \
        .replace('<em>', "**") \
        .replace('<p>', "") \
        .replace('</p>', "\n") \
        .replace('<pre><code>', "```\n") \
        .replace('</code></pre>', "```\n") \
        .replace("---</h2>", "\n") \
        .replace('<article class="day-desc"><h2>---', "#") \
        .replace("<main>", "") \
        .replace("</main>", "") \
        .replace("</article>", "") \
        .replace('<article class="day-desc"><h2 id="part2">---', "## ") \
        .replace("<ul>", "") \
        .replace("</ul>", "") \
        .replace("</li>", "") \
        .replace("<li>", "- ") \
        .replace("<code>", "`") \
        .replace("</code>", "`")\

    text = re.sub('<script>.*</script>', "", text)
    text = re.sub('<a href.*">', "", text)
    text = re.sub('<p class="day-success">(.|\n)*', "", text)
    text = re.sub('Your puzzle answer was.*.', "", text)
    text = re.sub('To begin, (.|\n)*', "", text)

    title = re.search('# .*', text).group(0)

    text = text.replace(title, title
                        + "\n\nCopyright (c) Eric Wastl "
                        + "\n\n[Link to Day " + str(day)
                        + "](" + url + str(day)
                        + ") \n\n## Part One")
    return text


if __name__ == '__main__':

    if os.path.exists("../session_key.yaml"):
        with open("../session_key.yaml", "r") as file:
            cookies = yaml.safe_load(file)

    webpage = requests.get(url + str(day), cookies=cookies).text

    format_day = f"{day:02d}"

    year_dir = os.getcwd()[:-6] + "\\" + str(year)
    day_dir = os.getcwd()[:-6] + "\\" + str(year) + "\\day_" + format_day
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
    if not os.path.exists(day_dir):
        os.mkdir(day_dir)

    with codecs.open("../" + str(year) + "/day_" + format_day + "/README.md", "w", "utf-8") as file:
        file.truncate(0)
        file.write(html_to_markdown(webpage))

    webpage = requests.get(url + str(day) + "/input", cookies=cookies).text

    with open("../" + str(year) + "/day_" + format_day + "/input.txt", "a") as file:
        file.truncate(0)
        file.write(webpage)

    path = "../" + str(year) + "/day_" + format_day + "/puzzle.py"
    if not os.path.exists(path):
        copyfile("puzzle_template.py", path)

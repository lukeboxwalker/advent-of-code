import codecs
import os
import re
import sys
from shutil import copyfile

import requests
import yaml

cookies = {
    "session": None
}


def html_to_markdown(text: str):
    text = re.search('<main>(.|\n)*</main>', text).group(0)
    text = text.replace('<em class="star">', "<b>") \
        .replace("<main>", "") \
        .replace("</main>", "") \
        .replace('<article class="day-desc">', "") \
        .replace("</article>", "") \
        .replace('</em>', "</b>") \
        .replace('<em>', "<b>") \

    text = re.sub('<script>.*</script>', "", text)
    text = re.sub('<p class="day-success">*</p>', "", text)
    text = re.sub('<p>Your puzzle answer was <code>[0-9]*</code>.</p>', "", text)

    title = re.search('<h2>--- .* ---</h2>', text).group(0)[8:-9]
    text = re.sub('<h2>--- .* ---</h2>', "<h1>" + title + " 🎄</h1><p>Copyright (c) Eric Wastl</p><a href=" + url + str(
        day) + ">Link to Day " + str(day) + "</a><h2>Part One 🎁</h2>", text)
    text = re.sub('<h2 id="part2">--- Part Two ---</h2>', "<h2>Part Two 🎁</h2>", text)
    return text


if __name__ == '__main__':
    os.chdir(str(sys.argv[0].split("setup.py")[0]))

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    url = "https://adventofcode.com/" + str(year) + "/day/"

    if os.path.exists("../session_key.yml"):
        with open("../session_key.yml", "r") as file:
            cookies = yaml.safe_load(file)

    webpage = requests.get(url + str(day), cookies=cookies).text

    format_day = f"{day:02d}"

    year_dir = os.getcwd()[:-3] + "\\year_" + str(year)
    day_dir = os.getcwd()[:-3] + "\\year_" + str(year) + "\\day_" + format_day
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
    if not os.path.exists(day_dir):
        os.mkdir(day_dir)

    path = "../year_" + str(year) + "/day_" + format_day

    with codecs.open(path + "/README.md", "w", "utf-8") as file:
        file.truncate(0)
        file.write(html_to_markdown(webpage))

    webpage = requests.get(url + str(day) + "/input", cookies=cookies).text

    with open(path + "/input.txt", "a") as file:
        file.truncate(0)
        file.write(webpage[:-1])

    solution_path = path + "/test_input.txt"
    if not os.path.exists(solution_path):
        copyfile("test_input.txt", solution_path)

    solution_path = path + "/solution.txt"
    if not os.path.exists(solution_path):
        copyfile("solution_template.txt", solution_path)

    puzzle_path = path + "/puzzle.py"
    if not os.path.exists(puzzle_path):
        copyfile("puzzle_template.py", puzzle_path)

    os.system('git add ' + path)

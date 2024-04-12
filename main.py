#!/usr/bin/python3
import re
from bs4 import BeautifulSoup


def read_html_file(file_path):
    try:
        with open(file_path, "r", encoding = "utf-8") as file:
            return (file.read())
    except FileNotFoundError:
        print("HTML file not found.")
        return (None)


def html2md(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    md_content = ""

    # Define a list of supported HTML tags
    # supported_tags = ["h1"]

    # Find and format h1 elements
    for h1 in soup.find_all("h1"):
        # Remove leading and trailing spaces
        h1_stripped = h1.text.strip().upper()
        md_content += f'<h1 align="center"><b>{h1_stripped}</b></h1>\n'

    # Find and format span elements with class "label label-primary"
    span_count = 0
    span_list = []
    for span in soup.find_all("span", class_="label label-primary"):
        span_count += 1
        span_list.append(span.text)
    if span_count > 0:
        tag_section = ""
        for _ in range(span_count):
            if _ == span_count - 1:
                tag_section += f"<code>{span_list[_]}</code>"
            else:
                tag_section += f"<code>{span_list[_]}</code> "
        md_content += f'<div align="center">{tag_section}</div>\n'

    md_content += "\n"

    for h2 in soup.find_all("h2"):
        md_content += ("\n<!--==================================================-->\n")
        h2_stripped = h2.text.strip()
        if h2.text == "Background Context":
            md_content += f"<br>\n\n## {h2_stripped}\n"

            # Create a list to store elements to process
            elements_to_process = []

            # Find all siblings of the current h2 until the next h2
            next_sibling = h2.find_next_sibling()
            while next_sibling and next_sibling.name != "h2":
                elements_to_process.append(next_sibling)
                next_sibling = next_sibling.find_next_sibling()

            # Process the elements in the elements_to_process list
            for next_sibling in elements_to_process:
                if next_sibling.name == "h3":
                    md_content += str(next_sibling)+"\n\n"
                elif next_sibling.name == "p":
                    p_content = str(next_sibling)+"\n\n"
                    md_content_wo_open_p = p_content.replace("<p>", "")
                    md_content_wo_close_p = md_content_wo_open_p.replace("</p>","")
                    md_content += md_content_wo_close_p
                else:
                    md_content += str(next_sibling)+"\n\n"
                next_sibling = next_sibling.find_next_sibling()

        elif h2.text == "Resources":
            md_content += f"<br>\n\n## {h2_stripped}\n"

            # Create a list to store elements to process
            elements_to_process = []

            # Find all siblings of the current h2 until the next h2
            next_sibling = h2.find_next_sibling()
            while next_sibling and next_sibling.name != "h2":
                elements_to_process.append(next_sibling)
                next_sibling = next_sibling.find_next_sibling()

            # Process the elements in the elements_to_process list
            for next_sibling in elements_to_process:
                if next_sibling.name == "h3":
                    md_content += str(next_sibling)+"\n\n"
                elif next_sibling.name == "ul":
                    li_tags = next_sibling.findChildren('li')
                    for li in li_tags:
                        a_tags = li.findChildren('a')
                        # em_tags = li.findChildren('em')
                        for a in a_tags:
                            if li.em is None:
                                md_content += f'<details>\n<summary><b><a href="{a["href"]}">{a.text}</a></b></summary><br>\n\n\n<br><p align="center">※※※※※※※※※※※※</p><br>\n</details>\n\n\n'
                            else:
                                md_content += f'<details>\n<summary><b><a href="{a["href"]}">{a.text}</a></b> ({li.em})</summary><br>\n\n\n<br><p align="center">※※※※※※※※※※※※</p><br>\n</details>\n\n\n'
                elif next_sibling.name == "p":
                    strong_tags = next_sibling.findChildren("strong")
                    for strong in strong_tags:
                        md_content += ""
                else:
                    md_content += str(next_sibling)+"\n"
                next_sibling = next_sibling.find_next_sibling()

        elif h2.text == "Learning Objectives":
            md_content += f"<br>\n\n## {h2_stripped}\n"

            # Create a list to store elements to process
            elements_to_process = []

            # Find all siblings of the current h2 until the next h2
            next_sibling = h2.find_next_sibling()
            while next_sibling and next_sibling.name != "h2":
                elements_to_process.append(next_sibling)
                next_sibling = next_sibling.find_next_sibling()

            # Process the elements in the elements_to_process list
            for next_sibling in elements_to_process:
                prev_sibling = next_sibling.find_previous_sibling()
                if next_sibling.name == "h3":
                    md_content += str(next_sibling)+"\n\n"
                elif next_sibling.name == "ul" or prev_sibling.text == "General":
                    li_tags = next_sibling.findChildren('li')
                    for li in li_tags:
                        li_content = str(li)
                        md_wo_open_li = li_content.replace("<li>", "")
                        md_wo_close_li = md_wo_open_li.replace("</li>", "")
                        li_content = md_wo_close_li
                        md_content += f'<details>\n<summary><b><a href=" "> </a>{li_content}</b></summary><br>\n\n\n<br><p align="center">※※※※※※※※※※※※</p><br>\n</details>\n\n\n'
                    md_content += "\n<br>\n"
                elif next_sibling.name == "p":
                    strong_tags = next_sibling.findChildren("strong")
                    for strong in strong_tags:
                        md_content += ""
                else:
                    md_content += str(next_sibling)+"\n"
                next_sibling = next_sibling.find_next_sibling()

        elif h2.text == "Requirements":
            md_content += f"<br>\n\n## {h2_stripped}\n"

            # Create a list to store elements to process
            elements_to_process = []

            # Find all siblings of the current h2 until the next h2
            next_sibling = h2.find_next_sibling()
            while next_sibling and next_sibling.name != "h2":
                elements_to_process.append(next_sibling)
                next_sibling = next_sibling.find_next_sibling()

            # Process the elements in the elements_to_process list
            for next_sibling in elements_to_process:
                if next_sibling.name == "h3":
                    md_content += str(next_sibling)+"\n\n"
                elif next_sibling.name == "ul":
                    li_tags = next_sibling.findChildren('li', recursive=False)
                    for li in li_tags:
                        li_content = str(li) + "\n"
                        md_content_wo_open_li = li_content.replace("<li>", "- ")
                        md_content_wo_close_li = md_content_wo_open_li.replace("</li>", "")
                        md_content += md_content_wo_close_li
                else:
                    md_content += str(next_sibling)+"\n"
                next_sibling = next_sibling.find_next_sibling()

        elif h2.text == "Tasks":
            md_content += f"<br>\n\n## {h2_stripped}\n"
            # Find all sections with class 'panel panel-default task-card'
            tasks = soup.find_all('div', class_='panel panel-default task-card')

            # Iterate over each task
            for task in tasks:
                # Extract title and label
                title = task.find("h3", class_="panel-title").text.strip()
                label = task.find("span", class_=["label", "label-info"]).text.strip()

                # Extract file info
                file_div = task.find("div", class_="list-group-item")
                file_ul = file_div.find("ul")
                for li in file_ul:
                    file_info = file_ul.findChildren("code")
                file_name = str(file_info[2]).replace("<code>", "").replace("</code>", "")
                files = file_name.split(", ")
                file_name = ", ".join([f"[{file}]()" for file in files])
                md_content += f"""<details>
<summary>

### {title}
`{label}`

File: {file_name}
</summary>
"""

                # Extract task content
                task_body = task.find("div", class_="panel-body")
                task_content = task_body.children
                elements_to_process = ["p", "ul", "pre"]
                for element in task_content:
                    if element.name in elements_to_process:
                        stripped_element = str(element).strip()
                        md_content += f"""
{stripped_element}
"""
                # script_content = task.find("pre").text.strip()

                md_content += f"""

</details>

"""

        else:
            md_content += f"<br>\n\n## {h2_stripped}\n"
            # Create a list to store elements to process
            elements_to_process = []

            # Find all siblings of the current h2 until the next h2
            next_sibling = h2.find_next_sibling()
            while next_sibling and next_sibling.name != "h2":
                elements_to_process.append(next_sibling)
                next_sibling = next_sibling.find_next_sibling()

            # Process the elements in the elements_to_process list
            for next_sibling in elements_to_process:
                if next_sibling.name == "h3":
                    md_content += str(next_sibling)+"\n\n"
                elif next_sibling.name == "p":
                    p_content = str(next_sibling)+"\n\n"
                    md_content_wo_open_p = p_content.replace("<p>", "")
                    md_content_wo_close_p = md_content_wo_open_p.replace("</p>","")
                    md_content += md_content_wo_close_p
                else:
                    md_content += str(next_sibling)+"\n\n"
                next_sibling = next_sibling.find_next_sibling()

    return (md_content)


def save_to_readme(text, filename="README.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


# def remove_whitespace_before_tags(text):
#     # Regular expression to match leading whitespace before HTML tags
#     pattern = re.compile(r'^\s+(?=<)')
    
#     # Process each line and remove leading whitespace before HTML tags
#     cleaned_text = re.sub(pattern, '', text)
    
#     return (cleaned_text)


def main():
    html_file_path = str(input("Path to file: "))
    html_content = read_html_file(html_file_path)
    if html_content:
        readme_content = html2md(html_content)
        # clean_readme = remove_whitespace_before_tags(readme_content)
        save_to_readme(readme_content)
        print("README.md file created successfully.")
    else:
        print("Failed to read HTML file.")


if __name__ == "__main__":
    main()

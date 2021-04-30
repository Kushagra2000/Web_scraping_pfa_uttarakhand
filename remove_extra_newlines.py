import re


with open('scraped_text.txt','r+') as f:
    content=f.read()
    new_content = re.sub(r'\n{3,}', '\n\n', content).strip()

    with open('formatted_st.txt','w+') as nf:
        nf.write(new_content)

from openai import OpenAI

def generate_report(vulns):

    with open("templates/pentest_prompt.txt") as f:
        prompt=f.read()

    prompt=prompt.replace("{vulnerabilities}",str(vulns))

    client=OpenAI()

    res=client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content

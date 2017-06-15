import tldextract
import article_html_output
import mercury_html_output


article_links = "article_links.txt"
mercury_links = "mercury_links.txt"

def get_lists(article_links, mercury_links):
    with open("article_links.txt","r") as website:
        article_content = website.read().splitlines()

    for i in range(0,len(article_content)):
        url_extract = tldextract.extract(article_content[i])
        article_content[i] = url_extract.domain + '.' + url_extract.suffix

    # THESE 2 LINES REMOVES REDUNDENCY
    article_content = set(article_content)
    article_content = list(article_content)


    with open("mercury_links.txt","r") as other_website:
        mercury_content = other_website.read().splitlines()

    for i in range(0,len(mercury_content)):
        url_extract = tldextract.extract(mercury_content[i])
        mercury_content[i] = url_extract.domain + '.' + url_extract.suffix

    # REMOVES REDUNDENCY FROM THE MERCURY_CONTENT LIST
    mercury_content = set(mercury_content)
    mercury_content = list(mercury_content)

    # REMOVES THE COMMON URLS BETWEEN article_content and mercury_content
    common_links = set(article_content).intersection(mercury_content)
    article_content = list(set(article_content) - common_links)
    print(article_content,len(article_content))
    print(mercury_content,len(mercury_content))
    return article_content, mercury_content


def get_result():
    url=input('Enter the url')
    extract_url = tldextract.extract(url)
    check_url = extract_url.domain + '.' + extract_url.suffix

    # UNCOMMENT LINE BELOW WHEN FUNCTION DEFINED ABOVE IS USED
    # article_content, mercury_content = get_lists(article_links,mercury_links)

    # USED WHEN LIST IS AL READY PRESENT
    article_content, mercury_content = article_links, mercury_links

    if check_url in article_content:
        output = article_html_output.article_output(url)

    elif check_url in mercury_content:
        output = mercury_html_output.mercury_output(url)

    else:
        output = mercury_html_output.mercury_output(url)

    return output

a=get_result()
print(a)





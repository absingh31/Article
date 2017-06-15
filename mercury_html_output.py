import mercury_Json_output
#import client
import numpy
import tldextract
#import html_text

def mercury_output(url):
    api_key = 'zEbEqMY846voNjx8urJPNdDW99amKrRnjbLXkZz0'

    content = mercury_Json_output.result(api_key, url)
    
    if 'error' in content.keys():
        print("WRONG URL, try checking if the url is correct")
        exit(0)

    if (content == None):
        print("ERROR: can't get a valid response from the API")
        exit(0)
    output_to_return= ""

    html_open = """<html> \n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n
                   <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">\n
                   <link rel="stylesheet" type="text/css" href="style.css">\n</head>\n<body>"""

    output_to_return = ''.join([output_to_return, html_open])

    # Title of the content added to local html file
    if (len(content['title'])!=0):
        html_heading = """<div class="smart_article_title"><!-- DIV CONTAINER FOR TITLE -->\n<h1 align="center">%s</h1>\n</div> \n\n"""%(content['title'])
        output_to_return = '.'.join([output_to_return, html_heading])

    else:
        html_heading = ''
        output_to_return = '.'.join([output_to_return, html_heading])

    # Adds source website to local html file
    # site_name = client.MercuryAPICall.get_top_domain(url)
    url_extract = tldextract.extract(url)
    site_name = url_extract.domain + '.' + url_extract.suffix
    if len(site_name)!=0:
        html_site_name = """<li>%s</li>\n"""%(site_name)

    else:
        html_site_name = ''

    # Adds published date if exist to local html file
    if (len(str(content['date_published']))>=9):
        html_date = """<li>%s</li>\n""" % ((str(content['date_published']))[:10])

    else:
        html_date = ''

    # Adds author name if exist to the local html file
    if content['author'] != None:
        html_author = """<li>%s</li>\n"""%((content['author']))

    else:
        html_author = ''

    html_meta_info = """<ul class="article_source_date_author">\n%s%s%s</ul>\n\n"""%(html_site_name,html_date,html_author)
    output_to_return = '.'.join([output_to_return, html_meta_info])


    # Adds main article content to the local html file
    if (len(content['content'])!=0):
        # tree = html_text.parse_html(content['content'])
        # text = html_text.extract_text(tree)
        html_body = """<div class="smart_article_content"><!-- DIV CONTAINER FOR MAIN ARTICLE CONTENT -->\n%s\n</div> \n\n"""%(content['content'])
        output_to_return = '.'.join([output_to_return, html_body])

    html_close = """</body>\n</html>"""
    output_to_return = '.'.join([output_to_return, html_close])

    return output_to_return









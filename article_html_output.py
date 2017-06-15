import article_json_output
import tldextract


def article_output(url):

    content = article_json_output.article(url)

    output_to_return = ""

    #START WRITING THE HTML FILE
    html_open = """<html> \n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">\n<link rel="stylesheet" type="text/css" href="style.css">\n</head>\n<body>"""
    output_to_return = '.'.join([output_to_return, html_open])

    # WRITE THE TITILE TO LOCAL HTML FILE
    if content['Title'] != None:
        html_heading = """<div class="smart_article_title"><!-- DIV CONTAINER FOR TITLE -->\n<h1 align="center">%s</h1>\n</div> \n\n"""%(content['Title'])
        output_to_return = '.'.join([output_to_return, html_heading])

    else:
        html_heading = ''
        output_to_return = '.'.join([output_to_return, html_heading])

    # WRITE THE SOURCE WEBSITE TO LOCAL HTML FILE
    url_extract = tldextract.extract(url)
    site_name = url_extract.domain + '.' + url_extract.suffix
    if len(site_name)!=0:
        html_site_name = """<li>%s</li>\n"""%(site_name)

    else:
        html_site_name = ''


    # GET THE AUTHOR NAME
    if len(content['Authors'])>0:
        html_author = """<li>%s</li>\n"""%((content['Authors'])[0])

    else:
        html_author = ''


    # GET THE PUBLISHED DATE
    date_variable = (str(content['Publish_date']))[:10]

    if len(date_variable) > 9:
        html_date = """<li>%s</li>\n""" % (date_variable)

    else:
        html_date = ''

    # WRITING SOURCE WEBSITE, AUTHOR NAME AND PUBLISHED DATE TO LOCAL HTML FILE
    html_meta_info = """<ul class="article_source_date_author">\n%s%s%s</ul>\n\n""" % (html_site_name, html_date, html_author)
    output_to_return = '.'.join([output_to_return, html_meta_info])


    # GIVE TOP IMAGE URL TO LOCAL HTML FILE
    if(content['Top_img'] != None):
        html_img = """<img src="%s" target="_blank"></img> """%(content['Top_img'])
        output_to_return = '.'.join([output_to_return, html_img])

    else:
        pass

    if content['Text'] != None:
        html_body = """<div class="smart_article_content"><!-- DIV CONTAINER FOR MAIN ARTICLE CONTENT -->\n%s\n</div> \n\n"""%(content['Text'])
        output_to_return = '.'.join([output_to_return, html_body])

    html_close = """</body>\n</html>"""
    output_to_return = '.'.join([output_to_return, html_close])
    
    return output_to_return



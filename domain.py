from urllib.parse import urlparse

#Get domain name(example.com)
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        return results[-2]+'.'+results[-1]

    except:
        return ""    


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        #below statement provides the network location using .netloc function 
        return urlparse(url).netloc
    except:
        return ""

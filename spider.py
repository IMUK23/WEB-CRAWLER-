from link_finder import LinkFinder
from urllib.request import urlopen
from general import *
from domain import *


class Spider:
    #Class Variable That is Shared among all instances 
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue = set()
    crawled = set()

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file=Spider.project_name+'/queue.txt'
        Spider.crawled_file=Spider.project_name+'/crawled.txt'
        self.boot()
        self.crawl_page('First Spider',Spider.base_url)

    #This boot is a static method that is if it is defined outside the class then also it will remain same 
    
    def boot(self):
        create_folder(Spider.project_name)
        create_datafiles(Spider.project_name,Spider.base_url)

        Spider.queue=file_to_set(Spider.queue_file)
        Spider.crawled=file_to_set(Spider.crawled_file)
    
    #This is also a static Method
    @staticmethod
    def crawl_page(thread_name,page_url):    
        if page_url not in Spider.crawled:
            print(thread_name+"Now Crawling"+page_url)
            print('Queue'+str(len(Spider.queue))+"| Crawled"+ str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_Files()
           
    @staticmethod
    def gather_link(page_url):
        html_string=''
        try:
            response=urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes=response.read()
                html_string=html_bytes.decode('utf-8')
            Finder=LinkFinder(Spider.base_url,page_url)
            Finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return Finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_Files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)                







     


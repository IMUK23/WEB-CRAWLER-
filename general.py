import os

#For Every Crawling or Scraping A separate Folder will be created 

def create_folder(directory):
    if not os.path.exists(directory):
        print("Creating Project"+directory)
        os.makedirs(directory)

# Create Queue and Crawled File(if not created )
# Queue are those that are yet to be crawled
# crawled are those are the already read


def create_datafiles(project_name,base_url):
    queue=project_name + '/queue.txt'
    crawled=project_name+ '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')    

# Create a new  file 
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()
     

#Add data onto an existing file 
def append_to_file(path,data):
    with open(path,'a') as f:
        f.write(data+"\n")

#Delete the content of file 
def delete_file_content(path):
    with open(path,'w') as file:
        #do nothing
        pass  
    file.close()      

#converting the links in file to set by reading the file
def file_to_set(filename):
    results=set()
    with open(filename,'rt') as f:
        for line in f:
            
            #replace is a built in function which replaces first value with another value

            results.add(line.replace("\n","")) 
    return results

def set_to_file(links,file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

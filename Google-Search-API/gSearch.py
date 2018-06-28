from google import google
import itertools
import operator
import json
import pprint
import requests
import urllib


def listGen(filePath):
    keyList=[]
    file = open(filePath, 'r')
    for line in file:
        keyList.append(line.strip())
    file.close()
    return keyList


def extractKeys():

    k1 = listGen('keys/keys1.txt')
    k2 = listGen('keys/keys2.txt')
    k3 = listGen('keys/keys3.txt')
    k4 = listGen('keys/keys4.txt')
    k5 = listGen('keys/keys5.txt')

    keywords = []
    keywords.extend(itertools.product(k1, k2))
    keywords.extend(itertools.product(k1, k3))
    keywords.extend(itertools.product(k1, k4))

    print("Number of Search Terms:" + str(len(keywords)))
    #pprint.pprint(keywords)
    return keywords


def extractURLs():
    num_page = 1  # how many pages to consider while searching Google - each pages about 10 urls
    urlDict = {}
    keywords = extractKeys()
    
    for terms in keywords:
        print(terms)
        # define the keywords order
        search_results = google.search(terms[0] + " " + terms[1], num_page)
        i = 1
        for result in search_results:
            # to check if the link exists [ omit 404 errors ] 
            try:
                a = urllib.request.urlopen(result.link)
                if a.getcode()==200:
                    print(result.link)
                    '''
                    Keys are URLs
                    Values are of the form [x,Y] 
                        x = total number of times this URL has been hit
                        Y = list of URL google page ranks (the rank given by Google for each URL)
                    eg: 
                    {
                        "URL": [2, [4,2]]
                    }
                    '''
                    if result.link in urlDict.keys():
                        urlDict[str(result.link)][0] += 1
                        urlDict[str(result.link)][1].append(i)
                    else:
                        urlDict[str(result.link)] = [1, [i]]
                    i += 1
                    
            except:
                print("********LINK ERROR [", result.link,"]********")
    # sorting dict based on values
    urlDict = dict(sorted(urlDict.items(), key=operator.itemgetter(1), reverse=False))
    print("Total number of unique URLs:" + str(len(urlDict)))
    
    with open('top-urls2.json', 'w') as fp:
        json.dump(urlDict, fp, indent=4)
  
    topURLlist = open('topURLlist2.txt', 'w')
    for urls in urlDict:
        topURLlist.write(urls[0]+'\n')
    topURLlist.close()

    
if __name__ == "__main__":
    extractURLs()

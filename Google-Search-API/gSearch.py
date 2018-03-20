from google import google
import itertools
import operator
import json

def listGen(filePath):
    keyList=[]
    file = open(filePath, 'r')
    for line in file:
        keyList.append(line.strip())
    file.close()
    return keyList

k1 = listGen('/Users/simin/Google Drive/CS599-Simin/gSearching/Google-Search-API/keys/keys1.txt')
k2 = listGen('/Users/simin/Google Drive/CS599-Simin/gSearching/Google-Search-API/keys/keys2.txt')
k3 = listGen('/Users/simin/Google Drive/CS599-Simin/gSearching/Google-Search-API/keys/keys3.txt')
k4 = listGen('/Users/simin/Google Drive/CS599-Simin/gSearching/Google-Search-API/keys/keys4.txt')
k5 = listGen('/Users/simin/Google Drive/CS599-Simin/gSearching/Google-Search-API/keys/keys5.txt')

keywords=[]
# keywords.extend(k1)
# keywords.extend(k2)
# keywords.extend(k3)
# keywords.extend(k4)
keywords.extend(itertools.product(k1,k2))
keywords.extend(itertools.product(k1,k3))
keywords.extend(itertools.product(k1,k4))

print("Number of Search Terms:" + str(len(keywords)))
print (keywords)

num_page = 1 #how many pages to consider while searching Google - each pages about 10 urls

urlDict = {}
#urlList = []
for terms in keywords:
    print (terms)
    #here we define the keywords order
    search_results = google.search(terms[0] +" " + terms[1], num_page)
    #search_results = google.search(terms, num_page)
    i=1
    for result in search_results:
        #urlList.append(result.link)
        if result.link in urlDict.keys():
            urlDict[result.link][0]+=1
            urlDict[result.link][1].append(i)
        else:
            urlDict[result.link]=[1,[i]]
        i += 1
        print(result.link)
urlDict = sorted(urlDict.items(), key=operator.itemgetter(1), reverse=True)

#print("Total number of URLs:" + str(len(urlList)))
print("Total number of unique URLs:" + str(len(urlDict)))

with open('top-urls.json', 'w') as fp:
    json.dump(urlDict, fp)

topURLlist = open('topURLlist.txt', 'w')
for urls in urlDict:
    topURLlist.write(urls[0]+'\n')
topURLlist.close()

#print(urlDict)

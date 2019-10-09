import json

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def parseBusinessData():
    #read the JSON file
    with open('.\yelp_business.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('business.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['business_id'])+'\t') #business id
            outfile.write(cleanStr4SQL(data['name'])+'\t') #name
            outfile.write(cleanStr4SQL(data['address'])+'\t') #full_address
            outfile.write(cleanStr4SQL(data['state'])+'\t') #state
            outfile.write(cleanStr4SQL(data['city'])+'\t') #city
            outfile.write(cleanStr4SQL(data['postal_code']) + '\t')  #zipcode
            outfile.write(str(data['latitude'])+'\t') #latitude
            outfile.write(str(data['longitude'])+'\t') #longitude
            outfile.write(str(data['stars'])+'\t') #stars
            outfile.write(str(data['review_count'])+'\t') #reviewcount
            outfile.write(str(data['is_open'])+'\t') #openstatus
            outfile.write(str([item for item in  data['categories']])+'\t') #category list
            outfile.write(str([])) # write your own code to process attributes
            outfile.write(str([])) # write your own code to process hours
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

def parseUserData():
    #{"average_stars": 3.18, "cool": 0, "fans": 0, "friends": [], "funny": 1, "name": "A", "review_count": 10, "useful": 3, "user_id": "4WZ-RUk5akPl5_4-tqqygw", "yelping_since": "2012-07-05"}
    #read the JSON file
    with open('.\yelp_user.JSON','r') as f:  #Assumes that the data files are available in the current directory. If not, you should set the path for the yelp data files.
        outfile =  open('user.txt', 'w')
        line = f.readline()
        count_line = 0
        #read each JSON abject and extract data
        while line:
            data = json.loads(line)
            outfile.write(str(data['average_stars'])+'\t') 
            outfile.write(str(data['cool'])+'\t') 
            outfile.write(str(data['fans'])+'\t') 
            outfile.write(str([item for item in  data['friends']])+'\t')
            outfile.write(str(data['funny'])+'\t') 
            outfile.write(cleanStr4SQL(data['name']) + '\t')  
            outfile.write(str(data['review_count']) + '\t') 
            outfile.write(str(data['useful']) + '\t') 
            outfile.write(str(data['user_id']) + '\t') 
            outfile.write(str(data['yelping_since']) + '\t')
            outfile.write('\n')

            line = f.readline()
            count_line +=1
    print(count_line)
    outfile.close()
    f.close()

def parseCheckinData():
    #write code to parse yelp_checkin.JSON
    pass


def parseReviewData():
    #write code to parse yelp_review.JSON
    pass

#parseBusinessData()
parseUserData()
parseCheckinData()
parseReviewData()

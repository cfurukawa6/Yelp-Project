import json

def cleanStr4SQL (s):
    return s.replace("'","`").replace("\n"," ")

def parseReviewData ():

    with open('.\yelp_review.JSON','r') as f:
        outfile = open('review.txt', 'w') #opens new file to store parsed data
        line = f.readline()
        num_line = 0

        while line:
            data = json.loads(line)
            outfile.write(cleanStr4SQL(data['review_id']) + '\t') #writes review id and adds tab
            outfile.write(cleanStr4SQL(data['user_id']) + '\t') #user_id 
            outfile.write(cleanStr4SQL(data['business_id']) + '\t') #business
            outfile.write(str(data['stars']) + '\t') #stars
            outfile.write(cleanStr4SQL(data['date']) + '\t') #date
            outfile.write(cleanStr4SQL(data['text']) + '\t') #text
            outfile.write(str(data['useful']) + '\t')
            outfile.write(str(data['funny']) + '\t')
            outfile.write(str(data['cool']) + '\t')
            outfile.write('\n')
            
            line = f.readline()
            num_line += 1


    print(num_line)
    outfile.close()
    f.close()
        
parseReviewData()

from collections import defaultdict
import operator
from sets import Set

def jaccard_distance(l1, l2):
    ##TODO:Implement write jaccard distance function
    union = Set(l1).union(Set(l2))
    intersect = Set(l1).intersection(Set(l2))
    return len(intersect) / float(len(union))

# Load data
f = open('data/user-brands.csv')
brand_users = defaultdict(list)  # Given a brand, which users are followers
user_brands = defaultdict(list)  # Given a user, which brands does the user follow
for line in f:
    user, brand = line.strip().split(',', 1)
    brand_users[brand].append(user)
    user_brands[user].append(brand)


# Create similarity "matrix"
similarity = defaultdict(dict)  # Given two brands, what is the similarity score using Jaccard coefficient Number of people in the intersection / Number of people in the union
brand_list = brand_users.keys()
user_list = user_brands.keys()

for brand1, users1 in brand_users.items():
    for brand2, users2 in brand_users.items():
        ##TODO:Implement compute similarity between brands
        key = tuple(sorted((brand1,brand2)))
        if not key in similarity:
            similarity[key] = jaccard_distance(users1,users2)
        #OR similarity[brand1][brand2] = jaccard_distance(users1, users2)
#print similarity

def get_similar_brands(brand, threshold = 0):
    """Given a brand, return similar brands with scores"""
    brand_scores = defaultdict(int)
    ## TODO : Implement
    ## For all other brands
    ## Get the brands that have similarity > threshold
    for other_brand in brand_list:
        if other_brand != brand:
            #Set key as above
            key = tuple(sorted([brand, other_brand]))
            
            #Look up sim score for the pair
            sim = similarity[key]
            
            #If it passes threshold then save
            if sim > threshold:
                #add it to dict
                brand_scores[other_brand] = sim

    return brand_scores
    ## Return a list of (brand, similarity_score) pairs



def get_brand_recommendations_usingother(user):
    """Given a user, return recommended brands with scores, looking at all other brands than my own"""
    all_brand_scores = defaultdict(int)
    ##TODO: Implement
    ## Take the brands that this user likes
    ## Find similar brands to each brand this user likes
    ## Get total similarity to all other brands based on similarirt to each brand this user likes

    ## Return the top scoring brands by total similarity
    # for a user - all the brands w/ preference; how similar is this brand to teh other brands. 
    # List of brands liked. for each brand liked, how similar to other brands, save score. for second brand - add to likeness
    #Method 2
    for other_brand in brand_list:
        all_brand_scores[other_brand] = sum ( [similarity[tuple(sorted((brand, other_brand)))] for brand in user_brands[user] ])
        
    return sorted([(score, key) for (key, score) in all_brand_scores.items()], reverse=True)[:10]  

def get_brand_recommendations_usingmine(user):
    """Given a user, return recommended brands with scores, looking at my brands"""
    all_brand_scores = defaultdict(int)
    ##TODO: Implement
    ## Take the brands that this user likes
    ## Find similar brands to each brand this user likes
    ## Get total similarity to all other brands based on similarirt to each brand this user likes

    ## Return the top scoring brands by total similarity
    # for a user - all the brands w/ preference; how similar is this brand to teh other brands. 
    # List of brands liked. for each brand liked, how similar to other brands, save score. for second brand - add to likeness
    # for my brands get similar. for each similar, increment my rating by the score and log the same.
    # for all other brands sum(sim)
    #Method 1
    brands_liked = user_brands[user]
    for brands in brands_liked:
        brand_scores = get_similar_brands(brands, 0)
        for brand1, score in brand_scores.items():
            if brand1 not in brands_liked:
                all_brand_scores[brand1] += score
    return sorted(all_brand_scores.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]

 

user = '90217'
# user = '89112'
# user = '89116'
print "Current brands: {}".format(user_brands.get(user))
print "Recommendations:"
#print get_brand_recommendations_usingother(user)
print get_brand_recommendations_usingmine(user)

"""Optimizations:
1. Limit similarity scores to brands with at least __ followers
2. Filter recommendations via a score threshold
"""

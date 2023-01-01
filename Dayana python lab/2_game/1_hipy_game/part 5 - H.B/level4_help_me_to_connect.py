from instapy import InstaPy
from instapy import smart_run

user_name = "illegible_debian"
pass_word = "abdalbaliISnothere"

session = InstaPy(username= user_name, password= pass_word)


with smart_run(session= session):
    session.set_relationship_bounds(enabled= True, delimit_by_numbers= True,
                                    max_followers=500, min_followers= 50,min_following=50)
    
    session.set_do_follow(True, percentage=100)
    session.set_dont_like(['porn', 'murder', 'fact', 'butt'])
    session.set_do_like(['programming', 'AI', 'ml', 'python'])

    session.like_by_tags(['python', 'C#', 'PHP'], amount=15)
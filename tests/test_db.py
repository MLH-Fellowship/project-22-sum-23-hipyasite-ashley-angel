# test db. py

import unittest
from peewee import *
from playhouse.shortcuts import model_to_dict
import sys


from app import TimelinePost 
MODELS = [TimelinePost]
 # use an in-memorv SOLite for tests
test_db = SqliteDatabase(': memory: ')



class TestTimelinePost(unittest.TestCase):

    def setUp(self):

            test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)


            test_db. connect()


            test_db. create_tables (MODELS)

    def tearDown(self):

# Not strictly necessary since SOLite in-memory databases only live

# for the duration of the connection.

# the connection... but a good practice all the same

            test_db.drop_tables (MODELS)


# Close connection to db

            test_db.close()

    
    def test_timeline_post(self):

# Create 2 timeline posts
        first_post = TimelinePost.create(name='John Doe',
        email='john@example.com', content='Hello world, I\'m John!')
        second_post = TimelinePost.create(name='Jane Doe',
        email='jane@example.com', content='Hello world, I\'m Jane!')
        timeline_posts ={'timelineposts':[
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.asc())
        ]}
        John=((timeline_posts.get('timelineposts'))[0])
        Jane=((timeline_posts.get('timelineposts'))[1])
        assert John["id"]==1 and John["name"]=='John Doe' and John["email"]=='john@example.com' and John["content"]== 'Hello world, I\'m John!'
        assert Jane["id"]==2 and Jane["name"]=='Jane Doe' and Jane["email"]=='jane@example.com' and Jane["content"]== 'Hello world, I\'m Jane!'
#checks if timeline posts have been cleared

    def test_check(self):
        timeline_posts ={'timelineposts':[
                model_to_dict(p)
                for p in TimelinePost.select().order_by(TimelinePost.created_at.asc())
                                        ]}
        
        assert  not timeline_posts['timelineposts']


    
    

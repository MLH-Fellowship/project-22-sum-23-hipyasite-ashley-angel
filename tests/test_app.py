

import unittest 

import os
os. environ ['TESTING'] ='true'
import sys

from app import app


class AppTestCase(unittest.TestCase):

        def setUp(self):

            self.client = app. test_client()







        def test_home(self):
            response =self.client.get("/")
            assert response. status_code == 302
            html = response.get_data(as_text=True)
            assert "<title>Redirecting...</title>" in html
            response =self.client.get("/home")
            assert response. status_code == 200
            html = response.get_data(as_text=True)
            assert "<title>Nothing to see here</title>" in html






        def test_timeline( self):
            response = self.client.get("/api/timeline_post")
            assert response.status_code == 200
            assert response.is_json
            json = response.get_json()
            assert "timeline_posts" in json
            response = self.client.post("/api/new_post",data={"name":"Smrithi",'email':"test@test.com","content":"Hello World, I'm Smrithi."})
            response = self.client.get("/api/timeline_post")
            json = response.get_json()
            prev=len(json["timeline_posts"]) 
            assert  "Smrithi" in json ['timeline_posts'][0]['name']
            response=self.client.delete("/api/timeline_post",data={"name":"Smrithi"})
            assert response.status_code == 200
            response = self.client.get("/api/timeline_post")
            json = response.get_json()
            assert len(json["timeline_posts"]) == prev-1
            response = self.client.get("/timeline")
            assert response.status_code == 200


        def test_malformed_timeline_post(self):

            response=self.client.post("/api/new_post",data={"name":"John Doe",'email':"not-an-email","content":"Hello World, I'm John."})
            assert response.status_code==400
            html=response.get_data(as_text=True)
            assert "Invalid email" in html 


            #POST request missing name
            response=self.client.post("/api/new_post", data={"email":"john@example.com","content":"Hello, world. I'm John."})
            assert response.status_code==400
            html=response.get_data(as_text=True)
            assert "Invalid name" in html

            

            #POST request with empty content 
            response=self.client.post("/api/new_post",data={"name":"John Doe","email":"john@example.com"})
            assert response.status_code==400
            html=response.get_data(as_text=True)
            assert "Invalid content" in html

            
    

       
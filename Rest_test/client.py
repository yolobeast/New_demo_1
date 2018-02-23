############################################################
#Name : Sathi.Ranganathan
#Porject : SSH autnentication manager
#date : Feburay,22.2018
############################################################
import json
import urllib2
import unittest

class RestApiTest(unittest.TestCase):

    def setUp(self):

        self.POSTUrl = "http://jsonplaceholder.typicode.com/posts"
        self.COMMENTUrl = "http://jsonplaceholder.typicode.com/comments"

    def test_post_API_id(self):
        print("-------Test Case for Loading ID in POSTS-------")
        testurl=(self.POSTUrl+"/1")
        print testurl
        response=urllib2.urlopen(testurl)
        html=response.read()
        print(html)
        self.assertTrue("1" in html)

    def test_post_API_title(self):
        print("-------Test Case for Loading title in POST-------")
        testurl=(self.POSTUrl+"/1")
        print testurl
        response=urllib2.urlopen(testurl)
        html=response.read()
        print(html)
        json_data=json.loads(html)
        comment_id=json_data["title"]
        print("commnet_id:"+str(comment_id))
        self.assertTrue(comment_id == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit")

    def test_post_API_body(self):
        print("-------Test Case for Loading title in POSTS-------")
        testurl=(self.POSTUrl+"/1")
        print testurl
        response=urllib2.urlopen(testurl)
        html=response.read()
        print(html)
        json_data=json.loads(html)
        comment_id=json_data["body"]
        print("commnet_id:"+str(comment_id))
        self.assertTrue(comment_id == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto")

    def test_comment_API_id(self):
        print("-------Test Case for Loading ID in COMMENTS-------")
        testurl=(self.COMMENTUrl+"/1")
        print testurl
        response=urllib2.urlopen(testurl)
        html=response.read()
        print(html)
        json_data=json.loads(html)
        comment_id=json_data["id"]
        print("commnet_id:"+str(comment_id))
        self.assertTrue(comment_id == 1)

    def test_comment_API_name(self):
        print("-------Test Case for Loading name in COMMENTS-------")
        testurl=(self.COMMENTUrl+"/1")
        print testurl
        response=urllib2.urlopen(testurl)
        html=response.read()
        print(html)
        json_data=json.loads(html)
        comment_id=json_data["name"]
        print("commnet_id:"+str(comment_id))
        self.assertTrue(comment_id == "id labore ex et quam laborum")
    def tearDown(self):
        print "------- test is over -------"

if __name__ == "__main__":
    unittest.main()

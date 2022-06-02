import unittest
from umuzi_prospects_files.visitor import create_visitor, list_visitors , delete_visitor , visitor_details, update_visitor, delete_all
from datetime import datetime
from mongoengine import connect, disconnect, Document, StringField, DateTimeField
from unittest.main import main
from bson import ObjectId


from umuzi_prospects_files.umuzi_prospects import Visitor
disconnect()

connect('mongoenginetest', host='mongomock://localhost', port = 8081)

class TestVisitor(unittest.TestCase):
    def test_creating_visitor(self):
        create_visitor("Thavha", "25", "jack", "enrollment compain")
        first_visitor = Visitor.objects().first()
        assert first_visitor.visitor_name == "Thavha", "create_visitor function failed to create a visistor"

    def test_list_visitors(self):
        visitors_number = len(list_visitors())
        all_visitors = Visitor.objects()
        assert visitors_number == len(all_visitors), "list_visitor function failed to list all visitors"


    def test_visitor_details(self):
        create_visitor("Thavha_test", "25", "jack", "enrollment compain")
        visitor_id =Visitor.objects().first().id
        details_of_visitor = visitor_details(visitor_id)
        first_visitor = Visitor.objects().first()
        assert  first_visitor.visitor_name == details_of_visitor["name"], "visitor_details function did not retrieve the correct visitor details"
        assert  ObjectId(details_of_visitor["id"]) ==visitor_id, "visitor_details function did not retrieve the correct visitor details"


    def test_delete_visitor(self):
        create_visitor("Thavha", "25", "jack", "enrollment compain")
        visitor_id =Visitor.objects().first().id
        delete_visitor(visitor_id)
        all_visitors = Visitor.objects()
        assert len(list_visitors()) == len(all_visitors),"delete_visitor function did not delete a visistor"

    def test_update_visitor(self):
        create_visitor("Thavha", "25", "jack", "enrollment compain")
        visitor_id =Visitor.objects().first().id
        update_visitor(visitor_id, "thavha_updated","30")
        updated_visitor =  Visitor.objects(id=visitor_id).first()
        assert updated_visitor.visitor_name == "thavha_updated", "update_visitor function did not update"
        assert updated_visitor.visitor_age == "30", "update_visitor function did not update"


    def test_delete_all(self):
        create_visitor("Thavha", "25", "jack", "enrollment compain")
        create_visitor("Thavha_test", "25", "jack", "enrollment compain")
        create_visitor("Thavha_for delete", "25", "jack", "enrollment compain")
        delete_all()
        all_visitors = Visitor.objects()
        assert len(all_visitors) == 0 , "delete all function did not detele all the visitors"
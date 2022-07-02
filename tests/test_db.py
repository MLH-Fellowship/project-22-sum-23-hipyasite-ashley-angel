from unittest import TestCase
from peewee import SqliteDatabase
from app import TimelinePost

MODELS = [TimelinePost]

db = SqliteDatabase(":memory:")

class TestTimlinePost(TestCase):
    def setUp(self) -> None:
        db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        db.connect()
        db.create_tables(MODELS)

    def tearDown(self) -> None:
        db.drop_tables(MODELS)
        db.close()

    def test_timeline(self) -> None:
        saved_post_1 = TimelinePost.create(name="#", email="hi@ex.com", content="##")
        saved_post_2 = TimelinePost.create(name="#", email="hi@ex.com", content="##")

        assert saved_post_1.id == 1
        assert saved_post_2.id == 2

        post_count: int = TimelinePost.select().count()

        assert post_count == 2

        fetched_post_1: TimelinePost = TimelinePost.get_by_id(saved_post_1.id)
        fetched_post_2: TimelinePost = TimelinePost.get_by_id(saved_post_2.id)

        assert fetched_post_1.name == saved_post_1.name and fetched_post_1.id == saved_post_1.id
        assert fetched_post_2.name == saved_post_2.name and fetched_post_2.id == saved_post_2.id

        TimelinePost.delete_by_id(fetched_post_1.id)
        TimelinePost.delete_by_id(fetched_post_2.id)

        post_count: int = TimelinePost.select().count()

        assert post_count == 0


from .models import *
from decimal import Decimal


class Seeder:

    def __init__(self):
        self.chapter_name = []
        self.entry_name = []

    def append_chapters(self):

        pass

    def append_scope_entries(sef):
        pass

    def seed(self, id):

        a=0
        for i in self.chapter_name:
            chapter_name = i
            a =a +1
            scope        = Scope.objects.get(id=id)
            chapter      = Chapter( code=a ,chapter_name=chapter_name, scope=scope)
            chapter.save()


generator=Seeder()

class Getter:

    def __init__(self, scope, chapter):
        self.chapters_query = Chapter.objects.filter(scope=scope)
        self.entries_query  = Entry.objects.filter(chapter_name=chapter)

    def replicate_chapters(self):

        for obj in self.chapters_query:
            obj.scope = new_scope
            chapter = Chapter('obj')
            chapter.save()







        


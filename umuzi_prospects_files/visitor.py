from datetime import datetime
from umuzi_prospects_files.umuzi_prospects import Visitor


def create_visitor(
    visitor_name,
    visitor_age,
    name_of_the_assistor,
    comments,
    date_of_visit=datetime.now(),
    time_of_visit=f'{datetime.now().strftime("%H:%M:%S")}',
):
    visitor = Visitor(
        visitor_name=visitor_name,
        visitor_age=visitor_age,
        name_of_the_assistor=name_of_the_assistor,
        comments=comments,
        date_of_visit=date_of_visit,
        time_of_visit=time_of_visit,
    )
    visitor.save()
    return f"{visitor['visitor_name']} saved"


def list_visitors():

    list_visitor = []
    visitors = Visitor.objects()
    for visitor in visitors:
        list_visitor.append(f'name:{visitor["visitor_name"]}, id:{visitor["id"]}')

    return list_visitor


def delete_visitor(visitor_id):
    visitor = Visitor.objects(id=visitor_id)
    visitor.delete()


def visitor_details(visitor_id):
    details = {}
    visitor = Visitor.objects(id=visitor_id)
    for items in visitor:
        details["id"] = f"{items.id}"
        details["name"] = f"{items.visitor_name}"
        details["age"] = f"{items.visitor_age}"
        details["assistant"] = f"{items.name_of_the_assistor}"
        details["comments"] = f"{items.comments}"
        details["date"] = f"{items.date_of_visit}"
        details["time"] = f"{items.time_of_visit}"
    return details


def update_visitor(
    visitor_id, visitor_name="", visitor_age="", name_of_the_assistor="", comments=""
):

    visitor = Visitor.objects(id=visitor_id)
    if len(visitor_name) > 0:
        visitor.update(visitor_name=visitor_name)
    if visitor_age != "":
        visitor.update(visitor_age=visitor_age)
    if len(name_of_the_assistor) > 0:
        visitor.update(name_of_the_assistor=name_of_the_assistor)
    if len(comments) > 0:
        visitor.update(comments=comments)
    if (
        len(visitor_name) > 0
        or len(visitor_age) > 0
        or len(name_of_the_assistor) > 0
        or len(comments) > 0
    ):
        visitor.update(date_of_visit=f"{datetime.now()}")
        visitor.update(time_of_visit=f'{datetime.now().strftime("%H:%M:%S")}')
        return "visitor updated"
    return "no updates"


def delete_all():
    visitor = Visitor.objects()
    visitor.delete({})
    return f"deleted all visitors"


# print(create_visitor("visitor_thavha_mongo", "23", "name_of_the_assistor", "comments"))
# print(update_visitor("62925c6d3f627854d48c34a3","anza tsiwana"))
# update_visitor("62924ecc8589cb86fbc3ee58", "thavha","27","anza","ahuan servise")
# delete_visitor('62925c6d3f627854d48c34a9')
# print(list_visitors())
# print(visitor_details("62925de33d0a1bc949e8a4d6"))
# print(delete_all())
# print(list_visitors())

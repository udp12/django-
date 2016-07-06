# import logging as log
# import datetime
# from polls.models import Login,Contact,Address
#
#
#
# @classmethod
# def create(cls,data):
#     name=cls.__name__
#     obj= cls(**data)
#     obj.save()
#     return {'status':True ,'msg':'%s created successfully' % name.title()}
#
#
# def json(self):
#     data={}
#     for k in self.properties().keys():
#         value=getattr(self,k)
#         if isinstance(value,datetime):
#             data[k]=str(value)
#         else:
#             data[k] =value
#     return  data
"""
    models:This file stores alist of comments that have 
    been created by different users  (normal Users, Moderators and Admins)

    It contains a list of dictionaries that represent comments that have been created
    by each user

    field keys
        user_id     : is the comment creater's id
        comment_id  : is the id comment created
        comment     : is the details contained in the comment created
        parent      : is the id of the comment which is nesting the current comment
                     Default value is none if its anew comment with out a parent
                     (A reply to a comment made by the same or another user)
"""
comments =
[
    {
        'user_id'   :1,
        'comment_id':1,
        'comment'   :'First comment created by user 1,has no parent'
        'parent'    :'None'
    },
    {
        'user_id'   :1,
        'comment_id':2,
        'comment'   :'Second comment created by user 1,has no parent'
        'parent'    : 'None'
    },
    {
        'user_id'   :3,
        'comment_id':3,
        'comment'   :'First comment created by user 3 In reply to creator of comment 1'
        'parent'    :1
    },
    {
        'user_id'   :2,
        'comment_id':4,
        'comment'   :'First comment created by user 2 in reply to creator of comment 1'
        'parent'    :1
    },
    {
        'user_id'   :1,
        'comment_id':5,
        'comment'   :'Hello this how we are doing things also in reply to creator of comment 1'
        'parent'    :1
    },
    {
        'user_id'   :1,
        'comment_id':6
        'comment'   :'Third comment created by user 1 in reply to creator of comment 4'
        'parent'    :4
    },
    {
        'user_id'   :3,
        'comment_id':7
        'comment'   :'Second comment created by user 3 and has no parent'
        'parent'    :1
    }
]
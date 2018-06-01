# New comment is a dictionary
# Comments is a list
def add_comment(body, author):
    id = len(comments) + 1
    new_comment = comment(id, 'body', 'author')
    comments.append(new_comment)

def reply_comment(id, body, author):
    reply = reply_comment(body, author)
    for replies in comments:
        if replies['comment_id'] == id:
            replies.append({'reply':reply.body, 'author':reply.author})
        else:
            print "Invalid id"
def edit_comment(id, comment_body, author):
    edit_comment = comment(id, 'body', 'author')
    for edits in comments:
        if edits['comment_id'] == id: 
            edits[id] = edit_comment
            print edit_comment[id] 
        else:
            print ('Invalid id selected')

def delete_comment(id, comment_body, author):
    delete_comment = comment(id, 'body', 'author')
    for deletes in comments:
        if deletes['comment_id'] == id: 
            deletes[id] = delete_comment
            print delete_comment[id] 
        else:
            print ('Invalid id selected')

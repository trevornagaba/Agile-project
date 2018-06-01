user_name = raw_input('Please enter your username: ') 
user_type = raw_input('Hello {}, what type of user are you? :'.format(user_name))

if user_type == user_type.lower('user'):
    comment = raw_input('Enter new comment here: ')
    add_comment()
    edt_comment = raw_input('If you want to edit a comment, please the comment id here: ')
    edit_comment()



elif user_type == user_type.lower('moderator'):
    comment = raw_input('Enter new comment here: ')
    add_comment()
    del_comment = raw_input('If you want to delete a comment, enter the comment id here: ')
    delete_comment()
    edt_comment = raw_input('If you want to edit a comment, please the comment id here: ')
    edit_comment()




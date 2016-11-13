"""praw constants."""

__version__ = '4.0.0b21'

API_PATH = {
    'about_edited':           'r/{subreddit}/about/edited/',
    'about_log':              'r/{subreddit}/about/log/',
    'about_modqueue':         'r/{subreddit}/about/modqueue/',
    'about_reports':          'r/{subreddit}/about/reports/',
    'about_spam':             'r/{subreddit}/about/spam/',
    'about_sticky':           'r/{subreddit}/about/sticky/',
    'about_stylesheet':       'r/{subreddit}/about/stylesheet/',
    'about_traffic':          'r/{subreddit}/about/traffic/',
    'about_unmoderated':      'r/{subreddit}/about/unmoderated/',
    'accept_mod_invite':      'r/{subreddit}/api/accept_moderator_invite',
    'approve':                'api/approve/',
    'block':                  'api/block',
    'blocked':                'prefs/blocked/',
    'by_id':                  'by_id/',
    'captcha':                'captcha/',
    'comment':                'api/comment/',
    'comment_replies':        'message/comments/',
    'compose':                'api/compose/',
    'contest_mode':           'api/set_contest_mode/',
    'del':                    'api/del/',
    'deleteflair':            'api/deleteflair',
    'delete_sr_header':       'r/{subreddit}/api/delete_sr_header',
    'delete_sr_image':        'r/{subreddit}/api/delete_sr_img',
    'distinguish':            'api/distinguish/',
    'domain':                 'domain/{domain}/',
    'duplicates':             'duplicates/{submission_id}/',
    'edit':                   'api/editusertext/',
    'flair':                  'r/{subreddit}/api/flair/',
    'flairconfig':            'api/flairconfig/',
    'flaircsv':               'r/{subreddit}/api/flaircsv/',
    'flairlist':              'r/{subreddit}/api/flairlist/',
    'flairselector':          'r/{subreddit}/api/flairselector/',
    'flairtemplate':          'r/{subreddit}/api/flairtemplate/',
    'flairtemplateclear':     'r/{subreddit}/api/clearflairtemplates/',
    'flairtemplatedelete':    'r/{subreddit}/api/deleteflairtemplate/',
    'friend':                 'api/friend/',
    'friend_v1':              'api/v1/me/friends/{user}',
    'friends':                'api/v1/me/friends/',
    'gild_thing':             'api/v1/gold/gild/{fullname}/',
    'gild_user':              'api/v1/gold/give/{username}/',
    'help':                   'help/',
    'hide':                   'api/hide/',
    'ignore_reports':         'api/ignore_reports/',
    'inbox':                  'message/inbox/',
    'info':                   'api/info/',
    'karma':                  'api/v1/me/karma',
    'leavecontributor':       'api/leavecontributor',
    'leavemoderator':         'api/leavemoderator',
    'list_banned':            'r/{subreddit}/about/banned/',
    'list_contributor':       'r/{subreddit}/about/contributors/',
    'list_moderator':         'r/{subreddit}/about/moderators/',
    'list_muted':             'r/{subreddit}/about/muted/',
    'list_wikibanned':        'r/{subreddit}/about/wikibanned/',
    'list_wikicontributor':   'r/{subreddit}/about/wikicontributors/',
    'liveabout':              'api/live/{id}/about/',
    'livecreate':             'api/live/create',
    'lock':                   'api/lock/',
    'me':                     'api/v1/me',
    'mentions':               'message/mentions',
    'message':                'message/messages/{messageid}/',
    'messages':               'message/messages/',
    'moderator_messages':     'r/{subreddit}/message/moderator/',
    'moderator_unread':       'r/{subreddit}/message/moderator/unread/',
    'morechildren':           'api/morechildren/',
    'my_contributor':         'subreddits/mine/contributor/',
    'my_moderator':           'subreddits/mine/moderator/',
    'my_multireddits':        'api/multi/mine/',
    'my_subreddits':          'subreddits/mine/subscriber/',
    'marknsfw':               'api/marknsfw/',
    'multireddit':            'user/{user}/m/{multi}/',
    'multireddit_api':        'api/multi/user/{user}/m/{multi}/',
    'multireddit_base':       'api/multi/',
    'multireddit_copy':       'api/multi/copy/',
    'multireddit_rename':     'api/multi/rename/',
    'multireddit_update':     'api/multi/user/{user}/m/{multi}/r/{subreddit}',
    'multireddit_user':       'api/multi/user/{user}/',
    'mute_sender':            'api/mute_message_author/',
    'read_message':           'api/read_message/',
    'remove':                 'api/remove/',
    'report':                 'api/report/',
    'save':                   'api/save/',
    'search':                 'r/{subreddit}/search/',
    'select_flair':           'r/{subreddit}/api/selectflair/',
    'sent':                   'message/sent/',
    'sticky_submission':      'api/set_subreddit_sticky/',
    'site_admin':             'api/site_admin/',
    'sub_recommendations':    'api/recommend/sr/{subreddits}',
    'submission':             'comments/{id}/',
    'submission_replies':     'message/selfreply/',
    'submit':                 'api/submit/',
    'subreddit':              'r/{subreddit}/',
    'subreddit_about':        'r/{subreddit}/about/',
    'subreddit_css':          'api/subreddit_stylesheet/',
    'subreddit_random':       'r/{subreddit}/random/',
    'subreddit_settings':     'r/{subreddit}/about/edit/',
    'subreddits_default':     'subreddits/default/',
    'subreddits_gold':        'subreddits/gold/',
    'subreddits_new':         'subreddits/new/',
    'subreddits_popular':     'subreddits/popular/',
    'subreddits_name_search': 'api/search_reddit_names/',
    'subreddits_search':      'subreddits/search/',
    'subscribe':              'api/subscribe/',
    'suggested_sort':         'api/set_suggested_sort/',
    'unfriend':               'api/unfriend/',
    'unhide':                 'api/unhide/',
    'unignore_reports':       'api/unignore_reports/',
    'unlock':                 'api/unlock/',
    'unmarknsfw':             'api/unmarknsfw/',
    'unmute_sender':          'api/unmute_message_author/',
    'unread':                 'message/unread/',
    'unread_message':         'api/unread_message/',
    'unsave':                 'api/unsave/',
    'upload_image':           'api/upload_sr_img',
    'user':                   'user/{user}/',
    'user_about':             'user/{user}/about/',
    'username_available':     'api/username_available/',
    'vote':                   'api/vote/',
    'wiki_edit':              'r/{subreddit}/api/wiki/edit/',
    'wiki_page':              'r/{subreddit}/wiki/{page}',
    'wiki_page_editor':       'r/{subreddit}/api/wiki/alloweditor/{method}',
    'wiki_page_settings':     'r/{subreddit}/wiki/settings/{page}',
    'wiki_pages':             'r/{subreddit}/wiki/pages/'}

JPEG_HEADER = b'\xff\xd8\xff'
MAX_IMAGE_SIZE = 512000
MIN_PNG_SIZE = 67
MIN_JPEG_SIZE = 128
PNG_HEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

USER_AGENT_FORMAT = '{{}} PRAW/{}'.format(__version__)

import time
import requests
import re
import json
import hashlib
import os
import random

from slugify import slugify
from .session_manager import CookieSessionManager
from .exception.instagram_auth_exception import InstagramAuthException
from .exception.instagram_exception import InstagramException
from .exception.instagram_not_found_exception import InstagramNotFoundException
from .model.account import Account
from .model.comment import Comment
from .model.location import Location
from .model.media import Media
from .model.story import Story
from .model.user_stories import UserStories



class Instagram:
    HTTP_NOT_FOUND = 404
    HTTP_OK = 200
    HTTP_FORBIDDEN = 403
    HTTP_BAD_REQUEST = 400

    MAX_COMMENTS_PER_REQUEST = 300
    MAX_LIKES_PER_REQUEST = 50
    # 30 mins time limit on operations that require multiple self.__req
    PAGING_TIME_LIMIT_SEC = 1800
    PAGING_DELAY_MINIMUM_MICROSEC = 1000000  # 1 sec min delay to simulate browser
    PAGING_DELAY_MAXIMUM_MICROSEC = 3000000  # 3 sec max delay to simulate browser

    instance_cache = None

    def get_stories(self, reel_ids=None):
        """
        :param reel_ids: reel ids
        :return: UserStories List
        """
        variables = {'precomposed_overlay': False, 'reel_ids': []}

        if reel_ids is None or len(reel_ids) == 0:
            time.sleep(self.sleep_between_requests)
            response = self.__req.get(endpoints.get_user_stories_link(),
                                      headers=self.generate_headers(
                                          self.user_session))

            if not Instagram.HTTP_OK == response.status_code:
                raise InstagramException.default(response.text,
                                                 response.status_code)

            json_response = response.json()

            try:
                edges = json_response['data']['user']['feed_reels_tray'][
                    'edge_reels_tray_to_reel']['edges']
            except KeyError:
                return []

            for edge in edges:
                variables['reel_ids'].append(edge['node']['id'])

        else:
            variables['reel_ids'] = reel_ids

        time.sleep(self.sleep_between_requests)
        response = self.__req.get(endpoints.get_stories_link(variables),
                                  headers=self.generate_headers(
                                      self.user_session))

        if not Instagram.HTTP_OK == response.status_code:
            raise InstagramException.default(response.text,
                                             response.status_code)

        json_response = response.json()

        try:
            reels_media = json_response['data']['reels_media']
            if len(reels_media) == 0:
                return []
        except KeyError:
            return []

        stories = []
        for user in reels_media:
            user_stories = UserStories()

            user_stories.owner = Account(user['user'])
            for item in user['items']:
                story = Story(item)
                user_stories.stories.append(story)

            stories.append(user_stories)
        return stories
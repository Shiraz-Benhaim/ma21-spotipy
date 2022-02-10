import spotipy
from spotipy import UserPermissions


class SearchRequests:
    def __init__(self, user_permission: UserPermissions):
        self.__data = spotipy.info
        self.search_limit = user_permission.SEARCH_RESULTS_LIMIT

    def search_any_request(self, func, *args):
        def inner():
            return func(*args)

        try:
            result = inner()
            return result if self.search_limit is None or self.search_limit >= len(result) \
                else result[:self.search_limit]
        except Exception as e:
            spotipy.log.info(f"Search failed because of bad input to search")
            raise e

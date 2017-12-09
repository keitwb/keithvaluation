from django.core.cache import cache


def cache_page(timeout=60*15):
    def _cache_key(path):
        return '_page_cache_%s' % path

    def wrap(func):
        def view(request, *args, **kwargs):
            # Skip caching altogether if there are query args
            if len(request.GET) > 0:
                return func(request, *args, **kwargs)

            cache_key = '_page_cache_%s' % request.path
            stored = cache.get(cache_key)
            if stored:
                return stored
            else:
                resp = func(request, *args, **kwargs)
                if hasattr(resp, 'render') and callable(resp.render):
                    resp.add_post_render_callback(
                        lambda r: cache.set(cache_key, r, timeout)
                    )
                else:
                    cache.set(cache_key, resp, timeout)
                return resp
        return view
    return wrap

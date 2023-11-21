from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import render, redirect

from apps.utils.helpers.fetch import fetch


BASE_URL = "http://localhost:3000"


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


index = IndexView.as_view()


class ClearView(View):
    def get(self, request):
        request.session.flush()
        return redirect("index")


clear = ClearView.as_view()


class SearchView(View):
    def get_current_page(self, results):
        return int(results.get("currentPage")) if results else int(1)

    def get_attrs(self, request):
        return (
            request.GET.get("query"),
            int(request.GET.get("page", 1)),
            request.GET.get("provider", ""),
        )

    def get_result(self, request):
        return (
            request.get_search_query(),
            request.get_search_results(),
            request.get_provider(),
        )

    def process(self, request, query, provider, page):
        url = f"{BASE_URL}/{provider}/{query}?page={page}"

        results = fetch(request, url)

        if results and results is not None:
            self.set_result(request, query, results, provider)
        else:
            self.set_result(request, "", {}, "")

    def set_result(self, request, query, results, provider):
        request.set_search_query(query)
        request.set_search_results(results)
        request.set_provider(provider)

    def get(self, request):
        query, page, provider = self.get_attrs(request)
        search_query, search_results, search_provider = self.get_result(request)

        if (
            not search_results
            or search_query != query
            or page != self.get_current_page(search_results)
            or search_provider != provider
        ):
            self.process(request, query, provider, page)

        if (
            not request.get_search_results
            or not request.get_search_query
            or not request.get_provider()
        ):
            return redirect(to="index")
        return render(request, "search.html")


search = SearchView.as_view()


class DetailsView(View):
    def get_attrs(self, request):
        return request.GET.get("id")

    def get_result(self, request):
        return request.get_id(), request.get_details(), request.get_provider()

    def process(self, request, details, id):
        _id = details.pop("id", "")
        item_id = id if id else _id

        if "episodes" in details:
            items = details.pop("episodes", [])
            items = [item for item in items if item.get("id")]
            items = sorted(items, key=lambda x: x.get("number", ""))

        elif "chapters" in details:
            items = details.pop("chapters", [])
            items = [item for item in items if item.get("pages")]

            items = sorted(
                items,
                key=lambda x: float(x.get("chapterNumber", 0))
                if x.get("chapterNumber")
                else 0,
            )

        item = items[0] if items else {}

        now_playing = item.get("id", "")

        self.set_result(request, item_id, details, items, item, now_playing)

    def set_result(self, request, id, details, items, item, now_playing):
        request.set_id(id)
        request.set_details(details)
        request.set_items(items)
        request.set_item(item)
        request.set_now_playing(now_playing)
        request.set_links({})

    def get(self, request):
        id = self.get_attrs(request)
        item_id, item_details, provider = self.get_result(request)

        if not item_details or item_id != id:
            url = f"{BASE_URL}/{provider}/info/{id}"
            details = fetch(request, url)

            if details:
                self.process(request, details, id)

            else:
                self.set_result(request, "", {}, [], {}, "")
                return redirect(to="index")
        return render(request, "details.html")


details = DetailsView.as_view()


class PopularView(View):
    def get_current_page(self, results):
        return int(results.get("currentPage")) if results else int(1)

    def get_attrs(self, request):
        return int(request.GET.get("page", 1))

    def get_result(self, request):
        return request.get_popular()

    def process(self, request, page):
        url = f"{BASE_URL}/anilist/popular?page={page}"
        results = fetch(request, url)

        if results and results is not None:
            self.set_result(request, results)
        else:
            self.set_result(request, {})

    def set_result(self, request, results):
        request.set_popular(results)

    def get(self, request):
        page = self.get_attrs(request)
        results = self.get_result(request)

        current_page = self.get_current_page(results)

        if not results or page != current_page:
            self.process(request, page)

        if not request.get_popular():
            return redirect(to="index")

        return render(request, "popular.html")


popular = PopularView.as_view()


class RecentView(View):
    def get_current_page(self, results):
        return int(results.get("currentPage")) if results else int(1)

    def get_attrs(self, request):
        return int(request.GET.get("page", 1))

    def get_result(self, request):
        return request.get_recent()

    def process(self, request, page):
        url = f"{BASE_URL}/gogoanime/recent-episodes?page={page}"
        results = fetch(request, url)

        if results and results is not None:
            self.set_result(request, results)
        else:
            self.set_result(request, {})

    def set_result(self, request, results):
        request.set_recent(results)

    def get(self, request):
        page = self.get_attrs(request)
        results = self.get_result(request)

        current_page = self.get_current_page(results)

        if not results or page != current_page:
            self.process(request, page)

        if not request.get_recent():
            return redirect(to="index")

        return render(request, "recent.html")


recent = RecentView.as_view()


class TopView(View):
    def get_current_page(self, results):
        return int(results.get("currentPage")) if results else int(1)

    def get_attrs(self, request):
        return int(request.GET.get("page", 1))

    def get_result(self, request):
        return request.get_top()

    def process(self, request, page):
        url = f"{BASE_URL}/gogoanime/top-airing?page={page}"
        results = fetch(request, url)

        if results and results is not None:
            self.set_result(request, results)
        else:
            self.set_result(request, {})

    def set_result(self, request, results):
        request.set_top(results)

    def get(self, request):
        page = self.get_attrs(request)
        results = self.get_result(request)

        current_page = self.get_current_page(results)

        if not results or page != current_page:
            self.process(request, page)

        if not request.get_top():
            return redirect(to="index")

        return render(request, "top.html")


top = TopView.as_view()


class TrendingView(View):
    def get_current_page(self, results):
        return int(results.get("currentPage")) if results else int(1)

    def get_attrs(self, request):
        return int(request.GET.get("page", 1))

    def get_result(self, request):
        return request.get_trending()

    def process(self, request, page):
        url = f"{BASE_URL}/anilist/trending?page={page}"
        results = fetch(request, url)

        if results and results is not None:
            self.set_result(request, results)
        else:
            self.set_result(request, {})

    def set_result(self, request, results):
        request.set_trending(results)

    def get(self, request):
        page = self.get_attrs(request)
        results = self.get_result(request)

        current_page = self.get_current_page(results)

        if not results or page != current_page:
            self.process(request, page)

        if not request.get_trending():
            return redirect(to="index")

        return render(request, "trending.html")


trending = TrendingView.as_view()


class WatchView(View):
    def get_action(self, request):
        return "read" if request.get_provider() == "mangadex" else "watch"

    def get_attrs(self, request):
        return request.GET.get("id")

    def get_context(self, request):
        items = request.get_items()
        now_playing = request.get_now_playing()

        current_episode = next(
            (index for index, item in enumerate(items) if item["id"] == now_playing),
            None,
        )

        previous_episode = (
            items[current_episode - 1]
            if items and current_episode is not None and current_episode > 0 and items
            else None
        )

        next_episode = (
            items[current_episode + 1]
            if items
            and current_episode is not None
            and current_episode < len(items) - 1
            and items
            else None
        )

        request.set_next(next_episode)
        request.set_previous(previous_episode)

    def get_data(self, request):
        return (
            request.get_now_playing(),
            request.get_provider(),
        )

    def get_links(self, request, action):
        now_playing, provider = self.get_data(request)

        url = f"{BASE_URL}/{provider}/{action}/{now_playing}"

        links = fetch(request, url)

        if links is not None and links:
            request.set_links(links)
        else:
            request.set_links({})

        self.get_context(request)

    def get(self, request):
        id = self.get_attrs(request)
        action = self.get_action(request)

        items = request.get_items()
        links = request.get_links()
        now_playing = request.get_now_playing()

        if items and not links:
            self.get_links(request, action)

        elif id != now_playing and items:
            current = next(
                (item for item in items if item["id"] == id),
                None,
            )
            if current:
                request.set_item(current)
                request.set_now_playing(current.get("id", ""))

                if request.get_item() and request.get_now_playing():
                    self.get_links(request, action)

        if not request.get_links():
            return redirect(to="index")

        return render(request, f"{action}.html")


watch = login_required(WatchView.as_view())


class WatchEpisodeView(View):
    def get_attrs(self, request):
        return request.GET.get("id")

    def get(self, request):
        id = self.get_attrs(request)

        url = f"{BASE_URL}/gogoanime/watch/{id}"

        links = fetch(request, url)

        if links is not None and links:
            request.set_links(links)
        else:
            request.set_links({})

        if not request.get_links():
            return redirect(to="index")

        return render(request, "watch.html")


watch_episode = login_required(WatchEpisodeView.as_view())

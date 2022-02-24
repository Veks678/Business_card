from django.urls import path, include

routes = [
    {'url': '', 'app': 'news'},
    {'url': 'resume', 'app': 'resume'},
    {'url': 'projects', 'app': 'projects'},
    {'url': 'blog', 'app': 'blog'}
]
urlpatterns = [
    path(route['url'], include(f'apps.{route["app"]}.urls'))
    for route in routes
]

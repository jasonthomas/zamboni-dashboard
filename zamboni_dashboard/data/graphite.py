graphs = (
    ['All Responses', ['target=sumSeries({{ ns }}.response.*)&target={{ ns }}.response.200&target={{ ns }}.response.301&target={{ ns }}.response.302&target={{ ns }}.response.403&target={{ ns }}.response.404&target={{ ns }}.response.405&target={{ ns }}.response.500']],
    ['Site performance', ['target=stats.timers.{{ site }}.view.GET.lower&target=stats.timers.{{ site }}.view.GET.mean&target=stats.timers.{{ site }}.view.GET.upper_90']],
    ['Redirects and Errors', ['target={{ ns }}.response.301&target={{ ns }}.response.302&target={{ ns }}.response.304&target={{ ns }}.response.400&target={{ ns }}.response.403&target={{ ns }}.response.404&target={{ ns }}.response.405&target={{ ns }}.response.500&target={{ ns }}.response.503']],
    ['Celery', ['target=sumSeries({{ site }}.celery.tasks.pending.*.*.*)&target=nonNegativeDerivative(sumSeries({{ site }}.celery.tasks.total.*.*.*))&target=nonNegativeDerivative(sumSeries({{ site }}.celery.tasks.failed.*.*.*))']],
    ['Validation', ['target=stats.timers.{{ site }}.devhub.validator.lower&target=stats.timers.{{ site }}.devhub.validator.mean&target=stats.timers.{{ site }}.devhub.validator.upper_90']],
    ['GUID Search', ['target=stats.timers.{{ site }}.view.api.views.guid_search.GET.lower&target=stats.timers.{{ site }}.view.api.views.guid_search.GET.mean&target=stats.timers.{{ site }}.view.api.views.guid_search.GET.upper_90&target=scale(stats.timers.{{ site }}.view.api.views.guid_search.GET.count(0.01)']],
    ['GUI Search Counts', ['target=scale(stats.timers.{{ site }}.view.api.views.guid_search.GET.count,0.1)']],
    ['Update', ['target=stats.timers.{{ site }}.services.update.lower&target=stats.timers.{{ site }}.services.update.mean&target=stats.timers.{{ site }}.services.update.upper_90&target=scale(stats.timers.{{ site }}.services.update.count(0.01)']],
    ['Verify', ['target=stats.timers.{{ site }}.services.verify.lower&target=stats.timers.{{ site }}.services.verify.mean&target=stats.timers.{{ site }}.services.verify.upper_90&target=scale(stats.timers.{{ site }}.services.verify.count(0.01)']],
    ['Homepage', ['target=stats.timers.{{ site }}.view.addons.views.home.GET.lower&target=stats.timers.{{ site }}.view.addons.views.home.GET.mean&target=stats.timers.{{ site }}.view.addons.views.home.GET.upper_90&target=scale(stats.timers.{{ site }}.view.addons.views.home.GET.count,0.1)']],
    ['Search', ['target=stats.timers.{{ site }}.view.search.views.search.GET.lower&target=stats.timers.{{ site }}.view.search.views.search.GET.mean&target=stats.timers.{{ site }}.view.search.views.search.GET.upper_90&target=scale(stats.timers.{{ site }}.view.search.views.search.GET.count,0.1)']],
    ['ES Request', ['target=stats.timers.{{ site }}.search.es.took.lower&target=stats.timers.{{ site }}.search.es.took.mean&target=stats.timers.{{ site }}.search.es.took.upper_90&target=scale(stats.timers.{{ site }}.search.es.took.count%2C0.1)']],
    ['Authenticated Responses', ['target=stats.{{ site }}.response.auth.200&target=scale(stats.{{ site }}.response.200%2C0.1)&from=-1hours']],
    ['Marketplace', ['target=stats.timers.{{ site }}.paypal.paykey.retrieval.upper_90']],
    ['Client', ['target=stats.timers.{{ site }}.window.performance.timing.domInteractive.mean'
                '&target=stats.timers.{{ site }}.window.performance.timing.domInteractive.upper_90'
                '&target=stats.timers.{{ site }}.window.performance.timing.domComplete.mean'
                '&target=stats.timers.{{ site }}.window.performance.timing.domComplete.upper_90'
                '&target=stats.timers.{{ site }}.window.performance.timing.domLoading.mean'
                '&target=stats.timers.{{ site }}.window.performance.timing.domLoading.upper_90']],
    ['Client Counts', ['target=stats.{{ site }}.window.performance.navigation.redirectCountstats'
                '&target=stats.{{ site }}.window.performance.navigation.type.back_forward'
                '&target=stats.{{ site }}.window.performance.navigation.type.navigate'
                '&target=stats.{{ site }}.window.performance.navigation.type.reload'
                '&target=stats.{{ site }}.window.performance.navigation.type.reserved']],
    ['Client Fragment', ['target=stats.timers.{{ site }}.window.performance.timing.fragment.loaded.upper_90',
                '&target=stats.timers.{{ site }}.window.performance.timing.fragment.loaded.mean']],
    ['Error Counts', ['target=sumSeries(stats.{{ site }}.error.*)'
                      '&target=stats.{{ site }}.error.operationalerror']],
    ['Validator', ['target={{ site }}.celery.tasks.total.devhub.tasks.validator'
                   '&target={{ site }}.celery.tasks.failed.devhub.tasks.validator'
                   '&target={{ site }}.celery.tasks.pending.devhub.tasks.validator']],
    ['Signing', ['target=stats.timers.{{ site }}.services.sign.upper_90',
                 '&target=stats.timers.{{ site }}.services.sign.count']],
)

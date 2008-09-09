from dozer.leak import Dozer
from dozer.profile import Profiler

def dozer_filter_factory(global_conf, **kwargs):
    def filter(app):
        return Dozer(app, global_conf, **kwargs)
    return filter


def dozer_filter_app_factory(app, global_conf, **kwargs):
    return Dozer(app, global_conf, **kwargs)

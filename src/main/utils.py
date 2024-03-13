from flask import abort


def class_route(self, rule, endpoint, **options):
    def decorator(cls):
        self.add_url_rule(rule, view_func=cls.as_view(endpoint), **options)
        return cls

    return decorator

def dado_foi_deletado(dado):
    if dado is None or dado.data_deletado is not None:
        abort(404)

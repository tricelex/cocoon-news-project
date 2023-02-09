from rest_framework.exceptions import NotFound


class GetObjectMixin(object):
    @staticmethod
    def get_object_by_model(model, id) -> object:
        try:
            obj = model.objects.get(id=id)
        except model.DoesNotExist as e:
            raise NotFound(f'Object not found with params {id} on model {model.__name__}') from e

        return obj

    @staticmethod
    def get_related_object_by_model(model, id, related_field) -> object:
        try:
            obj = model.objects.select_related(related_field).get(id=id)
        except model.DoesNotExist as e:
            raise NotFound(f'Object not found with params {id} on model {model.__name__}') from e

        return getattr(obj, related_field)

# -*- coding: utf-8 -*-
from djangorestframework_camel_case2.settings import api_settings
from djangorestframework_camel_case2.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    def render(self, data, *args, **kwargs):
        return super(CamelCaseJSONRenderer, self).render(camelize(data), *args,
                                                         **kwargs)

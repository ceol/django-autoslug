# -*- coding: utf-8 -*-

from django.db.models.fields import CharField

from autoslug.utils import slugify

class AutoSlugField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 255)

        self._populate_from = kwargs.pop('populate_from', None)
        if self._populate_from:
            kwargs.setdefault('editable', False)

        self._separator = kwargs.pop('separator', '-')

        self._always_update = kwargs.pop('always_update', False)

        self._slugify = kwargs.pop('slugify', slugify)

        if 'db_index' not in kwargs:
            kwargs['db_index'] = True

        if 'unique' not in kwargs:
            kwargs['unique'] = True

        super(AutoSlugField, self).__init__(*args, **kwargs)

    def pre_save(self, instance, add):
        """Return a proper slug.

        This first checks to make sure the slug should be set, and if
        so, loops through the populate_from fields.
        """
        current_slug = self.value_from_object(instance)

        # only update the slug when always_update is true or if
        # there isn't a slug set.
        if not self._populate_from or (not self._always_update and current_slug):
            return current_slug

        parts = []

        for attr in self._populate_from:
            try:
                part = self._slugify(attr(instance), self._separator)
            except TypeError:
                part = self._slugify(getattr(instance, attr), self._separator)
            parts.append(part)

        new_slug = self._separator.join(parts)
        setattr(instance, self.name, new_slug)

        return new_slug
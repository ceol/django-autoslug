# django-autoslug

Automatic slugification of models.

## Description

django-autoslug is a signal-like application that automatically creates unique, URL- and SEO-friendly slugs on Django models. Default slugs replace spaces and URL-unfriendly characters with dashes, e.g. "My Awesome 'Model'!" becomes `my-awesome-model`. Apostrophes are not replaced and are instead stripped, e.g. "Mom's Recipe" becomes `moms-recipe`. Unicode letters are left alone, since most modern browsers display them accurately, e.g. "Gaudí's lizard" becomes `gaudís-lizard`. Each field is wrapped to the 40th character broken by word, e.g. "And I would have gotten away with it, too!" becomes `and-i-would-have-gotten-away-with-it`.

## Requirements

django-autoslug has been tested on Django 1.5 using Python 2.7.3.

Models being attached must have a proper `pk` attribute.

## Installation

    1. python setup.py install

## Usage

    from django.db import models
    from autoslug.fields import AutoSlugField

    class MyModel(models.Model):
        name = models.CharField(max_length=255) # required field
        slug = AutoSlugField(populate_from=('name',))

Recommended parameters:

* `populate_from` - A list or tuple of instance attribute names, custom functions, or both. If supplied, django-autoslug will default `editable` to false. This field is required for all of the optional parameters, meaning if it's not set, the field as good as a normal `CharField`. Custom functions are passed the current instance of the model. E.g. to create a slug from the model's primary key converted to base-36:

    slug = AutoSlugField(populate_from=(lambda instance: int_to_base36(instance.pk),))

Optional parameters:

* `separator` - The string used when piecing together slugs. Default `-`
* `always_update` - If true, the slug will change as the `populated_form` values change instead of just at creation. This is useful if you want the slug to reflect model changes and don't care about URLs breaking. Default `False`
* `slugify` - The function used to create slugs. Default `autoslug.utils.slugify`

`AutoSlugField` also accepts any of the default parameters available for `CharField`. Certain parameters that django-autoslug sets defaults for automatically are listed below:

* `max_length` - Default `255`
* `unique` - Default `True`
* `db_index` - Default `True`
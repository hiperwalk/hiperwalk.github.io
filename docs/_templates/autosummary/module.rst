.. currentmodule:: {{ module }}

.. automodule:: {{ objname }}

    {% block functions%}
    {% if functions %}
    .. autosummary::
        :toctree: generated

    {% for item in functions %}
        {{ item }}
    {% endfor %}

    {% endif %}
    {% endblock %}

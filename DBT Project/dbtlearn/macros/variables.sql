{% macro learn_variables() %}

    {% set your_name_jinja = "Mosh" %}
    {{ log("Hello " ~ your_name_jinja, info=True) }}

    {{ log("Hello " ~ var("user_name","NO USERNAME IS SET") ~ "!", info=True) }}
{% endmacro %}
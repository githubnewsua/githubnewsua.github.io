---
title: "{{ title }}"
date: {{ article_date }}
draft: false
---
Источник: {{ media_name }} {{ article_url }}

{% for paragraph in paragraphs %}
{{ paragraph }}
{% endfor %}
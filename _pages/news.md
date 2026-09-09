---
layout: single
permalink: /news/
author_profile: true
---

{% for post in site.posts %}
<p><strong>{{ post.date | date: "%d-%m-%y" }}</strong> &mdash; {{ post.content }}</p>
{% endfor %}

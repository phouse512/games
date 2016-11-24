---
layout: default
---

## Welcome
Hi there, welcome to a space for thoughts about all sorts of games. For now,
there's not much here, but I hope you'll come and visit now and then.

{% for post in site.posts %}
<a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
{% endfor %}

***
